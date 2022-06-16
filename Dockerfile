FROM joyzoursky/python-chromedriver:3.9-selenium

WORKDIR /app
COPY . .

RUN pip3 install -r requirements.txt

CMD ["behave", "--tags=@flag_off_decline", "-f", "allure_behave.formatter:AllureFormatter", "-o", "allure_results", "./features"]
