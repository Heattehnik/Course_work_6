# Generated by Django 4.2.3 on 2023-07-28 04:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sender', '0007_remove_mailing_is_active_mailing_send_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mailinglog',
            name='client',
        ),
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
        migrations.RemoveField(
            model_name='mailingmessage',
            name='user',
        ),
        migrations.AddField(
            model_name='mailingmessage',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='пользователь'),
        ),
    ]