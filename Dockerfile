FROM python:3.8-slim


WORKDIR /Users/jmb/Documents/GitHub/mvp_demo

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/KlangVerso/mvp_demo.git .

run pip3 install -r requirements.txt

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "home.py", "--server.port=8501"]