# Generated by Django 2.1 on 2018-08-15 19:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0002_auto_20180814_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
