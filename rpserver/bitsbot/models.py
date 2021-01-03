from django.db import models

# Create your models here.
class BitsEnteranceExamInformation(models.Model):
	exam_type = models.CharField(max_length=50)
	info = models.CharField(max_length=2000)

class BitsEnteranceExamCenters(models.Model):
	exam_type = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	examcentercity = models.CharField(max_length=50)
	examcenteraddress = models.CharField(max_length=255)

class BitsCourseInformation(models.Model):
	course = models.CharField(max_length=50)
	info = models.TextField()

class BitsExamSyllabus(models.Model):
	exam_type = models.CharField(max_length=50)
	branch = models.CharField(max_length=50)
	syllabus = models.CharField(max_length=2000)

class BitsExamFee(models.Model):
	exam_type = models.CharField(max_length=50)
	fee = models.CharField(max_length=1000)

class BitsCourseFee(models.Model):
	course = models.CharField(max_length=50)
	fee = models.CharField(max_length=1000)

class BitsBranchCampusMapping(models.Model):
	course = models.CharField(max_length=50)
	branch = models.CharField(max_length=50)
	campus = models.CharField(max_length=50)