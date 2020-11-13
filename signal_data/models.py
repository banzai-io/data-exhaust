from django.db import models


class DataSignal(models.Model):
    EMAIL_SIGNAL = 'Email'
    PHONE_SIGNAL = 'Phone'

    SIGNAL_TYPES = (
        (EMAIL_SIGNAL, EMAIL_SIGNAL),
        (PHONE_SIGNAL, PHONE_SIGNAL)
    )

    # Email related signals
    BOUNCE = 'bounced'
    OPENED = 'opened'
    CLICKED = 'clicked'
    # Phone related signals
    NA = 'no-answer'
    BAD_CONTACT = 'bad-contact'
    DNC = 'do-not-contact'
    ANSWERED = 'answered-call-back'
    MORE_INFO = 'send-more-info'
    REGISTERED = 'register'
    ON_DEMAND = 'on-demand'
    UNREGISTERED = 'un-registered'
    UNSUBSCRIBE = 'unsubscribe'
    COMPLAINT = 'complaint'

    SIGNAL_OPTIONS = (
        (BOUNCE, BOUNCE),
        (OPENED, OPENED),
        (CLICKED, CLICKED),
        (NA, NA),
        (BAD_CONTACT, BAD_CONTACT),
        (DNC, DNC),
        (ANSWERED, ANSWERED),
        (MORE_INFO, MORE_INFO),
        (REGISTERED, REGISTERED),
        (ON_DEMAND, ON_DEMAND),
        (UNREGISTERED, UNREGISTERED),
        (UNSUBSCRIBE, UNSUBSCRIBE),
        (COMPLAINT, COMPLAINT),
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
        choices=SIGNAL_OPTIONS,
        max_length=80,
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
