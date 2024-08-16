from clients.currency_service import CurrencyConversorService

client = CurrencyConversorService()

btc_brl_value = client.converter('BTC', 'BRL')

print(btc_brl_value)