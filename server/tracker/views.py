"""TODO"""
from datatableview.views import XEditableDatatableView
from django.contrib.auth.models import User, Group

from django.views.generic import View, DetailView, CreateView
from django.http import JsonResponse

from django.urls import reverse
from datatableview.helpers import make_xeditable

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from tracker.serializers import TicketSerializer, UserSerializer, GroupSerializer, ImpactSerializer, PrioritySerializer, \
    TimeSensitivenessSerializer, ApplicationSerializer, VersionSerializer, ModuleSerializer, StatusSerializer

from tracker.serializers import SprintSerializer, RoadmapSerializer, CommentSerializer, ObjectiveSerializer

from .models import (
    Ticket,
    Task,
    Proposal,
    Process,
    Anomaly,
    Application,
    Version,
    Module,
    Impact,
    Priority,
    TimeSensitiveness,
    Reproducibility,
    AnomalyCategorie,
    Status, Sprint, Roadmap, Comment, Objective)

from .forms import (
    TicketMainForm,
    TaskMainForm,
    ProposalMainForm,
    ProcessMainForm,
    AnomalyMainForm,
    TicketRACIForm,
)


from django.utils.translation import ugettext as _


FORMS = {
    "task": TaskMainForm,
    "proposal": ProposalMainForm,
    "process": ProcessMainForm,
    "anomaly": AnomalyMainForm,
}

MODELS = {
    "task": Task,
    "proposal": Proposal,
    "process": Process,
    "anomaly": Anomaly,
}


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ObjectiveViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = ObjectiveSerializer

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class ImpactViewSet(viewsets.ModelViewSet):
    queryset = Impact.objects.all()
    serializer_class = ImpactSerializer


class PriorityViewSet(viewsets.ModelViewSet):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer


class TimeSensitivenessViewSet(viewsets.ModelViewSet):
    queryset = TimeSensitiveness.objects.all()
    serializer_class = TimeSensitivenessSerializer


class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class VersionViewSet(viewsets.ModelViewSet):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class SprintViewSet(viewsets.ModelViewSet):
    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer


class RoadmapViewSet(viewsets.ModelViewSet):
    queryset = Roadmap.objects.all()
    serializer_class = RoadmapSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class TicketsListView(XEditableDatatableView):

    model = Ticket

    template_name = "tracker/list.html"

    datatable_options = {
        "columns": [
            "id",
            (_("application"), "get_application_and_versions_display"),
            (_("modules"), "get_modules_display"),
            (_("label"), "label"),
            (_("impact"), "impact"),
            (_("priority"), "priority"),
            (_("type"), "type"),
            (_("reproducibility"), "reproducibility"),
            (_("time_sensitiveness"), "time_sensitiveness"),
            (_("status"), "status__label"),
        ],
        "structure_template": "datatableview/bootstrap_structure.html",
        "hidden_columns": ["id"],
        "search_fields": ["label", "application__label", "modules__label", "description"],
    }

    def get_column_impact_data(self, instance, *args, **kwargs):  # pylint: disable=unused-argument, no-self-use
        """Allow to change impact from the table"""

        return make_xeditable(
            instance=instance,
            default_value=instance.impact.pk,
            field_data="impact",
            type="select",
            source=reverse("kaoka_tracker:choices_impact"),
            url=self.request.path,
            )

    def get_column_priority_data(self, instance, *args, **kwargs):  # pylint: disable=unused-argument, no-self-use
        """Allow to change priority from the table"""

        return make_xeditable(
            instance=instance,
            default_value=instance.priority.pk,
            field_data="priority",
            type="select",
            source=reverse("kaoka_tracker:choices_priority"),
            url=self.request.path,
            )

    def get_column_type_data(self, instance, *args, **kwargs):  # pylint: disable=unused-argument, no-self-use
        """Allow to change priority from the table"""

        if instance.polymorphic_ctype.name != "anomaly":
            return instance.get_type_display()

        return make_xeditable(
            instance=instance,
            default_value=instance.type.pk,
            field_data="type",
            type="select",
            source=reverse("kaoka_tracker:choices_anomaly_type"),
            url=self.request.path,
            )

    def get_column_reproducibility_data(self, instance, *args, **kwargs):  # pylint: disable=unused-argument, no-self-use
        """Allow to change priority from the table"""

        if instance.polymorphic_ctype.name != "anomaly":
            return instance.get_reproducibility_display()

        return make_xeditable(
            instance=instance,
            default_value=instance.reproducibility.pk,
            field_data="reproducibility",
            type="select",
            source=reverse("kaoka_tracker:choices_reproducibility"),
            url=self.request.path,
            )

    def get_column_time_sensitiveness_data(self, instance, *args, **kwargs):  # pylint: disable=unused-argument, no-self-use
        """Allow to change priority from the table"""

        return make_xeditable(
            instance=instance,
            default_value=instance.time_sensitiveness.pk,
            field_data="time_sensitiveness",
            type="select",
            source=reverse("kaoka_tracker:choices_time_sensitiveness"),
            url=self.request.path,
            )

    def get_xeditable_form_kwargs(self):
        kwargs = super().get_xeditable_form_kwargs()

        instance = kwargs["model"].objects.get(pk=kwargs["data"]["pk"][0])
        kwargs["model"] = instance.polymorphic_ctype.model_class()

        return kwargs

    def update_object(self, form, obj):
        """ Saves the new value to the target object. """
        field_name = form.cleaned_data["name"]
        if field_name not in ("impact", "priority", "type", "reproducibility", "time_sensitiveness"):
            return JsonResponse({"status": "error", "message": "Change not allowed."}, content_type="application/json")
        value = form.cleaned_data["value"]
        setattr(obj, field_name, value)
        # noinspection PyBroadException
        try:
            obj.save(update_fields=[field_name])
        except:
            return JsonResponse({"status": "error", "message": "Couldn't save."}, content_type="application/json")

        return JsonResponse({"status": "success"}, content_type="application/json")

    def get_context_data(self, **kwargs):
        """Update context data with some new items"""
        context = super().get_context_data(**kwargs)

        context.update({})

        return context


