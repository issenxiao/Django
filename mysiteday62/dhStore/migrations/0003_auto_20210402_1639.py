# Generated by Django 2.2.9 on 2021-04-02 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dhStore', '0002_auto_20210402_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='state',
            field=models.IntegerField(max_length=11),
        ),
    ]
