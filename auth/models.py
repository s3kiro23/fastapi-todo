from uuid import uuid4
from tortoise.models import Model
from tortoise.fields import CharField, UUIDField, DatetimeField


class Token(Model):
    id = UUIDField(pk=True, default=uuid4)
    token = CharField(max_length=300, null=False)
    created_at = DatetimeField(null=True, auto_now_add=True)

    class Meta:
        table = "tokens"  # table name on the db
        ordering = ["-created_at"]  # order by c_at DESC
