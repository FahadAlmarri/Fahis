# Generated by Django 4.1.5 on 2023-02-01 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_remove_report_behavior_remove_report_metadata_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='Report_Address',
            field=models.TextField(default=564654, verbose_name='Report Address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='Report_Type',
            field=models.CharField(default='file', max_length=5, verbose_name='Report Type'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sample',
            name='ReportID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.report', to_field='Report_ID'),
        ),
    ]
