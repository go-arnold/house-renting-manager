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
