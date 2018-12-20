from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Ticket, Impact, Priority, TimeSensitiveness, Application, Version, Module, Status

from .models import Sprint, Roadmap, Comment


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # password and email are 2 options of this serializer
    class Meta:
        model = User
        fields = ('url', 'username', 'password', 'email','groups')

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = ('url', 'name')


class ImpactSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Impact
        fields = ('url', 'label')


class PrioritySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Priority
        fields = ('url', 'label', 'color')


class TimeSensitivenessSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TimeSensitiveness
        fields = ('url', 'label', 'color')


class ApplicationSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Application
        fields = ('url', 'label')


class VersionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Version
        fields = ('url', 'label', 'application')


class ModuleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Module
        fields = ('url', 'label', 'application')


class StatusSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Status
        fields = ('url', 'label')


class SprintSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Sprint
        fields = ('url', 'label', 'roadmap')


class RoadmapSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Roadmap
        fields = ('url', 'label')


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Comment
        fields = ('url', 'content', 'date', 'ticket')


class TicketSerializer(serializers.HyperlinkedModelSerializer):

    impact = serializers.SlugRelatedField(
        queryset=Impact.objects.all(), slug_field='label')
    status = serializers.SlugRelatedField(
        queryset=Status.objects.all(), slug_field='label')
    priority = serializers.SlugRelatedField(
        queryset=Priority.objects.all(), slug_field='label')
    time_sensitiveness = serializers.SlugRelatedField(
        queryset=TimeSensitiveness.objects.all(), slug_field='label')
    application = serializers.SlugRelatedField(
        queryset=Application.objects.all(), slug_field='label')
    version_affected_set = serializers.SlugRelatedField(
        queryset=Version.objects.all(), many=True, slug_field='label')
    module_set = serializers.SlugRelatedField(
        queryset=Module.objects.all(), many=True, slug_field='label', required=False, allow_null=True)
    responsible = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='username', required=False, allow_null=True)
    accountable = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='username', required=False, allow_null=True)
    consulted_set = serializers.SlugRelatedField(
        queryset=User.objects.all(), many=True, slug_field='username', required=False, allow_null=True)
    informed_set = serializers.SlugRelatedField(
        queryset=User.objects.all(), many=True, slug_field='username', required=False, allow_null=True)
    original = serializers.SlugRelatedField(
        queryset=Ticket.objects.all(), slug_field='label', required=False, allow_null=True)
    sprint = serializers.SlugRelatedField(
        queryset=Sprint.objects.all(), slug_field='label', required=True, allow_null=True
    )

    class Meta:
        model = Ticket
        fields = ('url',
                  'id',
                  'label',
                  'impact',
                  'status',
                  'open',
                  'priority',
                  'time_sensitiveness',
                  'responsible',
                  'accountable',
                  'consulted_set',
                  'informed_set',
                  'application',
                  'version_affected_set',
                  'original',
                  'module_set',
                  'sprint',
                  'description',
                  )




