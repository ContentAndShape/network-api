from src.__init__ import app


async def create_user(id: str):
    ...


async def get_user(id: str):
    ...


async def get_user_posts(id: str):
    ...


async def get_user_comments(id: str):
    ...


async def update_user(id: str, **kwargs):
    ...


async def delete_user(id: str):
    ...
