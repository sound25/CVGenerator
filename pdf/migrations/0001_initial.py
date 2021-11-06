# Generated by Django 3.2.9 on 2021-11-06 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('summary', models.TextField(max_length=2000)),
                ('school', models.CharField(max_length=200)),
                ('univesity', models.CharField(max_length=200)),
                ('degree', models.CharField(max_length=200)),
                ('previous_work', models.TextField(max_length=2000)),
                ('skills', models.CharField(max_length=2000)),
            ],
        ),
    ]
