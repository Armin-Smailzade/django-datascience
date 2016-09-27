from django.db import models

# Create your models here.
class Breast_Variables(models.Model):

	id = models.AutoField(primary_key=True)
	race = models.CharField(max_length = 100, null = True)
	maritalStatus = models.CharField(max_length = 200, null = True)
	histologicType = models.CharField(max_length = 200, null = True)
	behaviorCode = models.CharField(max_length = 200, null = True)
	vitalStatusRecord = models.CharField(max_length = 200, null = True)
	grade = models.CharField(max_length = 200, null = True)
	radiation = models.CharField(max_length = 200, null = True)
	ageAtDiognosis = models.CharField(max_length = 200, null = True)
	csTumorSize = models.CharField(max_length = 200, null = True)
	regionalNodesPositive = models.CharField(max_length = 200, null = True)
	regionalNodesExamined = models.CharField(max_length = 200, null = True)
	seerHistoricStageA = models.CharField(max_length = 200, null = True)
	csLymphNode = models.CharField(max_length = 200, null = True)
	csExtension = models.CharField(max_length = 200, null = True)
	survivalMonths = models.CharField(max_length = 200, null = True)

	result = models.CharField(max_length = 200, null = True, blank = True)
	
	def __str__(self): # In python 3 use __str__
		return str(self.id)