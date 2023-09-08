
import openai

# API 요청 보내기
def chat(prompt, api_key):

    openai.api_key = api_key
    messages = [
        {"role": "system", "content":"You are a helpful assistant"},
        {"role": "user", "content":prompt}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
    )
    return response.choices[0].message['content']

response = chat("집에서 할 수 있는 건강한 습관", "")
print(response)
