from src.__init__ import app


async def create_comment(author_id: str):
    ...


async def get_comment(id: str):
    ...


async def get_commented_post(id: str):
    ...


async def get_comment_author(id: str):
    ...


async def update_comment(id: str, **kwargs):
    ...


async def delete_comment(id: str):
    ...
