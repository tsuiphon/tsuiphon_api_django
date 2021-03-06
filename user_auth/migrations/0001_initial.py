# Generated by Django 2.1.7 on 2019-02-24 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=255)),
                ('talk_id', models.CharField(max_length=255)),
                ('user1_uid', models.CharField(max_length=255)),
                ('user1_provider', models.CharField(max_length=255)),
                ('user2_uid', models.CharField(max_length=255, null=True)),
                ('user2_provider', models.CharField(max_length=255, null=True)),
                ('created_at', models.IntegerField()),
                ('updated_at', models.IntegerField()),
                ('is_close', models.BooleanField(default=False)),
                ('is_wait', models.BooleanField(default=True)),
                ('flag', models.IntegerField(default=0)),
            ],
        ),
    ]
