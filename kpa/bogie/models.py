from django.db import models

# Create your models here.

class WheelSpecification(models.Model):
    formNumber = models.CharField(max_length=50)
    submittedBy = models.CharField(max_length=100)
    submittedDate = models.DateField()

    fields = models.JSONField()

    def __str__(self):
        return self.formNumber
    

class BogieChecksheet(models.Model):
    
    formNumber = models.CharField(max_length=50,unique=True)
    inspectionBy = models.CharField(max_length=100)
    inspectionDate = models.DateField()
    
    bogieDetails = models.JSONField()
    bogieChkSheet = models.JSONField()
    bmbcChkSheet = models.JSONField()
    
    status = models.CharField(max_length=20,default='Saved')
    
    def __str__(self):
        return self.formNumber 
    