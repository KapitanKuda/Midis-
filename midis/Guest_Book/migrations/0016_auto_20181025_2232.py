# Generated by Django 2.1.2 on 2018-10-25 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest_Book', '0015_auto_20181019_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='site',
            field=models.URLField(blank=True, max_length=150, null=True),
        ),
    ]
