import numpy as np 
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def cosine_sim(vec_a, vec_b):
    num = np.dot(vec_a,vec_b)
    deno = np.linalg.norm(vec_a)*np.linalg.norm(vec_b)
    return num/deno

class fintechpolicy:
    def __init__(self):
        self.documents = []
    
    def add_policy(self, policy_id: int, text: str):
        embedding = model.encode(text)
        self.documents.append({"id": policy_id, "text": text, "embedding": embedding})

    def query(self, user_question: str):
        query_encode = model.encode(user_question)
        scores = []
        for doc in self.documents:
            score = cosine_sim(query_encode, doc["embedding"])
            scores.append({"text": doc["text"], "score": score})
        scores.sort(key=lambda x: x["score"], reverse=True)
        best_doc = scores[0]
        confidence_pct = round(float(best_doc["score"]) * 100, 1)
        return {
            "policy": best_doc["text"],
            "confidence": f"{confidence_pct}%"
        }


db = fintechpolicy()
db.add_policy(1, "Daily domestic bank transfers are limited to $25,000 without requiring secondary video KYC verification.")
db.add_policy(2, "International wire transfers exceeding $10,000 require AML compliance review and settle within 2 to 3 business days.")
db.add_policy(3, "Accounts with more than 3 failed login attempts within 24 hours are temporarily locked for security verification.")
db.add_policy(4, "Crypto withdrawal transactions require mandatory 2-Factor Authentication and a 24-hour cooling period for new addresses.")

# Test query:
res = db.query("How much money can I send to a foreign country before review?")
print("Retrieved Policy:", res["policy"])
print("Confidence:", res["confidence"])
