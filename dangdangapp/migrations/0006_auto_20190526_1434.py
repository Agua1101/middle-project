# Generated by Django 2.0.6 on 2019-05-26 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dangdangapp', '0005_auto_20190526_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torder_ok',
            name='t_code',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
