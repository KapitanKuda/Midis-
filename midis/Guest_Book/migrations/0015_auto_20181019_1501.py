# Generated by Django 2.1.2 on 2018-10-19 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest_Book', '0014_auto_20181019_0227'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-date_pub']},
        ),
    ]
