# Generated by Django 4.2.5 on 2023-09-07 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type', models.CharField(max_length=100)),
                ('value', models.TextField()),
                ('app_id', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'data',
                'managed': False,
            },
        ),
    ]
