# Generated by Django 1.10.4 on 2019-01-10 05:15


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ctirs', '0004_auto_20190110_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system',
            name='http_proxy',
            field=models.CharField(default=b'', max_length=1024),
        ),
        migrations.AlterField(
            model_name='system',
            name='https_proxy',
            field=models.CharField(default=b'', max_length=1024),
        ),
    ]
