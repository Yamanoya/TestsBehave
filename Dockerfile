FROM debian:buster-slim

WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y && apt-get upgrade -y \
    python3-pip -y \
	python-pip
RUN pip install -r requirements.txt




CMD ["behave", "--tags=@null_byte", "-f", "allure_behave.formatter:AllureFormatter", "-o", "allure_results", "./features"]
