from django.db.models import Max
from django.db.models.signals import pre_save
from django.dispatch import receiver

from tracker.models import Ticket, Anomaly, Process, Proposal, Task


@receiver(pre_save, sender=Ticket, dispatch_uid="ticket_generate_number")
@receiver(pre_save, sender=Task, dispatch_uid="task_generate_number")
@receiver(pre_save, sender=Anomaly, dispatch_uid="anomaly_generate_number")
@receiver(pre_save, sender=Process, dispatch_uid="process_generate_number")
@receiver(pre_save, sender=Proposal, dispatch_uid="proposal_generate_number")
def ticket_generate_number(sender, instance, raw, using, update_fields, **kwargs):
    """
    Allow to generate the Ticket's number
    """
    if instance.pk:
        return
    # else we are creating
    if not instance.number:
        instance.number = (Ticket.objects.all().aggregate(Max("number"))["number__max"] or 0) + 1