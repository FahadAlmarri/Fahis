# Generated by Django 4.1.5 on 2023-02-01 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_alter_sample_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='Sample_name',
            field=models.TextField(null=True, verbose_name='Sample_name'),
        ),
    ]
