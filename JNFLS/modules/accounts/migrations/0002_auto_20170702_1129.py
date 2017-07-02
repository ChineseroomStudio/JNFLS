# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 11:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
        ('clubs', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentUnionDepartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='my_clubs',
            field=models.ManyToManyField(to='clubs.Club'),
        ),
        migrations.AddField(
            model_name='account',
            name='my_schoolclass',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.SchoolClass'),
        ),
        migrations.AddField(
            model_name='account',
            name='my_department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.StudentUnionDepartment'),
        ),
    ]
