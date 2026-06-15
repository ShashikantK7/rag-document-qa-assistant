import os
import google.generativeai as genai

api_key = os.getenv('GOOGLE_API_KEY')

if not api_key:
    print('GOOGLE_API_KEY not found')
    raise SystemExit(1)

genai.configure(api_key=api_key)

print('Available models:')
for model in genai.list_models():
    print(f'Name: {model.name}')
    print(f'Supported methods: {model.supported_generation_methods}')
    print('-' * 50)
