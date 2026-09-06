from fastapi import FastAPI
from pydantic import BaseModel, Field
from fintech_core import model, fraudrisk, normalize_transaction
from fintech_rag import db as policy_db
from fintech_tools import execute_financial_tool

app = FastAPI(title="FinTech")
class TransactionPayload(BaseModel):
    amount: float = Field(gt=0)
    account_age_days: float = Field(ge=0)
    failed_attempts_last_24h: float = Field(ge=0)
    is_foreign_ip: float = Field(ge=0, le=1)

class FraudResponse(BaseModel):
    risk_score_pct: str
    decision: str

@app.post("/fintech/evaluate-fraud", response_model=FraudResponse)
def evaluate_fraud(tx: TransactionPayload):
    features = normalize_transaction(
        tx.amount, 
        tx.account_age_days, 
        tx.failed_attempts_last_24h, 
        tx.is_foreign_ip
    )
    risk = fraudrisk.predict_fraud(model, features)
    if risk >= 0.70:
        decision = "BLOCKED: High Fraud Risk"
    elif risk >= 0.30:
        decision = "FLAGGED: Review Required"
    else:
        decision = "APPROVED: Safe Transaction"
        
    return FraudResponse(
        risk_score_pct=f"{risk * 100:.1f}%",
        decision=decision
    )
class AdvisorRequest(BaseModel):
    message: str

class AdvisorResponse(BaseModel):
    action: str        # "tool_call" or "compliance_rag"
    result: str
    confidence: str

@app.post("/fintech/advisor", response_model=AdvisorResponse)
def fintech_advisor(req: AdvisorRequest):
    msg = req.message.lower()
    
    # Branch A: Did the user ask for compound interest?
    if "interest" in msg or "compound" in msg:
        res = execute_financial_tool("calculate_compound_interest", {
            "principal": 10000.0, "annual_rate_pct": 7.0, "years": 10
        })
        return AdvisorResponse(
            action="tool_call",
            result=f"Compound investment value: ${res:,.2f}",
            confidence="100.0%"
        )
        
    # Branch B: Did the user ask for currency conversion?
    elif "convert" in msg or "currency" in msg or "usd" in msg or "inr" in msg:
        res = execute_financial_tool("convert_currency", {
            "amount": 100.0, "from_curr": "USD", "to_curr": "INR"
        })
        return AdvisorResponse(
            action="tool_call",
            result=f"Converted currency amount: {res}",
            confidence="100.0%"
        )
        
    # Branch C: Otherwise -> Consult the FinTech Compliance Policy Vector RAG!
    else:
        rag_res = policy_db.query(req.message)
        return AdvisorResponse(
            action="compliance_rag",
            result=rag_res["policy"],
            confidence=rag_res["confidence"]
        )
