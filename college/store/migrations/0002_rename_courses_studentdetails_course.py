# Generated by Django 4.1.7 on 2023-03-03 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentdetails',
            old_name='courses',
            new_name='course',
        ),
    ]