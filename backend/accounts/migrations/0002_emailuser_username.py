# Generated by Django 3.1.2 on 2020-10-30 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailuser',
            name='username',
            field=models.CharField(db_index=True, default=None, max_length=255, unique=True),
        ),
    ]