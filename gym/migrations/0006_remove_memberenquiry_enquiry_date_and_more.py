# Generated by Django 5.0.4 on 2024-09-29 12:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0005_memberenquiry'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberenquiry',
            name='enquiry_date',
        ),
        migrations.RemoveField(
            model_name='memberenquiry',
            name='is_resolved',
        ),
        migrations.AddField(
            model_name='memberenquiry',
            name='submitted_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='memberenquiry',
            name='branch',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='memberenquiry',
            name='contact',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='memberenquiry',
            name='emailid',
            field=models.EmailField(max_length=255),
        ),
        migrations.AlterField(
            model_name='memberenquiry',
            name='issue',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='memberenquiry',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
