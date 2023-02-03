import re
from re import Match

from starlette import status

from src.core.base.services import BaseService
from src.app.user.repositories import UserRepository
from src.core.redis_adapter import RedisAdapter
from src.core.utils import generate_one_time_code
from src.core.config import config
from src.core.template_engine import TemplateEngine
from src.core.smtp_class import SMTPController
from src.core.schemas import ErrorSchema


class UserService(BaseService):
    repository: UserRepository = UserRepository()
    redis: RedisAdapter = RedisAdapter(
        host=config.REDIS_HOST,
        port=config.REDIS_PORT,
    )
    template = TemplateEngine()
    smtp_controller = SMTPController()

    def validate_email(self, email: str) -> None | Match:
        return re.match(
            r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',
            email,
        )

    def send_html_to_email(
            self,
            email: str,
            path_html: str,
            **kwargs,
    ) -> None:
        html = self.template.render_html(path_html, **kwargs)

        self.smtp_controller.send_email(email, html)

    async def create_save_send_code(self, email: str) -> None | ErrorSchema:
        """
        This method generate code.
        Save code in redis.
        Render and sending html with code to email.
        """
        
        if not self.validate_email(email):
            return ErrorSchema(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid email.",
            )

        one_time_code = generate_one_time_code()

        self.redis.set_value(
            key=email,
            data=one_time_code,
            ex=config.DATA_RETENTION_TIME,
        )

        self.send_html_to_email(
            email=email,
            path_html='gmail_one_time_code.html',
            one_time_code=one_time_code,
        )
