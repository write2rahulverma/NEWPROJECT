# Generated by Django 2.2.5 on 2019-09-26 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=11)),
                ('pname', models.CharField(max_length=55)),
                ('price', models.CharField(max_length=11)),
                ('pdesc', models.CharField(max_length=55)),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]