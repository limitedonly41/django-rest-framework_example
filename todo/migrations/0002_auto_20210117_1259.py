# Generated by Django 3.1.5 on 2021-01-17 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
