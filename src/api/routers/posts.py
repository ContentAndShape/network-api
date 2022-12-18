from src.__init__ import app


async def create_post(author_id: str):
    ...


async def get_post(id: str):
    ...


async def get_post_comments(id: str):
    ...


async def update_post(id: str, **kwargs):
    ...


async def delete_post(id: str):
    ...
