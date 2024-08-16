from clients.currency_service import CurrencyConversorService
from clients.callme_service import CallmeBot

currency_client = CurrencyConversorService()
callme_client = CallmeBot()

btc_brl_value = currency_client.converter('BTC', 'BRL')

send = callme_client.send_message(
    message=f"O valor do Bitcoin está *{btc_brl_value}*"
)
