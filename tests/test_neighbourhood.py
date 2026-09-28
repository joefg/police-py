import time
import pytest

from police_py import neighbourhood

@pytest.fixture(autouse=True)
def slow_down_tests():
    yield
    time.sleep(1)

def test_get_neighbourhoods():
    force = "metropolitan"
    response = neighbourhood.get_neighbourhoods(force)
    assert response.status_code == 200

def test_get_neighbourhood():
    force = "essex"
    neighbourhood_code = "WC102"
    response = neighbourhood.get_neighbourhood(force, neighbourhood_code)
    assert response.status_code == 200

def test_get_neighbourhood_bounds():
    force = "essex"
    neighbourhood_code = "WC102"
    response = neighbourhood.get_neighbourhood_bounds(force, neighbourhood_code)
    assert response.status_code == 200

def test_get_neighbourhood_team():
    force = "essex"
    neighbourhood_code = "WC102"
    response = neighbourhood.get_neighbourhood_team(force, neighbourhood_code)
    assert response.status_code == 200

def test_get_neighbourhood_events():
    force = "essex"
    neighbourhood_code = "WC102"
    response = neighbourhood.get_neighbourhood_events(force, neighbourhood_code)
    assert response.status_code == 200

def test_get_neighbourhood_priorities():
    force = "essex"
    neighbourhood_code = "WC102"
    response = neighbourhood.get_neighbourhood_priorities(force, neighbourhood_code)
    assert response.status_code == 200

def test_get_neighbourhood_location():
    lng: float = -1.131592
    lat: float = 52.629729
    response = neighbourhood.get_neighbourhood_location(lng, lat)
    assert response.status_code == 200
