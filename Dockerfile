FROM python:3.12

EXPOSE 8000
ENV PIP_NO_CACHE_DIR=1
ENV PYTHONPATH=/var/app/src

WORKDIR /var/app
COPY . /var/app

RUN pip install uv
RUN uv pip install --system -r requirements.txt

RUN apt install -y

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]

