# Generated by Django 4.1 on 2023-01-24 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kvs_app', '0021_join_kvs_age_join_kvs_district_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sex_Choices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='join_kvs',
            name='sex',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kvs_app.sex_choices'),
        ),
    ]
