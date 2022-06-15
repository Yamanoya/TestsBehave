FROM debian:buster-slim

WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y \
    python3-pip 

RUN pip3 install -r requirements.txt


CMD ["behave", "--tags=@flag_off_decline", "-f", "allure_behave.formatter:AllureFormatter", "-o", "allure_results", "./features"]
