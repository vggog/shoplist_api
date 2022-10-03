from fastapi import FastAPI


API_V1_PREFIX = '/api/v1/'


class AppFactory:
    @classmethod
    def create_app(cls) -> FastAPI:
        """Returns the FastAPI app with instantiated DB."""
        app = FastAPI()
        cls._register_views(app)

        return app

    @classmethod
    def _register_views(cls, app: FastAPI):
        from src.app.routes import shopping_list_route

        app.include_router(
            shopping_list_route,
            prefix=''.join([API_V1_PREFIX, 'shopping_list']),
        )
