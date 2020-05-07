# Generated by Django 3.0.5 on 2020-04-18 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip', models.CharField(max_length=5)),
                ('snow_days_this_year', models.IntegerField(default=-1)),
                ('school_type', models.CharField(choices=[('PU', 'Public'), ('UP', 'Urban Public'), ('RP', 'Rural Public'), ('PR', 'Private'), ('BO', 'Boarding')], default='PU', max_length=2)),
            ],
        ),
    ]
