# Generated by Django 5.0 on 2023-12-14 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_contactinformation_contactmessages_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='contact_map',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
