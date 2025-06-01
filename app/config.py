import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")
os.environ["LANGSMITH_PROJECT"] = os.getenv("LANGSMITH_PROJECT", "default")

if not os.environ.get("FIREWORKS_API_KEY"):
    from getpass import getpass
    os.environ["FIREWORKS_API_KEY"] = getpass("Enter API key for Fireworks AI: ")