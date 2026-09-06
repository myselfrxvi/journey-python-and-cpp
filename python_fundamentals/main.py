from typing import Any, Callable
from fastapi import FastAPI
import numpy as np 
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer

# 1. Load Neural Embedding Model
model = SentenceTransformer("all-MiniLM-L6-v2")

# 2. FastAPI Application
app = FastAPI(title="Enterprise Agent API")

# 3. Vector Math Core
def cosine_similarity(vec_a: Any, vec_b: Any) -> float:
    dot = np.dot(vec_a, vec_b)
    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)
    return float(dot / (norm_a * norm_b))

# 4. Tool Registry System
TOOL_REG: dict[str, Callable] = {}

def register_tool(name: str):
    def decorator(func: Callable):
        TOOL_REG[name] = func
        return func
    return decorator

def execute_ai_tool_call(args: dict) -> Any:
    tool_name = args.get("tool")
    tool_func = TOOL_REG.get(tool_name)
    if tool_func:
        return tool_func(**args.get("arguments", {}))
    raise ValueError(f"Tool '{tool_name}' not found")

@register_tool("calculate_discount")
def calculate_discount(price: float, discount: float) -> float:
    return price - (price * discount / 100)

@register_tool("convert_currency")
def convert_currency(price: float, from_cur: str, to_cur: str) -> float:
    if from_cur == to_cur:
        return price
    if from_cur == "USD" and to_cur == "INR":
        return price * 83.0
    return price

# 5. In-Memory Vector Database
class SimpleVectorDB:
    def __init__(self):
        self.documents = []
    
    def add_docs(self, doc_id: Any, text: str):
        encode = model.encode(text)
        self.documents.append({
            "id": doc_id,
            "text": text,
            "embedding": encode
        })

    def search(self, query: str, top_k: int = 1):
        query_emb = model.encode(query)
        scores = []
        for doc in self.documents:
            score = cosine_similarity(query_emb, doc["embedding"])
            scores.append({"text": doc["text"], "score": score})
        scores.sort(key=lambda x: x["score"], reverse=True)
        return scores[:top_k]

# Initialize Knowledgebase with enterprise data
db = SimpleVectorDB()
db.add_docs(1, "We are offering a flat 20% discount on all electronics starting today.")
db.add_docs(2, "Our headquarters is located at 500 Tech Parkway, San Francisco.")
db.add_docs(3, "To reset your password, visit the security settings page.")

# 6. RAG Prompt Generator with Confidence Score
def generate_rag_prompt(db: SimpleVectorDB, query: str):
    matches = db.search(query, top_k=1)
    retrieved_context = matches[0]["text"]
    score = matches[0]["score"]

    prompt = f"""Based on the following retrieved context about your query:
Question: {query}
Answer: {retrieved_context}"""
    
    confidence_pct = round(float(score) * 100, 1)
    return prompt, f"{confidence_pct}%"

# 7. Autonomous Agent Router
def route_and_execute(db: SimpleVectorDB, message: str):
    user_input_lower = message.lower()
    
    if "sale" in user_input_lower or "discount" in user_input_lower:
        print("🤖 [Agent Decision: Calling Tool 'calculate_discount']")
        res = execute_ai_tool_call({
            "tool": "calculate_discount",
            "arguments": {"price": 100.0, "discount": 20.0}
        })
        return res, "100.0%"
    
    elif "currency" in user_input_lower or "exchange" in user_input_lower or "rupee" in user_input_lower:
        print("🤖 [Agent Decision: Calling Tool 'convert_currency']")
        res = execute_ai_tool_call({
            "tool": "convert_currency",
            "arguments": {"price": 100.0, "from_cur": "USD", "to_cur": "INR"}
        })
        return res, "100.0%"

    else:
        print("🤖 [Agent Decision: Querying RAG Knowledgebase]")
        return generate_rag_prompt(db, message)

# 8. FastAPI Schemas & Endpoint
class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: Any
    confidence: str

@app.post("/agent/chat", response_model=ChatResponse)
def chat_endpoint(req: ChatRequest):
    result, confidence = route_and_execute(db, req.message)
    return ChatResponse(response=result, confidence=confidence)
