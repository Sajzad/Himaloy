# Generated by Django 2.1.7 on 2008-04-21 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='post_comment',
        ),
    ]
