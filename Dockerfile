FROM python:latest

LABEL Maintainer="alvesgf16"

WORKDIR /app

COPY ./sample ./

CMD ["python", "./games.py"]
