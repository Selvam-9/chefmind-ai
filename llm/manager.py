from llm import openrouter
from llm.gemini import generate_answer as gemini_generate
from llm.openrouter import generate_answer as openrouter_generate



def generate_answer(prompt):

    providers = [
        ("Gemini", gemini_generate),
        ("OpenRouter", openrouter_generate),
        #("Groq", groq_generate)
    ]

    for provider_name, provider in providers:

        try:

            print(f"Trying {provider_name}...")

            answer = provider(prompt)

            print(f"{provider_name} Success")

            return answer, provider_name

        except Exception as e:

            print(f"{provider_name} Failed: {e}")

    return (
    "Sorry, all AI providers are currently unavailable. Please try again later.",
    "None")
