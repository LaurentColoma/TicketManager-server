"""TODO"""

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models import (
    BooleanField,
    CharField,
    TextField,
    DecimalField,
    DateField,
    ManyToManyField,
    OneToOneField,
    ForeignKey,
    ImageField,
    PositiveSmallIntegerField,
    PositiveIntegerField,
    Model,
    AutoField,
    Max,
    DateTimeField,
)
from polymorphic.models import PolymorphicModel

from django.utils.translation import ugettext_lazy as _

class Objective(Model):

    label = CharField("label", max_length=256)

    class Meta:
        """Application Meta class"""

        verbose_name = _("objective")
        verbose_name_plural = _("objectives")

        def __str__(self):
            return self.label

class Roadmap(Model):

    label = CharField("label", max_length=64)

    class Meta:  # pylint: disable=too-few-public-methods
        """Application Meta class"""

        verbose_name = _("roadmap")
        verbose_name_plural = _("roadmaps")

    def __str__(self):
        return self.label


class Sprint(Model):

    label = CharField("label", max_length=64)
    roadmap = ForeignKey(
        verbose_name=_("roadmap"),
        related_name="sprint",
        help_text=_("Related Roadmap"),
        to=Roadmap,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
    )
    objective = ForeignKey(
        verbose_name=_("objective"),
        related_name="objective",
        help_text=_("Related Objective"),
        to=Objective,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING
    )

    class Meta:  # pylint: disable=too-few-public-methods
        """Application Meta class"""

        verbose_name = _("sprint")
        verbose_name_plural = _("sprints")

    def __str__(self):
        return self.label


class Application(Model):

    label = CharField("label", max_length=64)
    #
    # Meta class
    #

    class Meta:  # pylint: disable=too-few-public-methods
        """Application Meta class"""

        verbose_name = _("application")
        verbose_name_plural = _("applications")

    def __str__(self):
        return self.label


class Version(Model):

    label = CharField("label", max_length=64)

    application = ForeignKey(
        verbose_name=_("Application"),
        related_name="version_set",
        help_text=_("Related application"),
        to=Application,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
    )

    #
    # Meta class
    #

    class Meta:  # pylint: disable=too-few-public-methods
        """Version Meta class"""

        verbose_name = _("version")
        verbose_name_plural = _("versions")

    def __str__(self):
        return self.label


class Module(Model):

    label = CharField("label", max_length=64)

    application = ForeignKey(
        verbose_name=_("Application"),
        related_name="module_set",
        help_text=_("Related application"),
        to=Application,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
    )

    #
    # Meta class
    #

    class Meta:  # pylint: disable=too-few-public-methods
        """Module Meta class"""

        verbose_name = _("module")
        verbose_name_plural = _("modules")

    def __str__(self):
        return self.label


class Impact(Model):

    #
    # Meta class
    #

    label = CharField("label", max_length=64)

    class Meta:  # pylint: disable=too-few-public-methods
        """Impact Meta class"""

        verbose_name = _("impact choice")
        verbose_name_plural = _("impact choices")

    def __str__(self):
        return self.label


class Priority(Model):

    label = CharField("label", max_length=64)

    color = CharField(
        verbose_name=_("Color"),
        help_text=_("Color associated with this priority"),
        max_length=10,
        null=False,
        blank=False
    )

    #
    # Meta class
    #

    class Meta:  # pylint: disable=too-few-public-methods
        """Priority Meta class"""
        verbose_name = _("priority choice")
        verbose_name_plural = _("priorities choices")

    def __str__(self):
        return self.label


class TimeSensitiveness(Model):

    label = CharField("label", max_length=64)

    color = CharField(
        verbose_name=_("Color"),
        help_text=_("Color associated with this time sensitiveness"),
        max_length=10,
        null=False,
        blank=False
    )

    #
    # Meta class
    #

    class Meta:  # pylint: disable=too-few-public-methods
        """TimeSensitiveness Meta class"""

        verbose_name = _("time sensitiveness choice")
        verbose_name_plural = _("time sensitiveness choices")

    def __str__(self):
        return self.label


