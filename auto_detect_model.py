import os
from google import genai

key = os.environ.get("AIzaSyDcrSkHqvEGQqhHBFTJ3PQuq6y1pZXcGVM")
client = genai.Client(api_key=key)

print("Starting model auto-detection...")
candidates = []
try:
    for m in client.models.list():
        # Heuristic: try models that sound generative
        if any(x in m.name for x in ["flash", "pro", "generate"]):
            candidates.append(m.name)
except Exception as e:
    print(f"List failed: {e}")
    exit(1)

print(f"Found {len(candidates)} candidates.")

working_model = None

for model_name in candidates:
    print(f"Testing {model_name}...", end=" ")
    try:
        # Try a simple generation
        client.models.generate_content(model=model_name, contents="Hello")
        print("SUCCESS!")
        working_model = model_name
        break
    except Exception as e:
        print(f"Failed ({str(e)[:50]}...)")

if working_model:
    print(f"RECOMMENDED MODEL: {working_model}")
else:
    print("No working generative model found.")
