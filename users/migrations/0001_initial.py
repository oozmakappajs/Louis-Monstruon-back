# Generated by Django 3.0.6 on 2020-05-15 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('create', models.DateTimeField(auto_now_add=True)),
                ('edit', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
