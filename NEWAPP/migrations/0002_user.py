# Generated by Django 2.2.5 on 2019-10-01 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NEWAPP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=11)),
                ('firstname', models.CharField(max_length=55)),
                ('lastname', models.CharField(max_length=55)),
                ('password', models.CharField(max_length=55)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
