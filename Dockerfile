FROM python:3.10-slim

RUN pip install -U deepeval

COPY . .

ENTRYPOINT ["deepeval"]
