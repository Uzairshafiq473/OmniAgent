# OmniAgent 🤖🌐  
**Unified AI Chatbot Interface for Multiple LLM Providers**  

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)

A powerful, multi-provider AI chatbot framework to interact with **Groq**, **GoogleAI**, and **DeepSeek** models. Customize agents, enable web search, and harness AI seamlessly!  

---

## ✨ Features  
- **Multi-Provider LLMs**: Switch between Groq (Llama3), Google Gemini, and DeepSeek models.  
- **Web Search Integration**: Real-time data via Tavily API.  
- **Customizable Agents**: Define system prompts to control AI behavior.  
- **Streamlit UI**: Clean and interactive interface.  
- **FastAPI Backend**: Scalable and efficient API.  

---

## 🛠️ Tech Stack  
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-FF6F00?logo=langchain&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-00B388?logo=groq&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?logo=google&logoColor=white)

---

## 🚀 Getting Started  

### Prerequisites  
- Python 3.9+  
- API keys for [Groq](https://console.groq.com/), [GoogleAI](https://makersuite.google.com/), [DeepSeek](https://openrouter.ai/keys), and [Tavily](https://tavily.com/).  

### Installation  
1. **Clone the repo**  
   ```bash  
   git clone https://github.com/your-username/OmniAgent.git  
   cd OmniAgent

# Project Setup Guide

This guide provides step-by-step instructions to set up your project environment, including setting up a Python virtual environment using Pipenv, pip, or conda.

## Table of Contents

1. [Setting Up a Python Virtual Environment](#setting-up-a-python-virtual-environment)
   - [Using Pipenv](#using-pipenv)
   - [Using pip and venv](#using-pip-and-venv)
   - [Using Conda](#using-conda)
2. [Running the application](#project-phases-and-python-commands)


## Setting Up a Python Virtual Environment

### Using Pipenv
1. **Install Pipenv (if not already installed):**  
```
pip install pipenv
```

2. **Install Dependencies with Pipenv:** 

```
pipenv install
```

3. **Activate the Virtual Environment:** 

```
pipenv shell
```

---

### Using `pip` and `venv`
#### Create a Virtual Environment:
```
python -m venv venv
```

#### Activate the Virtual Environment:
**macOS/Linux:**
```
source venv/bin/activate
```

**Windows:**
```
venv\Scripts\activate
```

#### Install Dependencies:
```
pip install -r requirements.txt
```

---

### Using Conda
#### Create a Conda Environment:
```
conda create --name myenv python=3.11
```

#### Activate the Conda Environment:
```
conda activate myenv
```

#### Install Dependencies:
```
pip install -r requirements.txt
```


# Project Phases and Python Commands

## Phase 1: Create AI Agent
```
python ai_agent.py
```

## Phase 2: Setup Backend with FastAPI
```
python backend.py
```

## Phase 3: Setup Frontend with Streamlit
```
python frontend.py
```

## IMPORTANT
### Make sure backend python script is running in a separate terminal
## 🚀 Getting Started  

### Prerequisites  
- Python 3.9+  
- API keys for [Groq](https://console.groq.com/), [GoogleAI](https://makersuite.google.com/), [DeepSeek](https://openrouter.ai/keys), and [Tavily](https://tavily.com/).  

### Installation  
1. **Clone the repo**  
   ```bash  
   git clone https://github.com/your-username/OmniAgent.git  
   cd OmniAgent

# Project Setup Guide

This guide provides step-by-step instructions to set up your project environment, including setting up a Python virtual environment using Pipenv, pip, or conda.

## Table of Contents

1. [Setting Up a Python Virtual Environment](#setting-up-a-python-virtual-environment)
   - [Using Pipenv](#using-pipenv)
   - [Using pip and venv](#using-pip-and-venv)
   - [Using Conda](#using-conda)
2. [Running the application](#project-phases-and-python-commands)


## Setting Up a Python Virtual Environment

### Using Pipenv
1. **Install Pipenv (if not already installed):**  
```
pip install pipenv
```

2. **Install Dependencies with Pipenv:** 

```
pipenv install
```

3. **Activate the Virtual Environment:** 

```
pipenv shell
```

---

### Using `pip` and `venv`
#### Create a Virtual Environment:
```
python -m venv venv
```

#### Activate the Virtual Environment:
**macOS/Linux:**
```
source venv/bin/activate
```

**Windows:**
```
venv\Scripts\activate
```

#### Install Dependencies:
```
pip install -r requirements.txt
```

---

### Using Conda
#### Create a Conda Environment:
```
conda create --name myenv python=3.11
```

#### Activate the Conda Environment:
```
conda activate myenv
```

#### Install Dependencies:
```
pip install -r requirements.txt
```


# Project Phases and Python Commands

## Phase 1: Create AI Agent
```
python ai_agent.py
```

## Phase 2: Setup Backend with FastAPI
```
python backend.py
```

## Phase 3: Setup Frontend with Streamlit
```
python frontend.py
```

## IMPORTANT
### Make sure backend python script is running in a separate terminal

## 🚀 Getting Started  

### Prerequisites  
- Python 3.9+  
- API keys for [Groq](https://console.groq.com/), [GoogleAI](https://makersuite.google.com/), [DeepSeek](https://openrouter.ai/keys), and [Tavily](https://tavily.com/).  

### Installation  
1. **Clone the repo**  
   ```bash  
   git clone https://github.com/your-username/OmniAgent.git  
   cd OmniAgent

# Project Setup Guide

This guide provides step-by-step instructions to set up your project environment, including setting up a Python virtual environment using Pipenv, pip, or conda.

## Table of Contents

1. [Setting Up a Python Virtual Environment](#setting-up-a-python-virtual-environment)
   - [Using Pipenv](#using-pipenv)
   - [Using pip and venv](#using-pip-and-venv)
   - [Using Conda](#using-conda)
2. [Running the application](#project-phases-and-python-commands)


## Setting Up a Python Virtual Environment

### Using Pipenv
1. **Install Pipenv (if not already installed):**  
```
pip install pipenv
```

2. **Install Dependencies with Pipenv:** 

```
pipenv install
```

3. **Activate the Virtual Environment:** 

```
pipenv shell
```

---

### Using `pip` and `venv`
#### Create a Virtual Environment:
```
python -m venv venv
```

#### Activate the Virtual Environment:
**macOS/Linux:**
```
source venv/bin/activate
```

**Windows:**
```
venv\Scripts\activate
```

#### Install Dependencies:
```
pip install -r requirements.txt
```

---

### Using Conda
#### Create a Conda Environment:
```
conda create --name myenv python=3.11
```

#### Activate the Conda Environment:
```
conda activate myenv
```

#### Install Dependencies:
```
pip install -r requirements.txt
```


# Project Phases and Python Commands

## Phase 1: Create AI Agent
```
python ai_agent.py
```

## Phase 2: Setup Backend with FastAPI
```
python backend.py
```

## Phase 3: Setup Frontend with Streamlit
```
python frontend.py
```

## IMPORTANT
### Make sure backend python script is running in a separate terminal

## 🏗 Technical Architecture

```mermaid
graph TD
    subgraph Phase_3[Phase 3: User Interaction]
        A[Streamlit UI] -->|API Request| B[FastAPI Backend]
        B -->|Response Payload| A
    end

    subgraph Phase_2[Phase 2: AI Processing]
        C[LLM Provider] --> D[LangGraph Agent]
        D --> E[Tools]
    end

    subgraph Phase_1[Phase 1: Foundation]
        F[Groq]
        G[Tavily]
        H[Miro]
    end

    Phase_3 -->|Processes Request| Phase_2
    Phase_2 -->|Utilizes| Phase_1
