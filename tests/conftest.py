import pytest
from fastapi.testclient import TestClient

from src.main import app


@pytest.fixture()
def client():
    # Dependency override
    yield TestClient(app)
