# Generated by Django 4.2.11 on 2024-04-29 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_emergencysituation'),
    ]

    operations = [
        migrations.AddField(
            model_name='emergencysituation',
            name='desc',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='emergencysituation',
            name='file',
            field=models.FileField(null=True, upload_to='file'),
        ),
    ]
