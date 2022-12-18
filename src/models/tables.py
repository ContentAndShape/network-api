from sqlalchemy.orm import declarative_base, declared_attr
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    TIMESTAMP,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID


Base = declarative_base()


class CreatedUpdatedMixin:
    created_at = Column(TIMESTAMP(timezone=True), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), nullable=False)


class AuthorRelationMixin:
    @declared_attr
    def author_id(cls):
        return Column(Integer, ForeignKey(
            "users.id", ondelete="SET NULL"), nullable=False)


class User(Base, CreatedUpdatedMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    password = Column(String(100), nullable=False)


class Post(Base, CreatedUpdatedMixin, AuthorRelationMixin):
    __tablename__ = "posts"

    id = Column(UUID, primary_key=True)
    name = Column(String(50), nullable=False)
    content = Column(Text(1000), nullable=False)


class Comment(Base, CreatedUpdatedMixin, AuthorRelationMixin):
    __tablename__ = "comments"

    id = Column(UUID, primary_key=True)
    post_id = Column(UUID, ForeignKey(
        "posts.id", ondelete="CASCADE"
    ), nullable=False)