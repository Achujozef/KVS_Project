# Generated by Django 4.1 on 2023-08-22 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kvs_app', '0036_services_district'),
    ]

    operations = [
        migrations.CreateModel(
            name='Databank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.IntegerField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='databankpic')),
                ('occupation', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('taluk', models.CharField(max_length=50)),
                ('workplace', models.CharField(max_length=50)),
                ('contact_person', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='matrimonial',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Approved', max_length=25),
        ),
    ]
