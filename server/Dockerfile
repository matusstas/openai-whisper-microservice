FROM python:3.9

WORKDIR /app/

RUN apt-get update && apt-get install -y ffmpeg

COPY ./requirements.txt ./requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY ./requirements-api.txt ./requirements-api.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements-api.txt

COPY ./src /app/src

EXPOSE 80

CMD [ "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
