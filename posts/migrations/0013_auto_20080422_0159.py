# Generated by Django 2.1.7 on 2008-04-21 19:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20080422_0156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='Timestamp',
            new_name='timestamp',
        ),
    ]