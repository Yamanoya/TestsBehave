FROM python:3.10-slim-buster

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

CMD ["behave", "--tags=@add_agent,@flag_on_with_accept_cancel,@flag_on_with_decline_cancel,@flag_off_decline,@null_byte,@act_all_decline_accept,@act_all_decline_cancel,@act_all_cancel,@torg_all_decline_accept,@torg_all_decline_cancel,@torg_all_cancel,@YKD_ALL_ACCEPT_DECLINE,@YKD_ALL_CANCEL_DECLINE,@YKD_ALL_DECLINE,@YKD_DECLINE,@YPD_ALL_ACCEPT_DECLINE,@YPD_ALL_CANCEL_DECLINE,@YPD_ALL_DECLINE,@YPD_DECLINE,@delete_agent", "-f", "allure_behave.formatter:AllureFormatter", "-o", "allure_results", "./features"]