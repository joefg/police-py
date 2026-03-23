import httpx

def get_availability(dataset: str) -> httpx.Response:
    return httpx.get(f"https://data.police.uk/api/{dataset}")
