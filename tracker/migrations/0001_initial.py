# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-22 09:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnomalyCategorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=64, verbose_name='label')),
            ],
            options={
                'verbose_name_plural': 'anomaly types',
                'verbose_name': 'anomaly type',
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=64, verbose_name='label')),
            ],
            options={
                'verbose_name_plural': 'applications',
                'verbose_name': 'application',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=140, verbose_name='content')),
                ('date', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': 'comments',
                'verbose_name': 'comment',
            },
        ),
        migrations.CreateModel(
            name='Impact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=64, verbose_name='label')),
            ],
            options={
                'verbose_name_plural': 'impact choices',
                'verbose_name': 'impact choice',
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=64, verbose_name='label')),
                ('application', models.ForeignKey(blank=True, help_text='Related application', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='module_set', to='tracker.Application', verbose_name='Application')),
            ],
            options={
                'verbose_name_plural': 'modules',
                'verbose_name': 'module',
            },
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=64, verbose_name='label')),
                ('color', models.CharField(help_text='Color associated with this priority', max_length=10, verbose_name='Color')),
            ],
            options={
                'verbose_name_plural': 'priorities choices',
                'verbose_name': 'priority choice',
            },
        ),
        migrations.CreateModel(
            name='Reproducibility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=64, verbose_name='label')),
            ],
            options={
                'verbose_name_plural': 'reproducibility choices',
                'verbose_name': 'reproducibility choice',
            },
        ),
        migrations.CreateModel(
            name='Roadmap',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=64, verbose_name='label')),
            ],
            options={
                'verbose_name_plural': 'roadmaps',
                'verbose_name': 'roadmap',
            },
        ),
        migrations.CreateModel(
            name='Sprint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=64, verbose_name='label')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('roadmap', models.ForeignKey(help_text='Related Roadmap', on_delete=django.db.models.deletion.CASCADE, related_name='sprint', to='tracker.Roadmap', verbose_name='roadmap')),
            ],
            options={
                'verbose_name_plural': 'sprints',
                'verbose_name': 'sprint',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=64, verbose_name='label')),
            ],
            options={
                'verbose_name_plural': 'statuses',
                'verbose_name': 'status',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=64, verbose_name='Ticket')),
                ('number', models.PositiveSmallIntegerField(help_text="Ticket's comment number", verbose_name='Number')),
                ('description', models.TextField(help_text='Do yourself a favour : be as exhaustive as you can !', verbose_name='Description')),
                ('open', models.BooleanField(default=True, help_text='is the ticket close or open', verbose_name='Open')),
                ('start', models.DateField(blank=True, help_text='the day the ticket was created', null=True, verbose_name='Starting Date')),
                ('end', models.DateField(blank=True, help_text='the day the ticket was closed', null=True, verbose_name='Ending Date')),
            ],
            options={
                'verbose_name_plural': 'tickets',
                'verbose_name': 'ticket',
            },
        ),
        migrations.CreateModel(
            name='TicketComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labelTicketComment', models.CharField(max_length=64, verbose_name='TicketComment')),
                ('number', models.PositiveSmallIntegerField(help_text="Ticket's comment number", verbose_name='Number')),
                ('comment', models.TextField(help_text='Type your comment here: ', verbose_name='Comment')),
                ('author', models.ForeignKey(blank=True, help_text='Author of the comment', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tracker_ticket_comment_set', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'verbose_name_plural': 'ticket comments',
                'verbose_name': 'ticket comment',
            },
        ),
        migrations.CreateModel(
            name='TimeSensitiveness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=64, verbose_name='label')),
                ('color', models.CharField(help_text='Color associated with this time sensitiveness', max_length=10, verbose_name='Color')),
            ],
            options={
                'verbose_name_plural': 'time sensitiveness choices',
                'verbose_name': 'time sensitiveness choice',
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=64, verbose_name='label')),
                ('application', models.ForeignKey(blank=True, help_text='Related application', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='version_set', to='tracker.Application', verbose_name='Application')),
            ],
            options={
                'verbose_name_plural': 'versions',
                'verbose_name': 'version',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('ticket_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tracker.Ticket')),
                ('commit_number', models.CharField(help_text='For traceability purposes (can be revert)', max_length=64, verbose_name='Commit number')),
            ],
            options={
                'verbose_name_plural': 'tasks',
                'verbose_name': 'task',
            },
            bases=('tracker.ticket',),
        ),
        migrations.AddField(
            model_name='ticketcomment',
            name='ticket',
            field=models.ForeignKey(blank=True, help_text='Ticket related to this comment', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_set', to='tracker.Ticket', verbose_name='Ticket'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='accountable',
            field=models.ForeignKey(blank=True, help_text='MOA leader on this ticket, A in RACI matrix', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tracker_ticket_accountable_set', to=settings.AUTH_USER_MODEL, verbose_name='Person accountable for this ticket'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='application',
            field=models.ForeignKey(blank=True, help_text='Related application', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_set', to='tracker.Application', verbose_name='Application'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='consulted_set',
            field=models.ManyToManyField(blank=True, help_text='Person with useful knowledge, C in RACI matrix', null=True, related_name='tracker_ticket_consulted_set', to=settings.AUTH_USER_MODEL, verbose_name='Person that must be consulted for this ticket'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='impact',
            field=models.ForeignKey(help_text='Is resolving this ticket will make a big difference ?', on_delete=django.db.models.deletion.CASCADE, related_name='ticket_set', to='tracker.Impact', verbose_name='Impact'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='informed_set',
            field=models.ManyToManyField(blank=True, help_text='Person concerned about this ticket, I in RACI matrix', null=True, related_name='tracker_ticket_informed_set', to=settings.AUTH_USER_MODEL, verbose_name='Person that must be informed about this ticket'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='module_set',
            field=models.ManyToManyField(blank=True, help_text='Related module', null=True, related_name='ticket_set', to='tracker.Module', verbose_name='Module'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='original',
            field=models.ForeignKey(blank=True, help_text='Mark this ticket as a duplicate of:', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='duplicate_set', to='tracker.Ticket', verbose_name='Original ticket'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_tracker.ticket_set+', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='priority',
            field=models.ForeignKey(help_text='Is resolving this ticket is game changing ?', on_delete=django.db.models.deletion.CASCADE, related_name='ticket_set', to='tracker.Priority', verbose_name='Priority'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='responsible',
            field=models.ForeignKey(blank=True, help_text='MOE leader on this ticket, R in RACI matrix', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tracker_ticket_responsible_set', to=settings.AUTH_USER_MODEL, verbose_name='Person in charge of this ticket'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='roadmap',
            field=models.ForeignKey(help_text='Related Roadmap', on_delete=django.db.models.deletion.CASCADE, related_name='ticket_set', to='tracker.Roadmap', verbose_name='roadmap'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='sprint',
            field=models.ForeignKey(blank=True, help_text='Related Sprint', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_set', to='tracker.Sprint', verbose_name='Sprint'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.ForeignKey(help_text='state of the ticket', on_delete=django.db.models.deletion.CASCADE, related_name='status_of_ticket', to='tracker.Status', verbose_name='Status'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='time_sensitiveness',
            field=models.ForeignKey(help_text='Is resolving this ticket is a matter of emergency or a long ', on_delete=django.db.models.deletion.CASCADE, related_name='ticket_set', to='tracker.TimeSensitiveness', verbose_name='Time sensitiveness'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='version_affected_set',
            field=models.ManyToManyField(blank=True, help_text='Application versions that are affected by the ticket', null=True, related_name='ticket_affected_set', to='tracker.Version', verbose_name='Affected versions'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='version_released',
            field=models.ForeignKey(blank=True, help_text='The ticket have been released  in version:', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket_released_set', to='tracker.Version', verbose_name='Version'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='version_targeted',
            field=models.ForeignKey(blank=True, help_text='Aimed version for the release of this ticket', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tickets_targeted_set', to='tracker.Version', verbose_name='Version'),
        ),
        migrations.AddField(
            model_name='comment',
            name='ticket',
            field=models.ForeignKey(help_text='Related Ticket', on_delete=django.db.models.deletion.CASCADE, related_name='set_comment', to='tracker.Ticket', verbose_name='ticket'),
        ),
        migrations.CreateModel(
            name='Anomaly',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tracker.Task')),
                ('step_to_reproduce', models.TextField(help_text='Explain how the anomaly occurs', verbose_name='Step to reproduce')),
                ('reproducibility', models.ForeignKey(blank=True, help_text='Is this anomaly occurs sometimes or always', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='anomaly_set', to='tracker.Reproducibility', verbose_name='Reproducibility')),
                ('type', models.ForeignKey(help_text='Type of anomalie', on_delete=django.db.models.deletion.CASCADE, related_name='anomaly_set', to='tracker.AnomalyCategorie', verbose_name='Type')),
            ],
            options={
                'verbose_name_plural': 'anomalies',
                'verbose_name': 'anomaly',
            },
            bases=('tracker.task',),
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tracker.Task')),
            ],
            options={
                'verbose_name_plural': 'processes',
                'verbose_name': 'process',
            },
            bases=('tracker.task',),
        ),
        migrations.CreateModel(
            name='Proposal',
            fields=[
                ('task_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='tracker.Task')),
            ],
            options={
                'verbose_name_plural': 'proposals',
                'verbose_name': 'proposal',
            },
            bases=('tracker.task',),
        ),
        migrations.AddField(
            model_name='task',
            name='assigned_to',
            field=models.ForeignKey(blank=True, help_text='User assigned to the task of resolving this ticket', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tracker_task_set', to=settings.AUTH_USER_MODEL, verbose_name='assigned_to'),
        ),
    ]