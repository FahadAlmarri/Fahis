# Generated by Django 4.1.5 on 2023-02-05 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_alter_report_report_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='id',
        ),
        migrations.AlterField(
            model_name='report',
            name='Report_ID',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, unique=True, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='sample',
            name='ReportID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.report'),
        ),
    ]
