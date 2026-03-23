import httpx

def get_stop_and_searches_point(lat: float, lng: float, date: str | None = None) -> httpx.Response:
    """Get stop-and-search reports within one mile of a single point.

    Parameters:
    lat, lng: `float`
        The point's coordinate using WGS-84 projection.
    date: `str`, optional
        Reporting month, in format <yyyy-mm>.
    """

    args = ""
    if date: args += f"date={date}&"
    args += f"lat={lat}&lng={lng}"
    return httpx.get(
        f"https://data.police.uk/api/stops-street?{args}"
    )


def get_stop_and_searches_poly(poly: str, date: str | None = None) -> httpx.Response:
    """Get stop-and-search crime reports within a custom polygon.

    Parameters:
    poly: `str`
        A series of lng/lat pairs, separated by colon, in the format of
        [lat],[lng]:[lat],[lng]:[lat],[lng]
    date: `str`, optional
        Reporting month, in format <yyyy-mm>.
    """

    args = ""
    if date: args += f"date={date}&"
    args += f"poly={poly}"
    return httpx.get(
        f"https://data.police.uk/api/stops-street?{args}"
    )


def get_stop_and_searches_at_location(location: str, date: str | None = None) -> httpx.Response:
    """Get stop-and-searches for a particular location.

    Parameters:
    location: `str`
        The ID of the location to get stop and searches for.
    date: `str`, optional
        Reporting month, in format <yyyy-mm>.
    """

    args = ""
    if date: args += f"date={date}&"
    args += f"location={location}&"
    return httpx.get(
        f"https://data.police.uk/api/stops-no-location?{args}"
    )


def get_stop_and_searches_with_no_location(force: str, date: str | None = None) -> httpx.Response:
    """Get stop-and-searches for a force that could not be mapped to a location.

    Parameters:
    force: `str`
        Force under which the search occured.
    date: `str`, optional
        Reporting month, in format <yyyy-mm>.
    """

    args = ""
    if date: args += f"date={date}&"
    args += f"force={force}&"
    return httpx.get(
        f"https://data.police.uk/api/stops-no-location?{args}"
    )


def get_stop_and_searches_by_force(force: str, date: str) -> httpx.Response:
    """Get a list of valid categories for a given data set date.

    Parameters:
    force: `str`
        Jurisdictional police force.
    date: `str`
        Reporting month, in format <yyyy-mm>.
    """

    return httpx.get(
        f"https://data.police.uk/api/stops-force?date={date}&force={force}"
    )
