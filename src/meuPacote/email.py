import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
# https://br.ajuda.yahoo.com/kb/Gerar-e-gerenciar-senhas-de-aplicativos-de-terceiros-sln15241.html

def enviar_email(usuario, senha, destinatario, assunto, mensagem):
     """
     Funcao para enviar email pelo servidor do Yahoo

     Essa função pega os dados e conecta no servidor Yahoo para enviar o email

     Parameters:
     usuario (str): usuário Yahoo válido
     senha (str): senha do usuário Yahoo válida
     destinatario (str): destinatario do email
     assunto (str): titulo do email
     mensagem (str): mensagem do email

     Returns:
     None: Sem retorno
     """
     # Configurações do servidor SMTP do Yahoo
     servidor_smtp = 'smtp.mail.yahoo.com'
     porta = 587
     # Criar objeto do tipo MIMEMultipart
     msg = MIMEMultipart()
     msg['From'] = usuario
     msg['To'] = destinatario
     msg['Subject'] = assunto
     # Adicionar mensagem ao corpo do e-mail
     msg.attach(MIMEText(mensagem, 'plain'))
     # Iniciar conexão com o servidor SMTP do Yahoo
     servidor = smtplib.SMTP(servidor_smtp, porta)
     servidor.starttls()
     # Autenticar no servidor SMTP
     servidor.login(usuario, senha)
     # Enviar e-mail
     servidor.sendmail(usuario, destinatario, msg.as_string())
     # Fechar conexão com o servidor SMTP
     servidor.quit()



def enviar_email(usuario, senha, destinatario, assunto, mensagem):
    # Cria a mensagem de e-mail
    msg = MIMEMultipart()
    msg['From'] = usuario
    msg['To'] = destinatario
    msg['Subject'] = assunto

    # Anexa o corpo da mensagem
    msg.attach(MIMEText(mensagem, 'plain'))

    # Conecta ao servidor SMTP e envia o e-mail
    try:
        with smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465) as server:
            server.login(usuario, senha)
            server.sendmail(usuario, destinatario, msg.as_string())
        print('Email enviado!')
    except Exception as e:
        print(f'Erro ao enviar email: {e}')