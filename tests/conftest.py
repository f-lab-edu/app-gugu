from typing import Generator

import pytest
from fastapi.testclient import TestClient

from main import app


@pytest.fixture(scope="session")
def mock_client() -> Generator[TestClient, None, None]:
    client = TestClient(app)
    yield client
