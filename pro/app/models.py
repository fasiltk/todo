# from django.db import models

# # Create your models here.
# class Task(models.Model):
#     name=models.CharField(max_length=244)
#     title=models.CharField(max_length=244)
#     description=models.CharField(max_length=244)
#     duedate=models.DateField()
#     # status=models.IntegerField()
#     def __str__(self):
#         return f"{self.name}"
# class Status(models.Model):
#     task =models.ForeignKey(Task,on_delete=models.CASCADE)
#     status=models.IntegerField()


from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=244)
    title = models.CharField(max_length=244)
    description = models.CharField(max_length=244)
    duedate = models.DateField()
    
    def __str__(self):
        return f"{self.name}"

class Status(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.IntegerField()
    
    def __str__(self):
        return f"Status: {self.status} for Task: {self.task.name}"
