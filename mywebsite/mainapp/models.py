from django.db import models

class Report(models.Model):
	Report_ID = models.IntegerField('Report ID')
	Behavior = models.CharField('Behavior', max_length=120)
	Signature = models.CharField('Signature', max_length=120)
	Metadata = models.CharField('Metadata', max_length=120)
	Others = models.TextField(blank=True)

	def __int__(self):
		return self.Report_ID


class FahisUser(models.Model):
	User_ID = models.IntegerField('User ID')
	fname = models.CharField('First Name', max_length=120)
	lname = models.CharField('Last name', max_length=120)
	User_Email = models.EmailField('User Email')

	def __str__(self):
		return self.fname + ' ' + self.lname

class Sample(models.Model):
	Sample_ID = models.IntegerField('Sample ID')
	Report = models.ForeignKey(Report, blank=True, null=True, on_delete=models.CASCADE)
	Privacy_Type = models.CharField('Privacy Type', max_length=8)
	Create_Date = models.DateTimeField('Creation Date')
	Sample_Type = models.CharField("Sample Type", max_length=5)
	Scanner = models.OneToOneField(FahisUser, blank=True, on_delete=models.RESTRICT)

	def __int__(self):
		return self.Sample_ID