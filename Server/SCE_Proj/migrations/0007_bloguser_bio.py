# Generated by Django 3.2.9 on 2021-12-30 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SCE_Proj', '0006_alter_bloguser_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloguser',
            name='bio',
            field=models.CharField(default='', max_length=300, null=True),
        ),
    ]
