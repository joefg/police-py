import time
import pytest

from police_py import crime

@pytest.fixture(autouse=True)
def slow_down_tests():
    yield
    time.sleep(1)

def test_get_street_level_crimes_point():
    lat: float = 52.629729
    lng: float = -1.131592
    response = crime.get_street_level_crimes_point(
        lat, lng
    )
    assert response.status_code == 200


def test_get_street_level_crimes_poly():
    poly: str = '52.268,0.543:52.794,0.238:52.130,0.478'
    response = crime.get_street_level_crimes_poly(poly)
    assert response.status_code == 200


def test_get_street_level_outcomes_point():
    lat: float = 52.629729
    lng: float = -1.131592
    response = crime.get_street_level_outcomes_point(
        lat, lng
    )
    assert response.status_code == 200


def test_get_street_level_outcomes_poly():
    poly: str = '52.268,0.543:52.794,0.238:52.130,0.478'
    response = crime.get_street_level_crimes_poly(poly)
    assert response.status_code == 200


def test_get_crimes_with_no_location():
    category: str = "all-crimes"
    force: str = "metropolitan"
    response = crime.get_crimes_with_no_location(category, force)
    assert response.status_code == 200


def test_get_crime_categories():
    date = "2026-02"
    response = crime.get_crime_categories(date)
    assert response.status_code == 200


def test_get_crime_outcome():
    crime_id = "e11dade0a92a912d12329b9b2abb856ac9520434ad6845c30f503e9901d140f1"
    response = crime.get_crime_outcome(crime_id)
    assert response.status_code == 200
