import os
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import AIMessage
from openai import OpenAI
from langchain_google_genai import ChatGoogleGenerativeAI  # Added GoogleAI

# API Keys
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
DEEPSEEK_R1_ZERO_FREE = os.environ.get("DEEPSEEK_R1_ZERO_FREE")
DEEPSEEK_R1_DISTILL_QWEN_32B = os.environ.get("DEEPSEEK_R1_DISTILL_QWEN_32B")
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")  # Added GoogleAI API key

def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider == "Groq":
        llm = ChatGroq(model=llm_id, api_key=GROQ_API_KEY) 
        # Create Agent for Groq
        tools = [TavilySearchResults(api_key=TAVILY_API_KEY, max_results=2)] if allow_search else []
        agent = create_react_agent(
            model=llm,
            tools=tools
        )
        # Include system prompt in the initial state
        state = {
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query}
            ]
        }

        # Invoke the agent
        response = agent.invoke(state)
        messages = response.get("messages", [])
        ai_messages = [msg.content for msg in messages if isinstance(msg, AIMessage)]
        
        return ai_messages[-1] if ai_messages else "No response available"

    elif provider == "GoogleAI":
        # Initialize Google Generative AI model
        llm = ChatGoogleGenerativeAI(model=llm_id, api_key=GOOGLE_API_KEY)
        
        # Create Agent for GoogleAI
        tools = [TavilySearchResults(api_key=TAVILY_API_KEY, max_results=2)] if allow_search else []
        agent = create_react_agent(
            model=llm,
            tools=tools
        )
        
        # Include system prompt in the initial state
        state = {
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query}
            ]
        }
        
        # Invoke the agent
        response = agent.invoke(state)
        messages = response.get("messages", [])
        ai_messages = [msg.content for msg in messages if isinstance(msg, AIMessage)]
        
        return ai_messages[-1] if ai_messages else "No response available"

    elif provider == "DeepSeek":
        # Select the correct API key based on the model
        api_key = (
            DEEPSEEK_R1_ZERO_FREE if llm_id == "deepseek/deepseek-r1-zero:free" 
            else DEEPSEEK_R1_DISTILL_QWEN_32B
        )
        
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,  # Use the correct API key
        )
        response = client.chat.completions.create(
            model=llm_id,  # Use the provided model ID
            messages=[{"role": "user", "content": query}],
            extra_headers={
                "HTTP-Referer": "http://localhost:3000",
                "X-Title": "AI Agent"
            }
        )
        # Remove \boxed{} from the response
        response_text = response.choices[0].message.content
        response_text = response_text.replace("\\boxed{", "").replace("}", "")
        return response_text


    else:
        raise ValueError(f"Unsupported provider: {provider}")