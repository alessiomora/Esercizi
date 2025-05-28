FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
 
COPY ./main.py /app/main.py
COPY ./requirements_server.txt /app/requirements.txt
 
WORKDIR /app

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt
 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]