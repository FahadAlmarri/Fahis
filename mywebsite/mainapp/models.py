from django.db import models
from django.contrib.auth.models import User

class Report(models.Model):
	Report_ID = models.IntegerField('Report ID', unique=True)
	Behavior = models.CharField('Behavior', max_length=120)
	Signature = models.CharField('Signature', max_length=120)
	Metadata = models.CharField('Metadata', max_length=120)
	Others = models.TextField(blank=True)

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
	ReportID = models.ForeignKey(Report, null=True,on_delete=models.CASCADE)
	Privacy_Type = models.CharField('Privacy Type', max_length=8)
	Create_Date = models.DateTimeField('Creation Date')
	Sample_Type = models.CharField("Sample Type", max_length=5)
	UserID = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	Sample_Address = models.TextField("Sample Address", null=True)
	def __int__(self):
		return self.Sample_ID