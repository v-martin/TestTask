# Generated by Django 4.1.7 on 2023-02-25 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_sale_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='user_id',
            field=models.CharField(max_length=6),
        ),
    ]
