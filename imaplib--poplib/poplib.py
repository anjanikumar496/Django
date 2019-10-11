
import poplib

class Insta_Gram_Mail_OTP:
    def Mail_OTP(usrname,password):
        final_otp = ""
        user = usrname
        Mailbox = poplib.POP3_SSL('pop.rediffmail.com')
        Mailbox.user(user)
        Mailbox.pass_(password)
        numMessages = len(Mailbox.list()[1])
        for i in range(numMessages):
            for msg in Mailbox.retr(i+1)[1]:
                if '<font size=3D"6' in str(msg):
                    final_otp = (str(str(msg).split('<font size=3D"6">')[1]).split('</font>')[0])
        print (final_otp)
        return final_otp
