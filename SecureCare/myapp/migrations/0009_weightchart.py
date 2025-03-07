# Generated by Django 4.2.11 on 2024-04-26 05:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeightChart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('login', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
