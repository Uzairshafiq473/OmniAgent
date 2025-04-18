from pydantic import BaseModel
from typing import List, Dict
from fastapi import FastAPI, HTTPException
from ai_agent import get_response_from_ai_agent
import uvicorn

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[Dict[str, str]]
    allow_search: bool

app = FastAPI(title="LangGraph AI Agent")

# Add root endpoint to prevent 404 errors
@app.get("/")
async def health_check():
    return {
        "status": "API is running", 
        "endpoints": {
            "chat": "/chat (POST)",
            "docs": "/docs"
        }
    }

ALLOWED_MODELS = {
    "Groq": ["llama3-70b-8192", "llama-3.3-70b-versatile"],
    "DeepSeek": ["deepseek/deepseek-r1-zero:free", "deepseek/deepseek-r1-distill-qwen-32b:free"],
    "GoogleAI": ["gemini-2.0-pro-exp-02-05","gemini-1.5-flash"]
}

@app.post("/chat")
async def chat_endpoint(request: RequestState):
    if request.model_provider not in ALLOWED_MODELS:
        raise HTTPException(status_code=400, detail="Invalid provider")
    
    if request.model_name not in ALLOWED_MODELS[request.model_provider]:
        raise HTTPException(status_code=400, detail="Invalid model for provider")

    try:
        response = get_response_from_ai_agent(
            llm_id=request.model_name,
            query=request.messages[-1]["content"],
            allow_search=request.allow_search,
            system_prompt=request.system_prompt,
            provider=request.model_provider
        )
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run(
        "backend:app",
        host="0.0.0.0",
        port=8000,
        reload=False,
        workers=1
    )