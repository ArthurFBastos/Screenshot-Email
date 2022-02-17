import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email.mime.base import MIMEBase
from email import encoders

def send_email():
    #Setar o Servidor SMTP
    host = "smtp.gmail.com"
    port = "587"
    login = "emailenvio@email.com"
    senha = "senha"
    destino = "emaildestino@email.com"

    #Dando start no servidor 
    server = smtplib.SMTP(host,port)
    server.ehlo()
    server.starttls()
    server.login(login,senha)


    #Construir o email tipo MIME
    corpo = """
    <b> Primeira linha </b>
    <p> Segunda linha de texto</p>
    """


    #Montando e-mail 
    email_msg = MIMEMultipart()
    email_msg['From'] = login
    email_msg['To'] = destino
    email_msg['Subject'] = "Assunto do email"
    email_msg.attach(MIMEText(corpo,'html'))

    #Abrimos o arquivo em modo leitura e binary 
    cam_arquivo = "Caminho do arquivo com separação de 2 barras \\"
    attchment = open(cam_arquivo,'rb')

    #Lemos o arquivo no modo binario e jogamos codificado em base 64 (que é o que o e-mail precisa )
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attchment.read())
    encoders.encode_base64(att)

    #Adicionado o cabeçalho no tipo anexo de email 
    att.add_header('Content-Disposition', f'attachment; filename=Nome_do_arquivo.tipo')
    #Fechamos o arquivo 
    attchment.close()

    #Colocamos o anexo no corpo do e-mail 
    email_msg.attach(att)

    #Enviar o email tipo MIME no servidor SMTP 
    server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())
    server.quit()