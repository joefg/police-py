import httpx

def get_street_level_crimes_point(lat: float, lng: float, date: str | None = None) -> httpx.Response:
    """Get street-level crime reports within one mile of a single point.

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
        f"https://data.police.uk/api/crimes-street/all-crime?{args}"
    )


def get_street_level_crimes_poly(poly: str, date: str | None = None) -> httpx.Response:
    """Get street-level crime reports within a custom polygon.

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
        f"https://data.police.uk/api/crimes-street/all-crime?{args}"
    )


def get_street_level_outcomes_point(lat: float, lng: float, date: str | None = None) -> httpx.Response:
    """Get street-level crime outcomes within one mile of a single point.

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
        f"https://data.police.uk/api/outcomes-at-location?{args}"
    )


def get_street_level_outcomes_poly(poly: str, date: str | None = None) -> httpx.Response:
    """Get street-level crime outcomes within a custom polygon.

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
        f"https://data.police.uk/api/outcomes-at-location?{args}"
    )


def get_crimes_with_no_location(category: str, force: str, date: str | None = None) -> httpx.Response:
    """Get crimes for a force that could not be mapped to a location.

    Parameters:
    category: `str`
        Category of crimes, available from <https://data.police.uk/docs/method/crime-categories>
    force: `str`
        Force under which the crimes occured.
    date: `str`, optional
        Reporting month, in format <yyyy-mm>.
    """

    args = ""
    if date: args += f"date={date}&"
    args += f"category={category}&"
    args += f"force={force}&"
    return httpx.get(
        f"https://data.police.uk/api/crimes-no-location?{args}"
    )


def get_crime_categories(date: str) -> httpx.Response:
    """Get a list of valid categories for a given data set date.

    Parameters:
    date: `str`
        Reporting month, in format <yyyy-mm>.
    """
    return httpx.get(
        f"https://data.police.uk/api/crime-categories?date={date}"
    )


def get_crime_last_updates() -> httpx.Response:
    """Get a date of when crime data in the API was last updated.
    """
    return httpx.get(
        "https://data.police.uk/api/crime-last-updated"
    )


def get_crime_outcome(crime_id: str) -> httpx.Response:
    """Return the case history for a specified crime.

    Parameters:
    crime_id: `str`
        A 64-character identifier for a crime as returned by other
        API methods.
    """
    return httpx.get(
        f"https://data.police.uk/api/outcomes-for-crime/{crime_id}"
    )
