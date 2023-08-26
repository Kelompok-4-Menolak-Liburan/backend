# Generated by Django 4.0.10 on 2023-08-26 04:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_salesdata_ticket_userticket_sales_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_online',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='salesdata',
            name='organizer',
            field=models.ForeignKey(default='ce5b638f-340b-4d86-893a-be4528366f36', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]