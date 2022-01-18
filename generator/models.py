import uuid
from django.db import models


def generate_uuid():
    """Generate a UUID4 hex.

    Returns:
        str: The generated UUID hex.
    """
    return uuid.uuid4().hex


class Vault(models.Model):
    uuid = models.CharField(max_length=40, default=generate_uuid, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.uuid
