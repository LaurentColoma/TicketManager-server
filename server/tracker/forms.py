"""TODO"""

from django.forms import (
    ModelForm,
    Textarea,
    HiddenInput,
    NumberInput,
    Select,
    SelectMultiple,
    TextInput,
    RadioSelect,
)

from .models import (
    Ticket,
    TicketComment,
    Task,
    Anomaly,
    Proposal,
    Process,
)


class TicketMainForm(ModelForm):

    class Meta:  # pylint: disable=too-few-public-methods
        """TicketMainForm Meta class"""
        model = Ticket

        fields = (
            "label",
            "impact",
            "priority",
            "time_sensitiveness",
            "application",
            "version_affected_set",
            "module_set",
            "description",
        )

        widgets = {
            "label": TextInput(attrs={
                "class": "form-control",
            }),
            "impact":  Select(attrs={  # RadioSelect
                "class": "form-control select2",
            }),
            "priority":  Select(attrs={  # RadioSelect
                "class": "form-control select2",
            }),
            "time_sensitiveness":  Select(attrs={  # RadioSelect
                "class": "form-control select2",
            }),
            "application": Select(attrs={
                "class": "form-control select2",
            }),
            "version_affected_set": SelectMultiple(attrs={
                "class": "form-control select2",
            }),
            "module_set": SelectMultiple(attrs={
                "class": "form-control select2",
            }),
            "description": Textarea(attrs={
                "class": "form-control mce",
            }),
        }


class TaskMainForm(TicketMainForm):

    class Meta(TicketMainForm.Meta):  # pylint: disable=too-few-public-methods
        """TaskMainForm Meta class"""
        model = Task


class ProposalMainForm(TicketMainForm):

    class Meta(TicketMainForm.Meta):  # pylint: disable=too-few-public-methods
        """ProposalMainForm Meta class"""
        model = Proposal


class ProcessMainForm(TicketMainForm):

    class Meta(TicketMainForm.Meta):  # pylint: disable=too-few-public-methods
        """ProcessMainForm Meta class"""
        model = Process


class AnomalyMainForm(TicketMainForm):

    class Meta(TicketMainForm.Meta):  # pylint: disable=too-few-public-methods
        """AnomalyMainForm Meta class"""
        model = Anomaly

        fields = TicketMainForm.Meta.fields[0:4] + (
            "type",
            "reproducibility",
        ) + TicketMainForm.Meta.fields[4:]

        widgets = TicketMainForm.Meta.widgets
        widgets.update({
            "type":  Select(attrs={  # RadioSelect
                "class": "form-control select2",
            }),
            "reproducibility":  Select(attrs={  # RadioSelect
                "class": "form-control select2",
            }),
        })


class TicketRACIForm(ModelForm):

    class Meta:  # pylint: disable=too-few-public-methods
        """TicketRACIForm Meta class"""

        model = Ticket

        fields = (
            "responsible",  # Ticket
            "accountable",  # Ticket
            "consulted_set",  # Ticket
            "informed_set",  # Ticket
        )

        widgets = {
            "responsible":  RadioSelect(attrs={
                "class": "form-control select2",
            }),
            "accountable":  RadioSelect(attrs={
                "class": "form-control select2",
            }),
            "consulted_set": SelectMultiple(attrs={
                "class": "form-control select2",
            }),
            "informed_set": SelectMultiple(attrs={
                "class": "form-control select2",
            }),
        }


class TicketDuplicationForm(ModelForm):

    class Meta:  # pylint: disable=too-few-public-methods
        """TicketDuplicationForm Meta class"""

        model = Ticket

        fields = (
            "original",
        )

        widgets = {
            "original":  Select(attrs={
                "class": "form-control select2",
            }),
        }


class TicketTargetForm(ModelForm):

    class Meta:  # pylint: disable=too-few-public-methods
        """TicketTargetForm Meta class"""
        model = Ticket

        fields = (
            "version_targeted",
        )

        widgets = {
            "version_targeted":  RadioSelect(attrs={
                "class": "form-control select2",
            }),
        }


class TicketReleaseForm(ModelForm):

    class Meta:  # pylint: disable=too-few-public-methods
        """TicketReleaseForm Meta class"""


        model = Ticket

        fields = (
            "version_released",
        )

        widgets = {
            "version_released":  RadioSelect(attrs={
                "class": "form-control select2",
            }),
        }


class TicketCommentForm(ModelForm):

    class Meta:  # pylint: disable=too-few-public-methods
        """TicketCommentForm Meta class"""

        model = TicketComment

        fields = (
            "ticket",
            "comment",
        )

        widgets = {
            "ticket": HiddenInput(),
            "comment": Textarea(attrs={
                "class": "form-control mce",
            }),
        }


# class Task(Ticket):
#     """Ticket that is a job to do"""
#
#     assigned_to = ForeignKey(
#         verbose_name=_("assigned_to"),
#         related_name="%(app_label)s_%(class)s_set",
#         help_text=_("User assigned to the task of resolving this ticket"),
#         to=getattr(settings, "AUTH_USER_MODEL", "auth.User"),
#         null=True,
#         blank=True,
#     )
#
#     commit_number = CharField(
#         verbose_name=_("Commit number"),
#         help_text=_("For traceability purposes (can be revert)"),
#         max_length=64,
#         null=False,
#         blank=False
#     )
#
#     #
#     # Meta class
#     #
#
#     class Meta:
#         verbose_name = _("task")
#         verbose_name_plural = _("tasks")
#
#
# class Process(Task):
#
#     #
#     # Meta class
#     #
#
#     class Meta:
#         verbose_name = _("process")
#         verbose_name_plural = _("processes")
#
#
# class Proposal(Task):
#
#     #
#     # Meta class
#     #
#
#     class Meta:
#         verbose_name = _("proposal")
#         verbose_name_plural = _("proposals")
#
#
# class Anomaly(Task):
#
#     step_to_reproduce = TextField(
#         verbose_name=_("Step to reproduce"),
#         help_text=_("Explain how the anomaly occurs"),
#         blank=False,
#         null=False,
#     )
#
#     type = ForeignKey(
#         verbose_name=_("Type"),
#         related_name="%(class)s_set",
#         help_text=_("Type of anomalie"),
#         to=AnomalyType,
#         null=False,
#         blank=False,
#     )
#
#     reproducibility = ForeignKey(
#         verbose_name=_("Reproducibility"),
#         related_name="%(class)s_set",
#         help_text=_("Is this anomaly occurs sometimes or always"),
#         to=Reproducibility,
#         null=True,
#         blank=True,
#     )
#
#     #
#     # Meta class
#     #
#
#     class Meta:
#         verbose_name = _("anomaly")
#         verbose_name_plural = _("anomalies")
