# Generated by Django 4.2.9 on 2024-04-27 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_foodtimetable'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=100)),
                ('bf_af', models.CharField(max_length=100)),
                ('times', models.CharField(max_length=100)),
                ('resident', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.residents')),
            ],
        ),
    ]
