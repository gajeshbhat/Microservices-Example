import yagmail
from nameko.rpc import rpc


class Mail(object):
    name = "mail"

    @rpc
    def send(self, to, subject, result):
        try:
            yag_obj = yagmail.SMTP(
                user={'MAILTRAP_USERNAME': ''},
                soft_email_validation=False,
                password='MAILTRAP_PASSWORD',
                host='smtp.mailtrap.io',
                smtp_starttls=True,
                smtp_ssl=False
            )
            yag_obj.send(to=to, subject=subject,
                         contents=str('This works! The result is ') + str(result))
            print("Email sent successfully!")
            return "Result sent in the mail. Check your inbox!"
        except:
            print("Sending email failed!")
            return "Failed! Check logs!"