class Reproducibility(Model):

    #
    # Meta class
    #

    label = CharField("label", max_length=64)

    class Meta:  # pylint: disable=too-few-public-methods
        """Reproducibility Meta class"""

        verbose_name = _("reproducibility choice")
        verbose_name_plural = _("reproducibility choices")

    def __str__(self):
        return self.label


class Status(Model):

    #
    # Meta Class
    #

    label = CharField("label", max_length=64)

    class Meta:  # pylint: disable=too-few-public-methods
        """Reproducibility Meta class"""

        verbose_name = _("status")
        verbose_name_plural = _("statuses")

    def __str__(self):
        return self.label


class Ticket(PolymorphicModel, Model):
    """Ticket base

    > The ticket reporter is the user that have created the ticket

    """

    label = CharField("Ticket", max_length=64)
    # PENDING = 0
    # DONE = 1
    # STATUS_CHOICES = (
    #     (PENDING, 'Pending'),
    #     (DONE, 'Done'),
    # )

    number = PositiveSmallIntegerField(
        verbose_name=_("Number"),
        help_text=_("Ticket's comment number"),
        blank=False,
        null=False,
    )

    description = TextField(
        verbose_name=_("Description"),
        help_text=_("Do yourself a favour : be as exhaustive as you can !"),
        blank=False,
        null=False,
    )

    responsible = ForeignKey(
        verbose_name=_("Person in charge of this ticket"),
        related_name="%(app_label)s_%(class)s_responsible_set",
        help_text=_("MOE leader on this ticket, R in RACI matrix"),
        to=User,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
    )

    accountable = ForeignKey(
        verbose_name=_("Person accountable for this ticket"),
        related_name="%(app_label)s_%(class)s_accountable_set",
        help_text=_("MOA leader on this ticket, A in RACI matrix"),
        to=User,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
    )

    consulted_set = ManyToManyField(
        verbose_name=_("Person that must be consulted for this ticket"),
        related_name="%(app_label)s_%(class)s_consulted_set",
        help_text=_("Person with useful knowledge, C in RACI matrix"),
        to=User,
        null=True,
        blank=True,
    )

    informed_set = ManyToManyField(
        verbose_name=_("Person that must be informed about this ticket"),
        related_name="%(app_label)s_%(class)s_informed_set",
        help_text=_("Person concerned about this ticket, I in RACI matrix"),
        to=User,
        null=True,
        blank=True,
    )

    status = ForeignKey(
        verbose_name=_("Status"),
        related_name="status_of_ticket",
        help_text=_("state of the ticket"),
        to=Status,
        null=False,
        blank=False,
        on_delete=models.DO_NOTHING,
    )

    open = BooleanField(
        verbose_name=_("Open"),
        help_text=_("is the ticket close or open"),
        default=True
    )

    impact = ForeignKey(
        verbose_name=_("Impact"),
        related_name="ticket_set",
        help_text=_("Is resolving this ticket will make a big difference ?"),
        to=Impact,
        null=False,
        blank=False,
        on_delete=models.DO_NOTHING,
    )

    priority = ForeignKey(
        verbose_name=_("Priority"),
        related_name="ticket_set",
        help_text=_("Is resolving this ticket is game changing ?"),
        to=Priority,
        null=False,
        blank=False,
        on_delete=models.DO_NOTHING,
    )

    time_sensitiveness = ForeignKey(
        verbose_name=_("Time sensitiveness"),
        related_name="ticket_set",
        help_text=_("Is resolving this ticket is a matter of emergency or a long "),
        to=TimeSensitiveness,
        null=False,
        blank=False,
        on_delete=models.DO_NOTHING,
    )

    original = ForeignKey(
        verbose_name=_("Original ticket"),
        related_name="duplicate_set",
        help_text=_("Mark this ticket as a duplicate of:"),
        to="self",
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
    )

    application = ForeignKey(
        verbose_name=_("Application"),
        related_name="ticket_set",
        help_text=_("Related application"),
        to=Application,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
    )

    version_affected_set = ManyToManyField(
        verbose_name=_("Affected versions"),
        related_name="ticket_affected_set",
        help_text=_("Application versions that are affected by the ticket"),
        to=Version,
        null=True,
        blank=True,
    )

    version_targeted = ForeignKey(
        verbose_name=_("Version"),
        related_name="tickets_targeted_set",
        help_text=_("Aimed version for the release of this ticket"),
        to=Version,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
    )

    version_released = ForeignKey(
        verbose_name=_("Version"),
        related_name="ticket_released_set",
        help_text=_("The ticket have been released  in version:"),
        to=Version,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
    )

    module_set = ManyToManyField(
        verbose_name=_("Module"),
        related_name="ticket_set",
        help_text=_("Related module"),
        to=Module,
        null=True,
        blank=True,
    )

    sprint = ForeignKey(
        verbose_name=_("Sprint"),
        related_name="ticket_set",
        help_text=_("Related Sprint"),
        to=Sprint,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
    )

    #depends_on = ManyToManyField(
    #   verbose_name=_("Depends_On"),
    #   related_name="ticket_set",
    #   help_text=_("ticket related to this ticket"),
    #   to=Ticket,
    #   null=True,
    #   blank=True
    # )

    def compute_name(self):
        return "{self.number}_{self.label}".format(self=self)

    def get_application_display(self):
        """Allow to display application"""

        return self.application.label

    def get_version_affected_set_display(self):
        """Allow to display modules"""

        return ", ".join([o.label for o in self.version_affected_set.all()])

    def get_application_and_versions_display(self):
        """Allow to display application and versions"""

        return "{} ({})".format(self.get_application_display(), self.get_version_affected_set_display())

    def get_module_set_display(self):
        """Allow to display modules"""

        return ", ".join([o.label for o in self.module_set.all()])

    def get_impact_display(self):
        """Allow to display impact"""

        return self.impact.labelImpact

    def get_priority_display(self):
        """Allow to display priority"""

        return self.priority.labelPriority

    def get_time_sensitiveness_display(self):
        """Allow to display priority"""

        return self.time_sensitiveness.labelTimeSensitiveness

    def get_type_display(self):
        """Allow to display type"""

        return _("Ticket")

    def get_reproducibility_display(self):
        """Allow to display type"""

        return _("N/A")

    def get_version_targeted_display(self):
        """Allow to display targeted version or '--'"""
        return self.version_targeted or "--"

    def get_version_released_display(self):
        """Allow to display released version or '--'"""
        return self.version_targeted or "--"

    # @property
    # def editable(self):
    #     return self.status in ("draft", "open", "on_hold", "planed", "in_progress", "ready", "tested")

    #
    # Meta class
    #

    class Meta:  # pylint: disable=too-few-public-methods
        """Ticket Meta class"""

        verbose_name = _("ticket")
        verbose_name_plural = _("tickets")
    def __str__(self):
        return self.label


