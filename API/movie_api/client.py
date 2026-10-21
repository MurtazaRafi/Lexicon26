from pydantic import BaseModel

from api_client import get_json
import requests
import os
from dotenv import load_dotenv

BASE = "http://127.0.0.1:8000"

movies = get_json(f"{BASE}/movies")
# print(movies)


new_movie = {"title": "Snow Crash", "director": "Neal Stephenson", "year": 1992}

load_dotenv()
key = os.getenv("API_KEY")

headers = {"X-API-Key" : key}
response = requests.post(f"{BASE}/movies", json=new_movie, timeout=5, headers=headers)

print(response.status_code, response.json())

get_json(f"{BASE}/movies/99")

