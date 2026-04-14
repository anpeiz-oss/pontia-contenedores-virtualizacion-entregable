FROM python:3.14-alpine

WORKDIR /

COPY tasks_management_app/ tasks_management_app/

RUN pip install --no-cache-dir -r ./tasks_management_app/requirements.txt

EXPOSE 8080

CMD ["fastapi", "run", "tasks_management_app/main.py", "--host", "0.0.0.0", "--port", "8080"]



