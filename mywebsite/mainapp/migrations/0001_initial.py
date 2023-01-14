# Generated by Django 4.1.4 on 2022-12-27 12:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FahisUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_ID', models.IntegerField(verbose_name='User ID')),
                ('fname', models.CharField(max_length=120, verbose_name='First Name')),
                ('lname', models.CharField(max_length=120, verbose_name='Last name')),
                ('User_Email', models.EmailField(max_length=254, verbose_name='User Email')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Report_ID', models.IntegerField(verbose_name='Report ID')),
                ('Behavior', models.CharField(max_length=120, verbose_name='Behavior')),
                ('Signature', models.CharField(max_length=120, verbose_name='Signature')),
                ('Metadata', models.CharField(max_length=120, verbose_name='Metadata')),
                ('Others', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sample_ID', models.IntegerField(verbose_name='Sample ID')),
                ('Privacy_Type', models.CharField(max_length=8, verbose_name='Privacy Type')),
                ('Create_Date', models.DateTimeField(verbose_name='Creation Date')),
                ('Sample_Type', models.CharField(max_length=5, verbose_name='Sample Type')),
                ('Report', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.report')),
                ('Scanner', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.RESTRICT, to='mainapp.fahisuser')),
            ],
        ),
    ]