class TicketCreateView(CreateView):

    def get_form_class(self):
        return FORMS.get(self.kwargs.get("type"), TicketMainForm)

    def get_queryset(self):
        return MODELS.get(self.kwargs.get("type"), Ticket).objects.all()

    model = Ticket

    form_class = TicketMainForm

    def get_initial(self):
        initial = super().get_initial()
        initial = initial.copy()
        initial["application"] = Application.objects.first()
        return initial

    # def get_form(self, form_class):
    #     form = super().get_form(form_class)
    #     form.fields["batch"].choices = [(b.id, "{} > ({})".format(b.label, ", ".join([p.label for p in b.semi_elaborated_products.all()])))
    #                                     for b in Batch.objects.all()]
    #     return form

    def get_success_url(self):
        """Returns URL to go in case of success"""
        return reverse("kaoka_tracker:list")

    template_name = "tracker/create.html"

    # def form_valid(self, form):
    #     """Action to process if the form is valid"""
    #     result = super().form_valid(form)
    #
    #     ticket = self.object

    def get_context_data(self, **kwargs):
        """Update context data with some new items"""
        context = super().get_context_data(**kwargs)

        context.update({"ticket_type": _(self.kwargs.get("type"))})

        return context


class TicketDetailView(DetailView):

    model = Ticket

    template_name = "tracker/detail.html"


####################
#                  #
#     Choices      #
#                  #
####################


class ImpactChoicesView(View):

    def get(self, request, *args, **kwargs):
        """Send all impact options"""

        return JsonResponse([{instance.id: instance.label}
                             for instance in Impact.objects.all()], safe=False)


class StatusChoicesView(View):

    def get(self, request, *args, **kwargs):
        """Send all priority options"""

        return JsonResponse([{instance.id: instance.label}
                             for instance in Status.objects.all()], safe=False)


class PriorityChoicesView(View):

    def get(self, request, *args, **kwargs):
        """Send all priority options"""

        return JsonResponse([{instance.id: instance.label}
                             for instance in Priority.objects.all()], safe=False)


class TimeSensitivenessChoicesView(View):

    def get(self, request, *args, **kwargs):
        """Send all priority options"""

        return JsonResponse([{instance.id: instance.label}
                             for instance in TimeSensitiveness.objects.all()], safe=False)


class ReproducibilityChoicesView(View):

    def get(self, request, *args, **kwargs):
        """Send all priority options"""

        return JsonResponse([{instance.id: instance.label}
                             for instance in Reproducibility.objects.all()], safe=False)


class AnomalyTypeChoicesView(View):

    def get(self, request, *args, **kwargs):
        """Send all priority options"""

        return JsonResponse([{instance.id: instance.label}
                             for instance in AnomalyCategorie.objects.all()], safe=False)
