import locale
import requests

locale.setlocale(locale.LC_ALL, 'pt_BR')
class CurrencyConversorService:
    """
    Serviço de conversão de moedas utilizando a API AwesomeAPI.
    """

    def __init__(self) -> None:
        """
        Inicializa uma nova instância do serviço de conversão de moedas.
        """
        pass

    def converter(self, coin_origin: str, coin_target: str):
        """
         Converte o valor de uma moeda de origem para uma moeda de destino.

         :param coin_origin: Código da moeda de origem (por exemplo, 'USD' para Dólar Americano).
         :type coin_origin: str

         :param coin_target: Código da moeda de destino (por exemplo, 'BRL' para Real Brasileiro).
         :type coin_target: str

         :return:
            O valor convertido da moeda de origem para a moeda de destino. 
            Se a moeda não for encontrada, retorna a mensagem de erro da API.
         :rtype: str
        """

        response = requests.get(
            url=f'https://economia.awesomeapi.com.br/json/last/{coin_origin}-{coin_target}'
        )

        if response.status_code == 404:
            return response.json().get('message')
        valor = response.json().get(f'{coin_origin}{coin_target}').get('bid')
        valor = locale.currency(
            float(valor),
            grouping=True
            )
        return valor

    