FROM arm64v8/python:3.11.2-slim-bullseye
LABEL maintainer="Maksim Surmach"

# Create directory for the app user
RUN mkdir -p /home/app

# Create the app user
RUN groupadd app && useradd -g app app


ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME


COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . $APP_HOME

RUN chown -R app:app $APP_HOME

USER app

CMD ["uvicorn", "main:app", "--host=0.0.0.0","--port=8000","--reload"]