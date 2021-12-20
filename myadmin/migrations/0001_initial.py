# Generated by Django 2.2.24 on 2021-12-18 14:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=50)),
            ],
            options={
                'db_table': ' permission',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('permission', models.ManyToManyField(to='myadmin.Permission')),
            ],
            options={
                'db_table': 'role',
            },
        ),
        migrations.CreateModel(
            name='waitui',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('datetime1', models.DateTimeField(default=datetime.datetime.now)),
                ('ridername', models.CharField(max_length=100)),
                ('riderphone', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=50)),
                ('detailes', models.CharField(max_length=50)),
                ('onboarding', models.CharField(max_length=50)),
                ('onboardtime', models.CharField(max_length=50)),
                ('threedays', models.CharField(max_length=50)),
                ('threeonjob', models.CharField(max_length=50)),
                ('sevendays', models.CharField(max_length=50)),
                ('sevenonjob', models.CharField(max_length=50)),
                ('fifitydays', models.CharField(max_length=50)),
                ('fifityonjob', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'waitui',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('pwd', models.ManyToManyField(to='myadmin.Role')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]