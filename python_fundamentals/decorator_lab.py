import time
import functools

def measure_latency(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Function '{func.__name__}' executed in {end_time - start_time}")
        return result
    return wrapper

@measure_latency
def simulate_model_inference(prompt: str, tokens: int = 50):
    time.sleep(0.5)
    return f"Generated response for: '{prompt}' ({tokens} tokens)"

def retry(max_attempts: int, delay: float):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts+1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt < max_attempts:
                        print(f"Retrying {func.__name__} ({delay}s delay)...")
                        time.sleep(delay)
                    else:
                        raise e 
        return wrapper 
    return decorator


result = simulate_model_inference("What is Python?", tokens=100)
print("Result:", result)
print("Preserved Function Name:", simulate_model_inference.__name__)

attempt_counter = 0

@retry(max_attempts=3, delay= 0.3)
def unstable_network_call():
    global attempt_counter
    attempt_counter += 1
    if attempt_counter < 3:
        raise ConnectionError("503 Service Unavailable")
    return "✅ 200 OK: Data successfully fetched!"

print("\n--- 🔄 Testing Auto-Retry Decorator ---")
output = unstable_network_call()
print("Final Output:", output)
