import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC75eb7e35ec088bfba8bccd5f4dbbebf6"
# Your Auth Token from twilio.com/console
auth_token  = "d1431895062c880e81fccc3efc013611"
client = Client(account_sid, auth_token)

# Passo a passo de solução

# Abrir os 6 arquivos excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

# Para cada arquivo:
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
# Verificar se algum valor na coluna Vendas daquele arquivo é maior do que 55.000
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5511987716014",
            from_="+14023472705",
            body=f'No mês de {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)

# Se for maior do que 55.000 -> Envia um SMS com o nome, o mês e as vendas do vendedor

# Caso nao seja maior do que 55.000 nao fazer nada

