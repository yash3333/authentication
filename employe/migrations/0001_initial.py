# Generated by Django 3.2.5 on 2021-08-06 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('designation', models.CharField(max_length=50)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('age', models.IntegerField()),
                ('companyname', models.CharField(max_length=50)),
            ],
        ),
    ]
