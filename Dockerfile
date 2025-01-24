FROM tiangolo/uvicorn-gunicorn:python3.11-slim

#
WORKDIR .

#
COPY . .

#
RUN pip install --no-cache-dir --upgrade -r requirements.txt

#

#
CMD ["uvicorn", "backend/main:app", "--host", "0.0.0.0", "--port", "8080"]
