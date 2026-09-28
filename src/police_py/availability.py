import httpx2

def get_availability(dataset: str) -> httpx2.Response:
    return httpx2.get(f"https://data.police.uk/api/{dataset}")
