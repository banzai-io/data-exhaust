import uuid as uuid
from django.db import models


class DataSignal(models.Model):
    EMAIL_SIGNAL = 'Email'
    PHONE_SIGNAL = 'Phone'

    SIGNAL_TYPES = (
        (EMAIL_SIGNAL, EMAIL_SIGNAL),
        (PHONE_SIGNAL, PHONE_SIGNAL)
    )

    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    signal_type = models.CharField(
        choices=SIGNAL_TYPES,
        max_length=6,
        db_index=True
    )
    identifier = models.CharField(
        max_length=255,
        db_index=True
    )
    signal_value = models.CharField(
        default='catch_all',
        max_length=120,
        db_index=True
    )
    valid = models.BooleanField(
        db_index=True,
        default=False
    )
    added = models.DateTimeField(auto_now_add=True)

    # Event related fields
    signal_meta = models.JSONField(
        verbose_name='Signal Meta Data',
        help_text='Contains event and contact data e.g. seniority, job options',
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        return f'{self.signal_type} signal - {self.valid}'
