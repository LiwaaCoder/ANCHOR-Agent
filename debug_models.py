import os
from google import genai

key = os.environ.get("GOOGLE_API_KEY")
if not key:
    print("No key found")
    exit(1)

client = genai.Client(api_key=key)

try:
    print("Listing models...")
    # 'config' might be needed for v1beta in some SDK versions, but let's try default first.
    # The error message suggested 'Call ListModels'. 
    # In the new SDK, it is client.models.list()
    for m in client.models.list():
        if "1.5" in m.name:
            print(f"Model: {m.name}")
except Exception as e:
    print(f"Error listing models: {e}")
