# Generated by Django 2.1.5 on 2020-03-05 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ready_recipe', '0018_auto_20200305_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='picture',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='media/'),
        ),
    ]