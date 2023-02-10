from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
	Report_ID=models.BigAutoField("id",unique=True,primary_key=True,auto_created=True)
	Score = models.IntegerField('Score',null=True)
	Network = models.JSONField('Network',null=True)
	Duration = models.IntegerField('Duration',null=True)
	Processes = models.JSONField('Processes',null=True)
	Report_Type = models.CharField("Report_Type", max_length=5)
	Report_Address = models.TextField("Report_Address")
	task_id=models.IntegerField("task_id",null=True)

	def __int__(self):
		return self.Report_ID




# class FahisUser(models.Model):
# 	User_ID = models.IntegerField('User ID')
# 	Username= models.CharField('Username', max_length=120)
# 	fname = models.CharField('First Name', max_length=120)
# 	lname = models.CharField('Last name', max_length=120)
# 	User_Email = models.EmailField('User Email')

# 	def __str__(self):
# 		return self.fname + ' ' + self.lname

class Sample(models.Model):
	id=models.BigAutoField("id",unique=True,primary_key=True,auto_created=True)
	ReportID = models.ForeignKey(Report,to_field="Report_ID", null=True,on_delete=models.CASCADE)
	Privacy_Type = models.CharField('Privacy_Type', max_length=8)
	Create_Date = models.DateTimeField('Creation_Date')
	Sample_Type = models.CharField("Sample_Type", max_length=5)
	UserID = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	Sample_Address = models.TextField("Sample_Address", null=True)
	Sample_name=models.TextField("Sample_name",null=True)
	Environment=models.TextField("Environment",null=True)
	def __int__(self):
		return self.Sample_ID