FROM tiangolo/uvicorn-gunicorn:python3.11-slim

#
WORKDIR .

#
COPY . .

#
RUN pip install --no-cache-dir --upgrade -r requirements.txt

#
ENTRYPOINT ["bash","./entrypoint.sh"]
