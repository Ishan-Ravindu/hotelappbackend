# Generated by Django 3.1.4 on 2021-01-13 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20201226_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('BF', 'උදේ'), ('LU', 'දවල්'), ('DI', 'රාත්\u200dරි'), ('SN', 'බයිට්'), ('OT', 'වෙනත්'), ('BF-LU', 'උදේ-දවල්'), ('BF-DI', 'උදේ-රාත්\u200dරි'), ('LU-DI', 'දවල්-රාත්\u200dරි'), ('BF-LU-DI', 'උදේ-දවල්-රාත්\u200dරි')], max_length=50),
        ),
    ]
