from src.core.base.repositories import BaseRepository


class BaseService:
    _repository = BaseRepository()

    async def validate_values(
        self,
        **kwargs,
    ) -> tuple:
        errors = {}
        for key, value in kwargs.items():
            validate_method = 'validate_{}'.format(key)
            if not hasattr(self, validate_method):
                continue

            success, error = getattr(self, validate_method)(value)
            if success:
                continue

            errors[key] = error
        attrs = kwargs
        return attrs, errors

    async def create(self, create_schema):
        data_for_create = create_schema.dict()
        attrs, errors = await self.validate_values(**data_for_create)

        if errors:
            return None, errors

        created_object = self._repository.create(**attrs)
        return created_object, None
