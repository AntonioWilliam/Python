

#Importando biblioteca date para saber o ano atual com o modulo datetime
from datetime import date
ano = int(input('Digite o ano para pesquisa. Caso queira saber se o ano atual é bissexto digite 0 : '))
if ano == 0:
    #Usando o datetime para extrair o ano atual do sistema == data.hoje.ano
    ano= date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano% 400 ==0:
    print(f'O ano {ano} é Bissexto')
else:
    print(f'O ano {ano} não é Bissexto')
    
'''"ano % 4 == 0" diz que todos os anos divisíveis por 4 são bissextos (2008, 2012, 2016, 2020 etc)
"ano % 100 != 0" diz que todos os anos divisíveis por 100 NÃO são bissextos, criando "falhas" na sequência (retira-se os anos 1700, 1800, 1900, 2000 etc)
"ano % 400 == 0" preenche as falhas com somente os números divisíveis por 400 (800, 1200, 1600, 2000 etc)
Então "ano % 4 == 0 and ano % 100 != 0" é um critério, e "ano % 400 == 0" é outro.'''