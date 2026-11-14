import os

from dotenv import load_dotenv

load_dotenv()

BASE_URL=os.getenv(
    "BASE_URL",
    "http://2.59.41.2:6700"
)

DEFAULT_TIMEOUT=int(os.getenv("DEFAULT_TIMEOUT", "10000"))
SUCCESS_URL=os.getenv("SUCCESS_URL", f"{BASE_URL}/")