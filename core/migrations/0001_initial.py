# Generated by Django 5.0.6 on 2024-07-03 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('full_name', models.CharField(max_length=10000)),
                ('dob', models.DateTimeField(blank=True, null=True)),
                ('contact_phone', models.CharField(max_length=12)),
                ('contact_mail', models.CharField(max_length=100)),
            ],
        ),
    ]
