import httpx

def get_neighbourhoods(force: str) -> httpx.Response:
    """Get neighbourhoods for a given force.

    Parameters:
    force: `str`
       Police force
    """

    return httpx.get(f"https://data.police.uk/api/{force}/neighbourhoods")


def get_neighbourhood(force: str, neighbourhood: str) -> httpx.Response:
    """Get a specific neighbourhood.

    Parameters:
    force: `str`
        Police force for which a neighbourhood would be served.
    neighbourhood: `str`
        Identifier for a specific neighbourhood, derviced from other API
        calls for the service.
    """

    return httpx.get(f"https://data.police.uk/api/{force}/{neighbourhood}")


def get_neighbourhood_bounds(force: str, neighbourhood: str) -> httpx.Response:
    """Get a specific neighbourhood's bounds.

    Parameters:
    force: `str`
        Police force for which a neighbourhood would be served.
    neighbourhood: `str`
        Identifier for a specific neighbourhood, derviced from other API
        calls for the service.

    Returns:
    List of lon/lat pairs describing the boundary.
    """

    return httpx.get(f"https://data.police.uk/api/{force}/{neighbourhood}/boundary")


def get_neighbourhood_team(force: str, neighbourhood: str) -> httpx.Response:
    """Get a specific neighbourhood's team.

    Parameters:
    force: `str`
        Police force for which a neighbourhood would be served.
    neighbourhood: `str`
        Identifier for a specific neighbourhood, derviced from other API
        calls for the service.
    """

    return httpx.get(f"https://data.police.uk/api/{force}/{neighbourhood}/people")


def get_neighbourhood_events(force: str, neighbourhood: str) -> httpx.Response:
    """Get a specific neighbourhood's events.

    Parameters:
    force: `str`
        Police force for which a neighbourhood would be served.
    neighbourhood: `str`
        Identifier for a specific neighbourhood, derviced from other API
        calls for the service.
    """

    return httpx.get(f"https://data.police.uk/api/{force}/{neighbourhood}/events")


def get_neighbourhood_priorities(force: str, neighbourhood: str) -> httpx.Response:
    """Get a specific neighbourhood's priorities.

    Parameters:
    force: `str`
        Police force for which a neighbourhood would be served.
    neighbourhood: `str`
        Identifier for a specific neighbourhood, derviced from other API
        calls for the service.
    """

    return httpx.get(f"https://data.police.uk/api/{force}/{neighbourhood}/priorities")


def get_neighbourhood_location(lng: float, lat: float) -> httpx.Response:
    """Get a specific neighbourhood's priorities.

    Parameters:
        lng: `float`
        lat: `float`
    """

    return httpx.get(f"https://data.police.uk/api/locate-neighbourhood?q={lat},{lng}")
