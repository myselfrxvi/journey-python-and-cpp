import torch.nn as nn
import torch
import math

class CausalSelfAttention(nn.Module):
    def __init__(self, d_model: int, n_heads: int):
        super().__init__()
        assert d_model % n_heads == 0
        self.d_model = d_model
        self.n_heads = n_heads
        self.head_dim = d_model // n_heads 
        self.qkv_proj = nn.Linear(d_model, 3*d_model)
        self.out_proj = nn.Linear(d_model, d_model)
    def forward(self, x: torch.Tensor):
        B,T,D = x.shape 
        q,k,v = self.qkv_proj(x).chunk(3, dim=-1)
        q = q.view(B,T,self.n_heads, self.head_dim).transpose(1,2) 
        k = k.view(B,T,self.n_heads, self.head_dim).transpose(1,2)
        v = v.view(B,T,self.n_heads, self.head_dim).transpose(1,2)
        scores = (q @ k.transpose(-2,-1)) /math.sqrt(self.head_dim)
        mask = torch.triu(torch.ones(T,T), diagonal=1).bool()
        scores = scores.masked_fill(mask, float('-inf'))
        weights = torch.softmax(scores, dim = -1)
        out = weights @ v
        out = out.transpose(1,2).contiguous().view(B,T,D)
        return self.out_proj(out) 
        
class FeedForward(nn.Module):
    def __init__(self, d_model:int):
        super().__init__()
        self.gelu = nn.GELU()
        self.f1 = nn.Linear(d_model, 4*d_model)
        self.f2 = nn.Linear(4*d_model, d_model)

    def forward(self, x:T.Tensor):
        return self.f2(self.gelu(self.f1(x)))

class TransformerBlock(nn.Module):
    def __init__(self, d_model: int, n_heads: int):
        super().__init__()
        self.ln1 = nn.LayerNorm(d_model)
        self.attn = CausalSelfAttention(d_model, n_heads)
        self.ln2 = nn.LayerNorm(d_model)
        self.ff = FeedForward(d_model)

    def forward(self, x:torch.Tensor) -> torch.Tensor:
        x = self.ln1(x + self.attn(x))
        x = self.ln2(x + self.ff(x))
        return x


if __name__ == "__main__":
    print("Testing your Transformer Block...")
    x = torch.randn(2, 6, 64)  
    block = TransformerBlock(d_model=64, n_heads=4)
    out = block(x)
    print(f"Input:  {x.shape}")
    print(f"Output: {out.shape}")
    print("SUCCESS: Full GPT Transformer Block working end-to-end!")
