import os
from dotenv import load_dotenv
import litellm

# Load your .env
load_dotenv()

model = os.getenv("MODEL")
api_key = os.getenv("NVIDIA_NIM_API_KEY")
api_base = "https://integrate.api.nvidia.com/v1"

print(f"🔑 Model: {model}")
print(f"🌐 Endpoint: {api_base}")

# Force drop unsupported params
response = litellm.completion(
    model=model,
    messages=[{"role": "user", "content": "Give me 3 startup ideas in Brazil"}],
    api_key=api_key,
    api_base=api_base,
    drop_params=True,
    additional_drop_params=["logprobs", "stop"]
)

print("✅ Response:", response["choices"][0]["message"]["content"])
