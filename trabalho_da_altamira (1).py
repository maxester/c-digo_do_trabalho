# -*- coding: utf-8 -*-
"""trabalho da Altamira

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oKBouYznAmXcvTzKoetRPkl_23byNiJN
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def Enviar_Email():
  try:
    remetente = "testesterdasilva@gmail.com"
    senha = "heoc wpvc oyua lisk"
    destinatário = "esters777nascimento@gmail.com"
    assunto = "Importando Bibliotecas - Ester da Silva Nascimento"

    mensagem = MIMEMultipart()
    mensagem["From"] = remetente
    mensagem["To"] = destinatário
    mensagem["Subject"] = assunto

    corpo = """\
    <html>
      <head>
        <tittle><h3>Olá, mundo! Eu sou o corpo do E-mail ʕ⁠·⁠ᴥ⁠·⁠ʔ<br></h3></tittle>
        <style>
          th {
            color: green;
          }

          table {
            margin-bottom: 50px;
            text-align: center;
          }
        </style>
      </head>
      <body>
        <header>
          <p>
            A função desse programa visa encaminhar um e-mail através do <i>Simple Mail Transfer Protocol</i> (SMTP), que é um protocolo utilizado para o envio e recebimentos de e-mails pela internet.<br>
          </p>

          <p>
            O motivo do envio desse e-mail é para comprovar que atendi à proposta do trabalho. A seguir, haverá uma tabela com informações sobre as bibliotecas utilizadas no código e uma imagem adicional!
          </p>
        </header>
        <table border = "1">
            <tr>
              <th width = "30%">Nome da Biblioteca</th>
              <th>Funcionalidade da Biblioteca</th>
            </tr>
            <tr>
              <td><b>smtplib</b></td>
              <td>
                Fornece uma interface para enviar E-mails usando o protocolo SMTP.<br>
                Por meio dela, é possível conectar-se a um servidor SMTP, como gmail, hotmail e outlook e realizar a autenticação com o servidor através de credenciais, como nome de usuário e senha
              </td>
            </tr>
            <tr>
              <td><b>email.mime.multipart</b></td>
              <td>
                Permite estruturar um email que pode conter várias partes, como texto simples, HTML e anexos.
              </td>
            </tr>
            <tr>
              <td><b>email.mime.text</b></td>
              <td>
                Usado especificamente para criar partes de texto simples ou em HTML ("plain" ou "html") para anexar em um e-mail com várias partes.
              </td>
            </tr>
        </table>
        <img src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTd94YZPknKqn6TqQ6W08RlnckVEea4y53phfK4cXECewn4FJiqrKLX7TBw&s=10"/>
      </body>
    </html>
    """
    mensagem.attach(MIMEText(corpo, 'html'))

    servidor = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    servidor.login(remetente, senha)
    servidor.sendmail(remetente, destinatário, mensagem.as_string())
    print("E-mail enviado com sucesso!")

  except smtplib.SMTPConnectError as ce:
    print(f"Falha na Conexão com o Servidor: {ce}")

  except smtplib.SMTPAuthenticationError as ae:
    print(f"Falha de Autenticação: {ae}")

  except smtplib.SMTPException as e:
    print(f"Erro ao Enviar E-mail: {e}")

  finally:
    servidor.quit()

Enviar_Email()