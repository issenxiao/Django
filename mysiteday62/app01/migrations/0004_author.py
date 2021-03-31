# Generated by Django 2.2.9 on 2021-03-21 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_publisher_addr'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=16, unique=True)),
                ('book', models.ManyToManyField(to='app01.Book')),
            ],
        ),
    ]
