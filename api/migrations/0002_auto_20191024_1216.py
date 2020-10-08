# Generated by Django 2.2.6 on 2019-10-24 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.DecimalField(decimal_places=2, default=True, max_digits=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=models.TextField(max_length=100),
        ),
    ]
