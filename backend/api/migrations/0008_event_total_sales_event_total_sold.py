# Generated by Django 4.0.10 on 2023-08-26 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_user_image_alter_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='total_sales',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='event',
            name='total_sold',
            field=models.IntegerField(default=0),
        ),
    ]
