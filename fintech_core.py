import torch as T 
import torch.nn as nn

class fraudrisk(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Linear(4,8)
        self.relu = nn.ReLU()
        self.layer2 = nn.Linear(8,1)
        self.sigmoid = nn.Sigmoid()

    def forward(self,x):
        x = self.layer1(x)
        x = self.relu(x)
        x = self.layer2(x)
        x = self.sigmoid(x)
        return x
    
    def predict_fraud(model: fraudrisk, features: list[float]):
        x = T.tensor(features, dtype=T.float32).unsqueeze(0)
        model.eval()
        with T.no_grad():
            pred = model(x).item()
        return pred 
def normalize_transaction(amount: float, age_days: float, failed: float, is_foreign: float) -> list[float]:
    return [
        amount / 10000.0,
        min(age_days / 365.0, 1.0),
        min(failed / 5.0, 1.0),
        is_foreign
    ]

# 1. Historical Training Data: [amount, account_age, failed_logins, is_foreign]
# Normalized amounts: $50 -> 0.05, $5000 -> 5.0
X_train = T.tensor([
    normalize_transaction(50.0, 300.0, 0.0, 0.0),   # SAFE (0.0)
    normalize_transaction(120.0, 180.0, 0.0, 0.0),  # SAFE (0.0)
    normalize_transaction(250.0, 450.0, 1.0, 0.0),  # SAFE (0.0)
    normalize_transaction(8500.0, 2.0, 4.0, 1.0),   # FRAUD (1.0)
    normalize_transaction(6000.0, 5.0, 3.0, 1.0),   # FRAUD (1.0)
    normalize_transaction(9200.0, 1.0, 5.0, 1.0),   # FRAUD (1.0)
], dtype=T.float32)

y_train = T.tensor([[0.0], [0.0], [0.0], [1.0], [1.0], [1.0]], dtype=T.float32)


model = fraudrisk()
model.eval()
criterion = nn.BCELoss()
optimizer = T.optim.Adam(model.parameters(), lr=0.05)

for epoch in range(100):
    preds = model(X_train)
    loss = criterion(preds, y_train)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print(f"Model Trained! Final Loss: {loss.item():.4f}")

# Safe user: $80, 200 days old, 0 fails, domestic
safe_tx = normalize_transaction(80.0, 200.0, 0.0, 0.0)
print(f"Safe Tx Risk:  {fraudrisk.predict_fraud(model, safe_tx) * 100:.1f}%")

# Fraudster: $7,500, 2 days old, 4 fails, international IP
fraud_tx = normalize_transaction(7500.0, 2.0, 4.0, 1.0)
print(f"Fraud Tx Risk: {fraudrisk.predict_fraud(model, fraud_tx) * 100:.1f}%")


        