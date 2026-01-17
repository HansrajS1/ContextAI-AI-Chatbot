import requests
from config.config import SERP_API_KEY

def web_search(query):
    url = "https://serpapi.com/search"
    params = {
        "q": query,
        "api_key": SERP_API_KEY,
        "engine": "google"
    }
    response = requests.get(url, params=params)
    data = response.json()

    results = []
    for item in data.get("organic_results", [])[:3]:
        results.append(item["snippet"])
    
    return "\n".join(results)
