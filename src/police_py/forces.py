import httpx

def get_forces() -> httpx.Response:
    return httpx.get("https://data.police.uk/api/forces")


def get_force(force: str) -> httpx.Response:
    return httpx.get(f"https://data.police.uk/api/forces/{force}")


def get_force_people(force: str) -> httpx.Response:
    return httpx.get(f"https://data.police.uk/api/forces/{force}/people")
