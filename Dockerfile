FROM python:3.10.1
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt  \
    && playwright install \
    && touch .env  \
    && chmod -R 777 .env \
    && pip install python-dotenv[cli]
