import pytest
from app.house import House


def test_add_house():
    h = House("Villa", "Kigali", 500)
    assert h.name == "Villa"
    assert h.location == "Kigali"
    assert h.price == 500
    assert h.is_rented is False


def test_rent_house():
    h = House("Villa", "Kigali", 500)
    h.rent()
    assert h.is_rented is True

    with pytest.raises(Exception):
        h.rent()


def test_release_house():
    h = House("Villa", "Kigali", 500)
    h.rent()
    h.release()
    assert h.is_rented is False


def test_search_by_location():
    h1 = House("Villa", "Kigali", 500)
    h2 = House("Apartment", "Musanze", 300)
    houses = [h1, h2]

    results = [h for h in houses if h.location.lower() == "kigali"]
    assert results == [h1]


def test_show_available():
    h1 = House("Villa", "Kigali", 500)
    h2 = House("Apartment", "Musanze", 300)
    h1.rent()
    available = [h for h in [h1, h2] if not h.is_rented]
    assert available == [h2]
