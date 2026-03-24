import time
import pytest

from police_py import stop_and_search

@pytest.fixture(autouse=True)
def slow_down_tests():
    yield
    time.sleep(1)

def test_get_stop_and_searches_point_point():
    lat: float = 52.629729
    lng: float = -1.131592
    response = stop_and_search.get_stop_and_searches_point(
        lat, lng
    )
    assert response.status_code == 200


def test_get_street_level_crimes_poly():
    poly: str = '52.268,0.543:52.794,0.238:52.130,0.478'
    response = stop_and_search.get_stop_and_searches_poly(poly)
    assert response.status_code == 200


def test_get_stop_and_searches_at_location():
    location: str = "1609590"
    date: str = "2026-01"
    response = stop_and_search.get_stop_and_searches_at_location(location, date)
    assert response.status_code == 200


def test_get_stop_and_searches_with_no_location():
    date: str = "2026-01"
    force: str = "metropolitan"
    response = stop_and_search.get_stop_and_searches_with_no_location(force, date)
    assert response.status_code == 200


def test_get_stop_and_searches_by_force():
    date: str = "2026-01"
    force: str = "metropolitan"
    response = stop_and_search.get_stop_and_searches_by_force(force, date)
    assert response.status_code == 200
