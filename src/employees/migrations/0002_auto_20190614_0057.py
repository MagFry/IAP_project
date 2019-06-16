# Generated by Django 2.2.2 on 2019-06-13 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeshours',
            name='id',
        ),
        migrations.AlterField(
            model_name='employeeshours',
            name='employees_hours_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='employees',
            name='pay',
            field=models.IntegerField(default=0),
        ),
    ]
