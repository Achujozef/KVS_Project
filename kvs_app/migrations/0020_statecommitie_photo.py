# Generated by Django 4.1 on 2023-01-24 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kvs_app', '0019_alter_join_kvs_sakha_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='statecommitie',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='state commitie'),
        ),
    ]