class TicketComment(Model):

    labelTicketComment = CharField("TicketComment", max_length=64)

    ticket = ForeignKey(
        verbose_name=_("Ticket"),
        related_name="comment_set",
        help_text=_("Ticket related to this comment"),
        to=Ticket,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
    )

    author = ForeignKey(
        verbose_name=_("Author"),
        related_name="tracker_ticket_comment_set",
        help_text=_("Author of the comment"),
        to=getattr(settings, "AUTH_USER_MODEL", "auth.User"),
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
    )

    number = PositiveSmallIntegerField(
        verbose_name=_("Number"),
        help_text=_("Ticket's comment number"),
        blank=False,
        null=False,
    )

    comment = TextField(
        verbose_name=_("Comment"),
        help_text=_("Type your comment here: "),
        blank=False,
        null=False,
    )

    def _hook_pre_save(self, *args, **kwargs):
        if not self.number:
            self.number = (TicketComment.objects.filter(ticket=self.ticket).aggregate(Max("number"))["number__max"] or 0) + 1
        return super()._hook_pre_save(*args, **kwargs)

    LABEL_FORMAT = "Ticket #{self.ticket.number}: Comment #{self.number}"

    #
    # Meta class
    #

    class Meta:  # pylint: disable=too-few-public-methods
        """TicketComment Meta class"""

        verbose_name = _("ticket comment")
        verbose_name_plural = _("ticket comments")

    def __str__(self):
        return self.labelTicketComment


