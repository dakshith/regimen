from django.db import models

# Create your models here.

class QuestionMaster(models.Model):
    question = models.TextField()
    shortName = models.CharField(max_length=500, default=None)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.shortName


class OptionMaster(models.Model):
    questionId = models.ForeignKey(QuestionMaster, on_delete=models.CASCADE, related_name='optons')
    option = models.CharField(max_length=100)
    optionWeight = models.IntegerField(default=0)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.option

    
class ResponseData(models.Model):
    confidence = models.CharField(max_length=100)
    penetration = models.CharField(max_length=100)
    intercourse = models.CharField(max_length=100)
    completion = models.CharField(max_length=100)
    satisfaction = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    avgScore = models.FloatField(default=0.00)

    # def __str__(self):
    #     return self.score




