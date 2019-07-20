# Generated by Django 2.2.2 on 2019-07-05 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_auto_20190705_2217'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='date_of_birth',
            new_name='dob_in_dd_mm_yyyy',
        ),
        migrations.AlterField(
            model_name='person',
            name='lives_in',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='studies_at',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
