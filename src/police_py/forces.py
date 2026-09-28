import httpx2

def get_forces() -> httpx2.Response:
    return httpx2.get("https://data.police.uk/api/forces")


def get_force(force: str) -> httpx2.Response:
    return httpx2.get(f"https://data.police.uk/api/forces/{force}")


def get_force_people(force: str) -> httpx2.Response:
    return httpx2.get(f"https://data.police.uk/api/forces/{force}/people")
