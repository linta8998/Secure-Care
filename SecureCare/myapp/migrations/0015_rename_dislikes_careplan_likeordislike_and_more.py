# Generated by Django 4.2.9 on 2024-04-27 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_careplan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='careplan',
            old_name='disLikes',
            new_name='likeOrdislike',
        ),
        migrations.RemoveField(
            model_name='careplan',
            name='likes',
        ),
    ]
