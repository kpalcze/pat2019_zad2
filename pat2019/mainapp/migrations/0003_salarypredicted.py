# Generated by Django 2.1.5 on 2019-01-09 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20190108_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalaryPredicted',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workedYears', models.FloatField(null=True)),
                ('salaryBrutto', models.FloatField(null=True)),
                ('salaryBruttoPredicted', models.FloatField(null=True)),
            ],
        ),
    ]
