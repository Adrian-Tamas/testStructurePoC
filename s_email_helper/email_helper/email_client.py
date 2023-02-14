import logging
import smtplib

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

logger = logging.getLogger('email_client')


class EmailClient:

    def __init__(self, email_address, email_password, smtp_server, port):
        self.email_address = email_address
        self.email_password = email_password
        self.smtp_server = smtp_server
        self.port = port

    def send_email(self, to, subject, message, file_path, attachment_name):
        try:
            # create email
            msg = MIMEMultipart()
            msg['Subject'] = subject
            msg['From'] = self.email_address
            msg['To'] = to
            html_content = MIMEText(message, "html")
            msg.attach(html_content)

            with open(file_path, "rb") as attachment:
                # The content type "application/octet-stream" means that a MIME attachment is a binary file
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())

            # Encode to base64
            encoders.encode_base64(part)

            # Add header
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {attachment_name}",
            )

            # Add attachment to your message and convert it to string
            msg.attach(part)

            # send email
            with smtplib.SMTP(self.smtp_server) as smtp:
                if self.email_password:
                    smtp.login(self.email_address, self.email_password)
                smtp.sendmail(
                    self.email_address, to, msg.as_string()
                )
            return True
        except Exception as e:
            print("=============")
            print("Problem during send email" + str(e))
            print("=============")
        return False
