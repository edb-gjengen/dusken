# Note: This is autogenerated with python manage.py inspectdb and the field types are a bit weird
from django.db import models
from django.utils.translation import ugettext_lazy as _


class DeliveryReport(models.Model):
    connection_name = 'tekstmelding'

    timestamp = models.DateTimeField()
    msgid = models.TextField(blank=True, null=True)
    ext_id = models.TextField(db_column='extID', blank=True, null=True)
    msisdn = models.FloatField(blank=True, null=True)
    errorcode = models.IntegerField(blank=True, null=True)
    errormessage = models.TextField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    statustext = models.TextField(blank=True, null=True)
    operatorerrorcode = models.TextField(blank=True, null=True)
    registered = models.TextField(blank=True, null=True)
    sent = models.TextField(blank=True, null=True)
    delivered = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{}: {}'.format(self.__class__.__name__, self.pk)

    class Meta:
        managed = False
        db_table = 'dlr'


class TekstmeldingEvent(models.Model):
    connection_name = 'tekstmelding'

    NOTIFY_COULD_NOT_CHARGE = 'notify_could_not_charge'
    NOTIFY_PAYMENT_OPTIONS_NEW = 'notify_payment_options_new'
    NOTIFY_PAYMENT_OPTIONS_RENEWAL = 'notify_payment_options_renewal'
    NOTIFY_VALID_MEMBERSHIP = 'notify_valid_membership'

    RENEW_MEMBERSHIP = 'renew_membership'
    RENEW_MEMBERSHIP_DELIVERED = 'renew_membership_delivered'

    NEW_MEMBERSHIP_DELIVERED = 'new_membership_delivered'
    NEW_MEMBERSHIP = 'new_membership'
    NEW_MEMBERSHIP_CARD = 'new_membership_card'

    ACTION_CHOICES = (
        (NOTIFY_VALID_MEMBERSHIP, _('Notify valid membership')),
        (NOTIFY_PAYMENT_OPTIONS_RENEWAL, _('Notify payment options renewal')),
        (NOTIFY_PAYMENT_OPTIONS_NEW, _('Notify payment options new')),
        (NOTIFY_COULD_NOT_CHARGE, _('Notify could not charge')),
        (RENEW_MEMBERSHIP, _('Renew membership')),
        (RENEW_MEMBERSHIP_DELIVERED, _('Renew membership delivered')),
        (NEW_MEMBERSHIP, _('New membership')),
        (NEW_MEMBERSHIP_DELIVERED, _('New membership delivered')),
        (NEW_MEMBERSHIP_CARD, _('New membership card')),
    )

    timestamp = models.DateTimeField()
    incoming = models.ForeignKey('tekstmelding.IncomingMessage', models.SET_NULL, blank=True, null=True)
    outgoing = models.ForeignKey(
        'tekstmelding.OutgoingMessage', models.SET_NULL, blank=True, null=True, related_name='events')
    dlr = models.ForeignKey('tekstmelding.DeliveryReport', models.SET_NULL, blank=True, null=True)
    action = models.TextField(choices=ACTION_CHOICES, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)
    activation_code = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{}: {}'.format(self.__class__.__name__, self.pk)

    class Meta:
        managed = False
        db_table = 'event'


class IncomingMessage(models.Model):
    connection_name = 'tekstmelding'

    timestamp = models.DateTimeField()
    msgid = models.TextField(blank=True, null=True)
    msisdn = models.FloatField(blank=True, null=True)
    msg = models.TextField(blank=True, null=True)
    mms = models.IntegerField(blank=True, null=True)
    mmsdata = models.TextField(blank=True, null=True)
    shortcode = models.IntegerField(blank=True, null=True)
    mcc = models.IntegerField(blank=True, null=True)
    mnc = models.IntegerField(blank=True, null=True)
    pricegroup = models.IntegerField(blank=True, null=True)
    keyword = models.TextField(blank=True, null=True)
    keywordid = models.IntegerField(blank=True, null=True)
    errorcode = models.IntegerField(blank=True, null=True)
    errormessage = models.TextField(blank=True, null=True)
    registered = models.TextField(blank=True, null=True)
    ip = models.TextField(blank=True, null=True)

    def __str__(self):
        return '{}: {}'.format(self.__class__.__name__, self.pk)

    class Meta:
        managed = False
        db_table = 'incoming'


class OutgoingMessage(models.Model):
    connection_name = 'tekstmelding'

    timestamp = models.DateTimeField()
    sender = models.TextField()
    destination = models.TextField()
    pricegroup = models.IntegerField()
    content_type_id = models.IntegerField(db_column='contentTypeID')
    content_header = models.TextField(db_column='contentHeader', blank=True, null=True)
    content = models.TextField()
    dlr_url = models.TextField(db_column='dlrUrl', blank=True, null=True)
    age_limit = models.IntegerField(db_column='ageLimit')
    ext_id = models.TextField(db_column='extID', blank=True, null=True)
    send_date = models.TextField(db_column='sendDate', blank=True, null=True)
    ref_id = models.TextField(db_column='refID', blank=True, null=True)
    priority = models.IntegerField()
    gw_id = models.IntegerField(db_column='gwID')
    pid = models.IntegerField()
    dcs = models.IntegerField()

    def __str__(self):
        return '{}: {}'.format(self.__class__.__name__, self.pk)

    class Meta:
        managed = False
        db_table = 'outgoing'


class OutgoingResponse(models.Model):
    connection_name = 'tekstmelding'

    timestamp = models.DateTimeField()
    message_id = models.TextField(db_column='MessageID')
    success = models.IntegerField(db_column='Success')
    error_number = models.IntegerField(db_column='ErrorNumber')
    error_message = models.TextField(db_column='ErrorMessage', blank=True, null=True)

    def __str__(self):
        return '{}: {}'.format(self.__class__.__name__, self.pk)

    class Meta:
        managed = False
        db_table = 'outgoing_response'
