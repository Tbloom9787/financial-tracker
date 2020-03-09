# Generated by Django 3.0.3 on 2020-03-09 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Indice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
                ('price', models.FloatField()),
                ('change', models.FloatField()),
                ('percentChange', models.FloatField()),
            ],
        ),
    ]
