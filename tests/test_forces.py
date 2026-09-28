import time
import pytest

from police_py import forces

@pytest.fixture(autouse=True)
def slow_down_tests():
    yield
    time.sleep(1)

def test_get_forces():
    response = forces.get_forces()
    assert response.status_code == 200


def test_get_force():
    force = "metropolitan"
    response = forces.get_force(force)
    assert response.status_code == 200


def test_get_force_people():
    force = "metropolitan"
    response = forces.get_force_people(force)
    assert response.status_code == 200
