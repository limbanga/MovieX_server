# Generated by Django 5.2.1 on 2025-06-30 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_booking_app_trans_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cinema',
            name='address',
        ),
        migrations.AddField(
            model_name='cinema',
            name='district',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cinema',
            name='street',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='cinema',
            name='ward',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cinema',
            name='city',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
