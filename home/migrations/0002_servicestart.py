# Generated by Django 4.2.1 on 2023-12-13 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceStart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=200)),
            ],
        ),
    ]
