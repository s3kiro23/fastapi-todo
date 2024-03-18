from passlib.hash import bcrypt
from uuid import uuid4
from tortoise.models import Model
from tortoise.fields import CharField, UUIDField, BooleanField, DatetimeField, IntField


class User(Model):
    id = IntField(pk=True)
    username = CharField(max_length=100, null=False)
    email = CharField(max_length=100, null=True, unique=True)
    password_hash = CharField(max_length=128, null=True)
    is_active = BooleanField(null=False, default=True)
    is_verified = BooleanField(null=False, default=False)
    verified_at = DatetimeField(null=True)
    disabled = BooleanField(null=False, default=False)
    created_at = DatetimeField(null=True, auto_now_add=True)
    updated_at = DatetimeField(null=True, auto_now=True)

    @classmethod
    async def get_user_by_email(cls, email: str):
        return cls.get(email=email)

    @classmethod
    async def get_user_by_username(cls, username: str):
        return cls.get(username=username)

    @classmethod
    async def get_user_by_id(cls, id: str):
        return cls.get(id=id)

    @classmethod
    async def verify_password(self, password: str):
        return bcrypt.verify(password, self.password_hash)

    class Meta:
        table = "users"  # table name on the db
        ordering = ["-created_at"]  # order by c_at DESC
