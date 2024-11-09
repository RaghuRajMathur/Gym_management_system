# Generated by Django 5.1.2 on 2024-11-09 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0007_member_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('trainer_id', models.AutoField(primary_key=True, serialize=False)),
                ('trainer_name', models.CharField(max_length=150)),
                ('trainer_password', models.CharField(default='default_password', max_length=100)),
                ('chatroom_id', models.CharField(max_length=50, null=True)),
                ('contact', models.CharField(max_length=15, null=True)),
                ('email', models.EmailField(max_length=50, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='chatroom_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
