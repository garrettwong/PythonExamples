## requires disable account key: https://login.yahoo.com/account/security?scrumb=ruOkEoe6mQ2

# Import smtplib for the actual sending function
import smtplib
from email.mime.text import MIMEText
import sys

import Configs

textfile = './file-watcher-folder/workfile'


class EmailManager:
    def send(self, to):
        # Open a plain text file for reading.  For this example, assume that
        # the text file contains only ASCII characters.
        fp = open(textfile, 'rb')
        # Create a text/plain message
        msg = MIMEText(fp.read())
        fp.close()

        me = Configs.config['me']
        you = 'gwong005@gmail.com'

        # me == the sender's email address
        # you == the recipient's email address
        msg['Subject'] = 'The contents of %s' % textfile
        msg['From'] = Configs.config['me']
        msg['To'] = to

        # Send the message via our own SMTP server, but don't include the
        # envelope header.
        s = smtplib.SMTP(Configs.config['smtpServer'])
        s.sendmail(Configs.config['me'], [you], msg.as_string())
        s.quit()

    def sendYahooMail(self, to):
        # fun-fact: from is a keyword in python, you can't use it as variable, did abyone check if this code even works?
        fromMy = Configs.yahooConfig['me']

        subj = 'TheSubject'
        date = '2/1/2010'
        message_text = 'Hello Or any thing you want to send'
        msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % (
            fromMy, to, subj, date, message_text)

        username = str(Configs.yahooConfig['me'])
        password = str(Configs.yahooConfig['pw'])

        try:
            server = smtplib.SMTP(Configs.yahooConfig['smtpServer'], 587)
            print(server.ehlo())
            server.starttls()

            server.login(username, password)
            print('logged in')
            server.sendmail(fromMy, to, msg)
            server.quit()
            print 'ok the email has sent '
            
        except:
            print 'can\'t send the Email', sys.exc_info()[0]
            raise
            


if __name__ == "__main__":
    em = EmailManager()

    em.send('gwong005@gmail.com')
    em.sendYahooMail('gwong005@gmail.com')
