FROM docker.io/node:22-alpine as frontend

COPY ./frontend /frontend

WORKDIR /frontend/duckygotchi

RUN \
    npm install &&\
    npm run build

FROM tiangolo/uvicorn-gunicorn:python3.11-slim

#
WORKDIR .

#
COPY . .

COPY --from=frontend ./frontend/duckygotchi/dist   ./static

RUN ls -la ./static

#
RUN pip install --no-cache-dir --upgrade -r requirements.txt

#
ENTRYPOINT ["bash","./entrypoint.sh"]
