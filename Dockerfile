FROM python:3.10.1
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt  \
    && wget https://github.com/allure-framework/allurectl/releases/latest/download/allurectl_linux_386 -O ./allurectl \
    && chmod +x ./allurectl \
    && if grep -wq "playwright" requirements.txt; then playwright install; fi
