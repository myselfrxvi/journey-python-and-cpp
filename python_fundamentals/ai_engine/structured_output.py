import json 
from pydantic import BaseModel, Field

class supportTic(BaseModel):
    customer_name: str
    issue_category: str  
    urgency_level: int = Field(ge=1, le=5) 
    requires_human: bool
    summary: str
    
def parse_llm_response(raw_llm_json):
        data = json.loads(raw_llm_json)
        return supportTic(**data)

fake_llm_output = """
{
    "customer_name": "Marcus Aurelius",
    "issue_category": "billing",
    "urgency_level": 4,
    "requires_human": true,
    "summary": "Charged twice for annual cloud subscription."
}
"""
ticket = parse_llm_response(fake_llm_output)
print(f"✅ Parsed Ticket for: {ticket.customer_name}")
print(f"Urgency: {ticket.urgency_level}/5 | Needs Human: {ticket.requires_human}")