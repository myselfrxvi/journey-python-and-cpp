import sys
class DataSetStreamer:
    def __init__(self, limit: int):
        self.limit = limit 
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            self.current +=1
            return self.current
        else: 
            raise StopIteration

def stream_batches(dataset: list[str], batchsize: int):
    for i in range(0, len(dataset), batchsize):
        yield dataset[i:i+batchsize]

streamer = DataSetStreamer(limit=3)
sample_data = ["doc_1", "doc_2", "doc_3", "doc_4", "doc_5", "doc_6", "doc_7"]


for batch in stream_batches(sample_data, batchsize=2):
    print("GPU Processing Batch:", batch)

for num in streamer:
    print("Streamed item:", num)

list_data = [x ** 2 for x in range(1_000_000)]
gen_data  = (x ** 2 for x in range(1_000_000))
print("\n--- 📊 Memory Comparison ---")
print(f"List Comprehension Size: {sys.getsizeof(list_data):,} bytes")
print(f"Generator Expression Size: {sys.getsizeof(gen_data):,} bytes")


raw_logs = [
    "INFO: Server started at port 8000",
    "ERROR: Database connection timeout (Code: 504)",
    "WARNING: Disk usage at 85%",
    "ERROR: Invalid JWT token signature (Code: 401)",
    "INFO: User logged in",
    "ERROR: Rate limit exceeded (Code: 429)"
]


def filter_errors(logs: list[str]):
    for log in logs:
        if "ERROR" in log:
            yield log

def extract_error_code(error_logs):
    for log in error_logs:
        code = log.split("Code:")[1].rstrip(")")
        yield code

# Conveyor belt connection:
error_stream = filter_errors(raw_logs)
code_stream  = extract_error_code(error_stream)

print("\n--- 🚨 Streaming Error Codes ---")
for code in code_stream:
    print("Found Error Code:", code)
