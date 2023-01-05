import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from starlette.status import HTTP_201_CREATED


class TestUserRoutes:
    @pytest.mark.asyncio
    async def test_user_creates(self, app: FastAPI, client: AsyncClient) -> None:
        res = await client.post(
            "/api/user/",
            json={"email": "kan1i@gmail.com", "password": "123456", "name": "name"},
        )

        assert res.status_code == HTTP_201_CREATED
