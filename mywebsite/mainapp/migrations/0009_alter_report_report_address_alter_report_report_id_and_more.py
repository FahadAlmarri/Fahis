# Generated by Django 4.1.5 on 2023-02-02 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_alter_report_report_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='Report_Address',
            field=models.TextField(verbose_name='Report_Address'),
        ),
        migrations.AlterField(
            model_name='report',
            name='Report_ID',
            field=models.IntegerField(auto_created=True, unique=True, verbose_name='Report_ID'),
        ),
        migrations.AlterField(
            model_name='report',
            name='Report_Type',
            field=models.CharField(max_length=5, verbose_name='Report_Type'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Create_Date',
            field=models.DateTimeField(verbose_name='Creation_Date'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Privacy_Type',
            field=models.CharField(max_length=8, verbose_name='Privacy_Type'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Sample_Address',
            field=models.TextField(null=True, verbose_name='Sample_Address'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Sample_Type',
            field=models.CharField(max_length=5, verbose_name='Sample_Type'),
        ),
    ]
