# Generated by Django 2.0.6 on 2019-05-25 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dangdangapp', '0003_auto_20190525_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='torder_ok',
            name='t_userid',
            field=models.ForeignKey(db_column='t_userid', on_delete=django.db.models.deletion.DO_NOTHING, to='dangdangapp.TUser'),
        ),
    ]
