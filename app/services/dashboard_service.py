from python_scripts.generate_dashboard import generate_dashboard as generate
import httpx


async def generate_dashboard(dataset: str):
    # Call your existing dashboard generation script
    dashboard = generate(dataset)
    return dashboard


async def ask_chatgpt(question: str):
    # Implement ChatGPT API call here
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENAI_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": "gpt-3.5-turbo",
                "messages": [{"role": "user", "content": question}],
            },
        )
    return response.json()["choices"][0]["message"]["content"]
