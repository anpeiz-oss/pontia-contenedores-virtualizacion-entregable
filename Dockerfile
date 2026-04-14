FROM python:3.14-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /

COPY tasks_management_app/ tasks_management_app/

RUN pip install --no-cache-dir -r ./tasks_management_app/requirements.txt

EXPOSE 8080

CMD ["fastapi", "run", "tasks_management_app/main.py", "--port", "8080"]



