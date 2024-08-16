
# Bot conversor de moedas

O objetivo do projeto é consumir uma API que fornece dados sobre conversão de moedas.



## Clonando o projeto

Clone o projeto

```bash
  git clone https://github.com/jose-alison/currency_bot_whatsapp/
```

Entre no diretório do projeto

```bash
  cd currency_bot_whatsapp
```


## Instalação

Instale e inicie a venv

```python
  python3 -m venv venv
  source ~/venv/bin/activate
```

Instale o requirements do projeto:

```python
  pip install -r requirements.txt
```
    
## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env

`CALLME_URL`

`CALLME_PHONE`

`CALLME_API_KEY`

O site da CallMeBot possui instruções de como obter os dados acima. [Acesse a documentação aqui](https://www.callmebot.com/es/blog/api-gratis-mensajes-whatsapp/)


## Executando o projeto localmente

Execute o arquivo main para executar o script

```python 
  python3 main.py
```