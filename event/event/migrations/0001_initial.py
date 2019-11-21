# Generated by Django 2.2.7 on 2019-11-21 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import event.xlib.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=event.xlib.utils.generate_uid, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=3000, null=True)),
                ('photo', models.URLField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'event.event ',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='EventTag',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=event.xlib.utils.generate_uid, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('events', models.ManyToManyField(related_name='tags', to='event_event.Event')),
            ],
            options={
                'db_table': 'event.event_tag',
                'managed': True,
            },
        ),
    ]