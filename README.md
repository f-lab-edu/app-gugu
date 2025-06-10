<h1 align="center">App Gugu 🕊️</h1>
<p align="center">This is very simple and quick example how to make the FastAPI app by designing in terms of CNCF</p>

## Overview

```plaintext
app-gugu/
├── Dockerfile
├── README.md
├── __pycache__
│   └── main.cpython-311.pyc
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── __pycache__
│   ├── main.py
│   ├── model
│   └── service
└── tests
    ├── __pycache__
    ├── conftest.py
    ├── service
    └── test_main.py
```

### Installation

This project uses [uv](https://docs.astral.sh/uv/), If you need to install it, Use the snippet as follows.

```bash
pip install uv
```

And then install all dependencies by using `requirements.txt`.

```bash
uv pip install -r requirements.txt
```

You can run the server by using [uvicorn](https://www.uvicorn.org/).

```bash
PYTHONPATH=$(pwd)/src uvicorn src.main:app --host 0.0.0.0 --port 8000
```

### Docker

**Building**

```bash
docker build . -t fastapi_gugu:latest
```

**Runninng**

```bash
docker run -dit --name your-app -p 8000:8000 fastapi_gugu
```

**Testing via cURL**

```bash
curl localhost:8000/health

# expected result
# {"status":"ok","is_error":false,"result":null}
```

### Unittest

```bash
PYTHONPATH=$(pwd)/src pytest tests/
```

### Coverage

```bash
PYTHONPATH=$(pwd)/src pytest --cov --cov-report=term --cov-report=html tests/
```
