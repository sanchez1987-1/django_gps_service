# Generated by Django 4.2.5 on 2023-10-17 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserParamsApi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_id', models.CharField(max_length=100)),
                ('app_pass', models.CharField(max_length=200)),
                ('app_api_key', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'user_params',
                'managed': False,
            },
        ),
    ]
