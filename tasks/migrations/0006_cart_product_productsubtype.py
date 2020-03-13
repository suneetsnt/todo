# Generated by Django 3.0.4 on 2020-03-07 19:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0005_auto_20200308_0036'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSubType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtype', models.CharField(max_length=200)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.ProductType')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1000)),
                ('productType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.ProductSubType')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]