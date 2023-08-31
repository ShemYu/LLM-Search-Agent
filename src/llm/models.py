import openai
from decouple import config

OPENAI_API_KEY = config("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY


def get_model(name):
    if name == "gpt3":
        return openai.Model("text-davinci-003")

    if name == "codegen":
        return openai.Model("code-davinci-002")
    # TODO: Add others llm models

    # Fallback default model
    return openai.Model("text-curie-001")
