# Generated by Django 3.0.5 on 2023-03-29 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0005_feedback_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='occasion',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
