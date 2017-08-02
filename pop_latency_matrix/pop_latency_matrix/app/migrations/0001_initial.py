# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-01 16:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PointOfPresence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pop_a', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pop_a', to='app.PointOfPresence')),
                ('pop_b', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pop_b', to='app.PointOfPresence')),
            ],
        ),
        migrations.CreateModel(
            name='TestType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('unit', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='tests',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.TestType'),
        ),
    ]