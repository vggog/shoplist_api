from typing import Any

import redis


class RedisAdapter:
    def __init__(
        self,
        host: str = 'localhost',
        port: int = 6379,
        charset: int = 'utf-8',
        decode_response: bool = True,
    ):
        self.redis_host = host
        self.redis_port = port
        self.redis_charset = charset
        self.redis_decode_response = decode_response

    def _get_redis_client(self):
        return redis.StrictRedis(
            host=self.redis_host,
            port=self.redis_port,
            charset=self.redis_charset,
            decode_responses=self.redis_decode_response,
        )

    def set_value(self, key: str, data: Any) -> None:
        with self._get_redis_client() as client:
            client.set(name=key, value=data)

    def get_value(self, key: str) -> Any:
        with self._get_redis_client() as client:
            return client.get(name=key)
