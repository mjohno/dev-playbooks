FROM ubuntu:xenial

RUN apt-get update && apt-get install -y \
    gcc \
    libssl-dev \
    libffi-dev \
    python \
    python-apt\
    python-pip

WORKDIR /apps

RUN pip install ansible ansible-lint ansible-review

COPY . .

RUN ansible-playbook -i tests/inventory tests/main.yml --syntax-check
RUN ansible-playbook -i tests/inventory tests/main.yml --check
RUN ansible-lint .
RUN ansible-playbook -i tests/inventory tests/main.yml
RUN ansible-playbook -i tests/inventory tests/main.yml
