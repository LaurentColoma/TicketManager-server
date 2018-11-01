"""
Admin interface manager.

TODO.
"""
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Application, Version, Module, Impact, Priority, TimeSensitiveness, Reproducibility, Ticket, \
    TicketComment, Process, Proposal, AnomalyCategorie, Anomaly, Status, Sprint, Roadmap, Comment


@admin.register(Application)
class ApplicationAdmin(ModelAdmin):
    pass


@admin.register(Version)
class VersionAdmin(ModelAdmin):
    pass


@admin.register(Status)
class StatusAdmin(ModelAdmin):
    pass


@admin.register(Module)
class ModuleAdmin(ModelAdmin):
    pass


@admin.register(Impact)
class ImpactAdmin(ModelAdmin):
    pass


@admin.register(Priority)
class PriorityAdmin(ModelAdmin):
    pass


@admin.register(TimeSensitiveness)
class TimeSensitivenessAdmin(ModelAdmin):
    pass


@admin.register(Reproducibility)
class ReproducibilityAdmin(ModelAdmin):
    pass


@admin.register(Ticket)
class TicketAdmin(ModelAdmin):
    pass


@admin.register(TicketComment)
class TicketCommentAdmin(ModelAdmin):
    pass


@admin.register(Process)
class TaskAdmin(ModelAdmin):
    pass


@admin.register(Proposal)
class ProposalAdmin(ModelAdmin):
    pass


@admin.register(AnomalyCategorie)
class VersionAdmin(ModelAdmin):
    pass


@admin.register(Anomaly)
class AnomalyAdmin(ModelAdmin):
    pass


@admin.register(Sprint)
class SprintAdmin(ModelAdmin):
    pass


@admin.register(Roadmap)
class RoadmapAdmin(ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    pass
