# Generated by Django 3.1.4 on 2021-01-13 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('conform', 'conform'), ('dileved', 'dileved'), ('rejected', 'rejected')], max_length=50),
        ),
    ]
