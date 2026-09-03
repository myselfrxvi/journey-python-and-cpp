from typing import Callable, Any
import functools
import time 

FINANCIAL_TOOL: dict[list, str, Callable] = {}

def register_tools(name:str):
    def decorator(func: Callable):
        FINANCIAL_TOOL[name] = func
        return func 
    return decorator
def execute_financial_tool(tool_name: str, args: dict[str, Any]) -> Any:
    if tool_name not in FINANCIAL_TOOL:
        raise ValueError(f"Tool '{tool_name}' not found!")
    return FINANCIAL_TOOL[tool_name](**args)

@register_tools("calculate_compound_interest")
def calculate_compound_interest(principal: float, annual_rate_pct: int, years: int):
    future_value = principal * ((1 + annual_rate_pct/100) ** years)
    return round(future_value, 2)

@register_tools("convert_currency")
def convert_currency(price: float, from_curr: str, to_cur: str):
    pass 

@register_tools("get_historical_rate")
def get_historical_rate(amount: float, from_curr: str, to_curr: str):
    pass 

@register_tools("estimate_capital_gains_tax")
def estimate_capital_gains_tax(profit: float, holding_period_months: int):
    if holding_period_months <=12:
        tax_rate = 0.15
    else:
        tax_rate = 0.20
    return round(profit * tax_rate, 2)   

# 1. Test Compound Interest: $10,000 at 7% for 10 years:
inv_result = execute_financial_tool("calculate_compound_interest", {
    "principal": 10000.0, "annual_rate_pct": 7.0, "years": 10
})
print("Investment Growth:", inv_result)

# 2. Test Tax: $5,000 profit held for 8 months (short term):
tax_result = execute_financial_tool("estimate_capital_gains_tax", {
    "profit": 5000.0, "holding_period_months": 8
})
print("Estimated Tax:", tax_result)
