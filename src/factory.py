from fastapi import FastAPI
from src.app.user.routes import router as user_routes


class AppFactory:

    @classmethod
    def create_app(cls) -> FastAPI:
        app = FastAPI()
        cls._append_routes(app)
        return app

    @staticmethod
    def _append_routes(app: FastAPI):
        app.include_router(
            user_routes,
            prefix='/user'
        )
