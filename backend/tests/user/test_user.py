import pytest
from httpx import AsyncClient
from starlette.status import HTTP_201_CREATED, HTTP_200_OK

from tests.factories.user import UserFactory


class TestUserRoutes:

    user = UserFactory().create_user()

    @pytest.mark.asyncio
    async def test_user_creates(self, client: AsyncClient) -> None:

        res = await client.post(
            "/api/user/",
            json={
                "email": self.user.email,
                "password": self.user.password,
                "name": self.user.name,
            },
        )

        data = res.json()

        assert res.status_code == HTTP_201_CREATED
        assert data["email"] == self.user.email
        assert data["name"] == self.user.name

    @pytest.mark.asyncio
    async def test_user_get(self, client: AsyncClient) -> None:
        res = await client.get(f"/api/user/?email={self.user.email}")

        assert res.status_code == HTTP_200_OK
