from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request model
class ChatRequest(BaseModel):
    question: str

@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        llm = Ollama(model="llama3")
        
        # Build prompt
        prompt = PromptTemplate(
            input_variables=["question"],
            template="""
You are ClimaSense, a smart and friendly assistant that answers weather-related questions in a short and helpful way.

Question: {question}
Answer:
            """
        )
        
        final_prompt = prompt.format(question=req.question)
        response = llm(final_prompt)

        return {"answer": response}
    
    except Exception as e:
        return {"answer": f"Error occurred: {str(e)}"}
