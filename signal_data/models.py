from djongo import models
from django import forms


class Item(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            'name',
        )


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
    NA = 'No Answer'
    BAD_CONTACT = 'Bad Contact'
    DNC = 'Do Not Contact'
    ANSWERED = 'Answered, Call Back'
    MORE_INFO = 'Send More Info'
    REGISTERED = 'Register'
    ON_DEMAND = 'On Demand'
    UNREGISTERED = 'Un-registered'

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
    )

    _id = models.ObjectIdField()
    signal_type = models.CharField(choices=SIGNAL_TYPES, max_length=6)
    hashed_identifier = models.CharField(max_length=255)
    signal_value = models.CharField(choices=SIGNAL_OPTIONS, max_length=80)
    valid = models.BooleanField()
    added = models.DateTimeField(auto_now_add=True)

    # Event related fields
    event_name = models.CharField(max_length=255, help_text='Name of event where this signal originated')
    seniority = models.ArrayField(
        model_container=Item,
        model_form_class=ItemForm,
    )
    job_functions = models.ArrayField(
        model_container=Item,
        model_form_class=ItemForm,
    )

    objects = models.DjongoManager()