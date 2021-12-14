# Generated by Django 3.2 on 2021-12-14 03:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AiAnalysisLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image_path', models.CharField(blank=True, max_length=255, null=True)),
                ('success', models.CharField(blank=True, max_length=255, null=True)),
                ('message', models.CharField(blank=True, max_length=255, null=True)),
                ('classes', models.IntegerField(blank=True, db_column='class', null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(11)])),
                ('confidence', models.DecimalField(blank=True, decimal_places=4, max_digits=5, null=True)),
                ('request_timestamp', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('response_timestamp', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
            ],
            options={
                'db_table': 'ai_analysis_log',
                'ordering': ['id'],
            },
        ),
    ]