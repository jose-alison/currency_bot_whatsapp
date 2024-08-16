from dotenv import load_dotenv
import os
import requests

load_dotenv(override=True)

class CallmeBot:
    def __init__(self) -> None:
        self.__base_url = os.getenv("CALLME_URL")
        self.__phone = os.getenv("CALLME_PHONE")
        self.__api_key = os.getenv("CALLME_API_KEY")

    def send_message(self, message):
        response = requests.get(
            url=f"{self.__base_url}?phone={self.__phone}&text={message.replace(' ', '+')}&apikey={self.__api_key}"
        )
        if response.status_code == 200:
            print('Mensagem enviada')
        return response.text