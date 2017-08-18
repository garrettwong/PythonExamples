## requires disable account key: https://login.yahoo.com/account/security?scrumb=ruOkEoe6mQ2

# Import smtplib for the actual sending function
import smtplib
from email.mime.text import MIMEText
import sys

textfile = './file-watcher-folder/workfile'
smtpServer = 'localhost'
#smtpServer = 'mailrelay'


class EmailManager:
    def send(self):
        # Open a plain text file for reading.  For this example, assume that
        # the text file contains only ASCII characters.
        fp = open(textfile, 'rb')
        # Create a text/plain message
        msg = MIMEText(fp.read())
        fp.close()

        me = ''
        you = ''

        # me == the sender's email address
        # you == the recipient's email address
        msg['Subject'] = 'The contents of %s' % textfile
        msg['From'] = me
        msg['To'] = you

        # Send the message via our own SMTP server, but don't include the
        # envelope header.
        s = smtplib.SMTP(smtpServer)
        s.sendmail(me, [you], msg.as_string())
        s.quit()

    def sendYahooMail(self):
        # fun-fact: from is a keyword in python, you can't use it as variable, did abyone check if this code even works?
        fromMy = ''
        to = ''
        username = ''
        password = ''

        subj = 'TheSubject'
        date = '2/1/2010'
        message_text = 'Hello Or any thing you want to send'
        msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % (
            fromMy, to, subj, date, message_text)

        username = str(username)
        password = str(password)

        try:
            server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
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

    # em.send()
    em.sendYahooMail()
