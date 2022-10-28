FROM python:3.10.1
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt  \
    && if grep -wq "playwright" requirements.txt; then playwright install; fi \
    && touch .env  \
    && chmod -R 777 .env \
