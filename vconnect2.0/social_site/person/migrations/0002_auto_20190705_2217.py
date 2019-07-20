# Generated by Django 2.2.2 on 2019-07-05 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='lives_in',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='studies_at',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
