import os
from pathlib import Path
BASE_DIR = str(Path(os.path.dirname(__file__)).parent)
import pandas as pd

from meuPacote.atletas import getAge
from meuPacote.atletas import getCountry
from meuPacote.atletas import getMedal
from meuPacote.email import enviar_email

def main(): 
    file = BASE_DIR + '/data/nomesAtletas.xlsx'

    df = pd.read_excel(file)
    df['nome'].values

    age = []
    Name = df['nome'].values
    for nome in Name:
        nome = getAge(nome)
        age += [nome]
        print(nome)

    df['age'] = age 

    country = []
    Name = df['nome'].values
    for nome in Name:
        nome = getCountry(nome)
        country += [nome]
        print(nome)

    df['country'] = country

    medal = []
    Name = df['nome'].values
    for nome in Name:
        nome = getMedal(nome)
        medal += [nome]
        print(nome)

    df['medal'] = medal

    df.to_excel(BASE_DIR + '/data/listaFinal.xlsx')

    ####################
    df.loc[df["medal"]=="Gold",:]
    
    df.loc[df["country"]=="United States",:]

    df["country"]

    #################### 


    usuario = os.environ.get("YAHOO_USER")
    senha = os.environ.get("YAHOO_PASSWORD")
    
    destinatario = "laerte.takeuti@yahoo.com"
    assunto = "Prova AP2"
    mensagem = """
i. 
-Alex Walter Diggelmann.
-Alexandra Simons de Ridder.
-Katherine Jessie Jean "Kate" Allen (-Diechtler).
ii.
-Os EUA ganharam 13 medalhas.
iii.
-Oskar Thiede.
-Idade:69.
iv.
Nessa amostra 38 paises ganharam.
#Isabella Aguiar
"""
    enviar_email(usuario, senha, destinatario, assunto, mensagem)

if __name__ == '__main__':
    main()
