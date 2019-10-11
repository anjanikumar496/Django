import imaplib
import email
class FaceBook_Code:
    def Codess(email_user,email_pass,domain):
        mail = imaplib.IMAP4_SSL("imap."+domain,993)
        mail.login(email_user, email_pass)
        mail.select()
        type, data = mail.search(None, 'ALL')
        mail_ids = data[-1]
        id_list = mail_ids.split()
        for num in data[0].split():
            typ, data = mail.fetch(num, '(RFC822)' )
            raw_email = data[0][1]
            raw_email_string = raw_email.decode('utf-8')
            email_message = email.message_from_string(raw_email_string)
        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1].decode('utf-8'))
                email_subject = msg['subject'][:5]
                print(email_subject)
                return email_subject