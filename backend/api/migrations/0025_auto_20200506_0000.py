# Generated by Django 3.0.3 on 2020-05-06 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0024_auto_20200505_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='id',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]