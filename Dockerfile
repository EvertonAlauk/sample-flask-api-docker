FROM python:3

RUN apt-get update && apt-get install -y --no-install-recommends \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        git \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY . /app

RUN /usr/local/bin/python -m pip install --upgrade pip && pip install -r ./app/requirements.txt

WORKDIR /app

EXPOSE 5178

CMD python app.py
