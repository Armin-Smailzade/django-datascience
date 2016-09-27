# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breast_Variables',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('race', models.CharField(null=True, max_length=100)),
                ('maritalStatus', models.CharField(null=True, max_length=200)),
                ('histologicType', models.CharField(null=True, max_length=200)),
                ('behaviorCode', models.CharField(null=True, max_length=200)),
                ('vitalStatusRecord', models.CharField(null=True, max_length=200)),
                ('grade', models.CharField(null=True, max_length=200)),
                ('radiation', models.CharField(null=True, max_length=200)),
                ('ageAtDiognosis', models.CharField(null=True, max_length=200)),
                ('csTumorSize', models.CharField(null=True, max_length=200)),
                ('regionalNodesPositive', models.CharField(null=True, max_length=200)),
                ('regionalNodesExamined', models.CharField(null=True, max_length=200)),
                ('seerHistoricStageA', models.CharField(null=True, max_length=200)),
                ('csLymphNode', models.CharField(null=True, max_length=200)),
                ('csExtension', models.CharField(null=True, max_length=200)),
                ('survivalMonths', models.CharField(null=True, max_length=200)),
                ('result', models.CharField(blank=True, null=True, max_length=200)),
            ],
        ),
    ]
