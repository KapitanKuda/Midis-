# Generated by Django 2.1.2 on 2018-10-16 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest_Book', '0003_auto_20181016_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='ip',
            field=models.CharField(db_index=True, max_length=150),
        ),
    ]
