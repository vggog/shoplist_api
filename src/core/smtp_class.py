import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from src.core.config import config


class SMTPController:
    login = config.SMTP_LOGIN
    password = config.SMTP_PASSWORD
    host = config.SMTP_HOST
    port = config.SMTP_PORT

    def _create_html_message(self, to_email: str, html: str) -> MIMEMultipart:
        message = MIMEMultipart()
        message["Subject"] = "Одноразовый код Shoplist"
        message["From"] = self.login
        message["To"] = to_email

        attaching_message = MIMEText(html, "html")
        message.attach(attaching_message)

        return message

    def send_email(self, to_email: str, sending_message: str) -> None:
        smtp_obj = smtplib.SMTP(self.host, self.port)
        smtp_obj.starttls()
        smtp_obj.login(self.login, self.password)

        message = self._create_html_message(to_email, sending_message)

        smtp_obj.sendmail(self.login, to_email, message.as_string())
        smtp_obj.quit()