class Task(Ticket):
    """Ticket that is a job to do"""

    assigned_to = ForeignKey(
        verbose_name=_("assigned_to"),
        related_name="tracker_task_set",
        help_text=_("User assigned to the task of resolving this ticket"),
        to=getattr(settings, "AUTH_USER_MODEL", "auth.User"),
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
    )

    commit_number = CharField(
        verbose_name=_("Commit number"),
        help_text=_("For traceability purposes (can be revert)"),
        max_length=64,
        null=False,
        blank=False
    )

    def get_type_display(self):
        """Allow to display type"""

        return _("Task")

    #
    # Meta class
    #

    class Meta:  # pylint: disable=too-few-public-methods
        """Task Meta class"""

        verbose_name = _("task")
        verbose_name_plural = _("tasks")


class Process(Task):

    def get_type_display(self):
        """Allow to display type"""

        return _("Process")

    #
    # Meta class
    #

    class Meta:  # pylint: disable=too-few-public-methods
        """Process Meta class"""

        verbose_name = _("process")
        verbose_name_plural = _("processes")


class Proposal(Task):

    def get_type_display(self):
        """Allow to display type"""

        return _("Proposal")

    #
    # Meta class
    #

    class Meta:  # pylint: disable=too-few-public-methods
        """Proposal Meta class"""

        verbose_name = _("proposal")
        verbose_name_plural = _("proposals")


class AnomalyCategorie(Model):

    #
    # Meta class
    #

    label = CharField("label", max_length=64)

    class Meta:  # pylint: disable=too-few-public-methods
        """AnomalyType Meta class"""

        verbose_name = _("anomaly type")
        verbose_name_plural = _("anomaly types")

    def __str__(self):
        return self.label


class Anomaly(Task):

    step_to_reproduce = TextField(
        verbose_name=_("Step to reproduce"),
        help_text=_("Explain how the anomaly occurs"),
        blank=False,
        null=False,
    )

    type = ForeignKey(
        verbose_name=_("Type"),
        related_name="anomaly_set",
        help_text=_("Type of anomalie"),
        to=AnomalyCategorie,
        null=False,
        blank=False,
        on_delete=models.DO_NOTHING,
    )

    reproducibility = ForeignKey(
        verbose_name=_("Reproducibility"),
        related_name="anomaly_set",
        help_text=_("Is this anomaly occurs sometimes or always"),
        to=Reproducibility,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
    )

    def get_type_display(self):
        """Allow to display type"""

        return self.type.label

    def get_reproducibility_display(self):
        """Allow to display reproducibility"""

        return self.reproducibility.label

    #
    # Meta class
    #

    class Meta:  # pylint: disable=too-few-public-methods
        """Anomaly Meta class"""

        verbose_name = _("anomaly")
        verbose_name_plural = _("anomalies")


class Comment(Model):

    content = CharField(
        "content",
        max_length=140,
    )
    date = DateTimeField()
    # user = ForeignKey(
    #     verbose_name=_("user"),
    #     related_name="comment_set",
    #     help_text=_("Related User"),
    #     to=User,
    #     null=False,
    #     blank=False,
    # )
    ticket = ForeignKey(
        verbose_name=_("ticket"),
        related_name="set_comment",
        help_text=_("Related Ticket"),
        to=Ticket,
        null=False,
        blank=False,
        on_delete=models.DO_NOTHING,
    )

    class Meta:  # pylint: disable=too-few-public-methods
        """Application Meta class"""

        verbose_name = _("comment")
        verbose_name_plural = _("comments")

    def __str__(self):
        return self.content
