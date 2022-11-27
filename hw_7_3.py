import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Email_Client():

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def send_message(self, send_to, subject, message):
        '''отправка сообщений'''
        msg = MIMEMultipart()
        msg['From'] = self.login
        recipients = ', '.join(send_to)
        msg['To'] = recipients
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        ms = smtplib.SMTP('smtp.gmail.com', 587)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()

        ms.login(self.login, self.password)
        ms.sendmail(self.login, recipients, msg.as_string())
        ms.quit()
        return True

    def recieve_message(self, index=-1, folder="INBOX"):
        '''получение сообщений. По умолчанию возвращает последнее во входящих, можно в параметрах выбрать индекс
        необходимого письма и папку'''
        mail_connect = imaplib.IMAP4_SSL("imap.gmail.com")
        mail_connect.login(self.login, self.password)
        mail_connect.list()
        mail_connect.select(folder)

        result, data = mail_connect.uid('search', None, 'ALL')
        latest_email_uid = data[0].split()[index]
        result, data = mail_connect.uid('fetch', latest_email_uid, '(RFC822)')
        msg = email.message_from_bytes(data[0][1])
        mail_connect.logout()
        return msg

'''========================== для проверки ==========================='''

if __name__ == '__main__':

    TEST_RECIPIENTS = ['vasya@email.com', 'petya@email.com']
    TEST_LOGIN = 'login@gmail.com'
    TEST_PASSWORD = 'qwerty'

    my = Email_Client(TEST_LOGIN, TEST_PASSWORD)
    my.send_message(TEST_RECIPIENTS, 'test_subject', 'test_body')
    print(my.recieve_message()['From'])