FROM debian:buster-slim

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

CMD ["behave", "--tags=@null_byte", "-f", "allure_behave.formatter:AllureFormatter", "-o", "allure_results", "./features"]
