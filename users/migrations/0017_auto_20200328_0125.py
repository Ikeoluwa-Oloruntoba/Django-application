# Generated by Django 3.0.4 on 2020-03-28 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20200328_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='award_month_year',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='award',
            name='award_place',
            field=models.CharField(max_length=100),
        ),
    ]