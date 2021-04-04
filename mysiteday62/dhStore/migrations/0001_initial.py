# Generated by Django 2.2.9 on 2021-04-02 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=16, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='orderitem',
            fields=[
                ('itemid', models.AutoField(primary_key=True, serialize=False)),
                ('count', models.CharField(max_length=32)),
                ('subtotal', models.CharField(max_length=16)),
                ('pid', models.CharField(max_length=32, unique=True)),
                ('oid', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('oid', models.CharField(max_length=32, primary_key=True, serialize=False, unique=True)),
                ('orderitem', models.DateTimeField()),
                ('total', models.CharField(max_length=64)),
                ('state', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=20)),
                ('telephone', models.CharField(max_length=20)),
                ('uid', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('pid', models.CharField(max_length=32, primary_key=True, serialize=False, unique=True)),
                ('pname', models.CharField(max_length=50)),
                ('market_price', models.CharField(max_length=50)),
                ('pimage', models.CharField(max_length=200)),
                ('pdate', models.DateField()),
                ('is_hot', models.CharField(max_length=11)),
                ('pdesc', models.CharField(max_length=255)),
                ('pflag', models.CharField(max_length=11)),
                ('cid', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('uid', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('telephone', models.CharField(max_length=20)),
                ('birthday', models.DateField()),
                ('sex', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=11)),
                ('code', models.CharField(max_length=64)),
            ],
        ),
    ]
