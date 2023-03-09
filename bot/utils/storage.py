from typing import Dict, Any, Optional, cast

from aiogram import Bot
from aiogram.fsm.state import State
from aiogram.fsm.storage.base import BaseStorage, StorageKey, StateType
from aiogram.fsm.storage.redis import KeyBuilder, DefaultKeyBuilder
from django.core.cache import cache
from redis.typing import ExpiryT


class DjangoRedisStorage(BaseStorage):
    def __init__(
            self,
            key_builder: Optional[KeyBuilder] = None,
            state_ttl: Optional[ExpiryT] = None,
            data_ttl: Optional[ExpiryT] = None,
    ):
        if key_builder is None:
            key_builder = DefaultKeyBuilder()
        self.key_builder = key_builder
        self.state_ttl = state_ttl
        self.data_ttl = data_ttl

    async def set_state(self, bot: Bot, key: StorageKey, state: StateType = None) -> None:
        redis_key = self.key_builder.build(key, "state")
        if state is None:
            await cache.adelete(redis_key)
        else:
            await cache.aset(
                redis_key,
                cast(str, state.state if isinstance(state, State) else state),
                self.state_ttl,
            )

    async def get_state(self, bot: Bot, key: StorageKey) -> Optional[str]:
        redis_key = self.key_builder.build(key, "state")
        value = await cache.aget(redis_key)
        if isinstance(value, bytes):
            return value.decode("utf-8")
        return cast(Optional[str], value)

    async def set_data(self, bot: Bot, key: StorageKey, data: Dict[str, Any]) -> None:
        redis_key = self.key_builder.build(key, "data")
        if not data:
            await cache.adelete(redis_key)
            return
        await cache.aset(
            redis_key,
            bot.session.json_dumps(data),
            self.data_ttl,
        )

    async def get_data(self, bot: Bot, key: StorageKey) -> Dict[str, Any]:
        redis_key = self.key_builder.build(key, "data")
        value = await cache.aget(redis_key)
        if value is None:
            return {}
        if isinstance(value, bytes):
            value = value.decode("utf-8")
        return cast(Dict[str, Any], bot.session.json_loads(value))

    async def close(self) -> None:
        await cache.aclose()
