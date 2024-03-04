from django.db import models

class Position(models.Model):
    position_id = models.AutoField(primary_key=True)
    position_title = models.CharField(max_length=120)


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    staff_name = models.CharField(max_length=128)
    staff_surname = models.CharField(max_length=128, null=True, blank=True)
    staff_birthday = models.DateField()
    staff_position = models.ForeignKey(Position, on_delete=models.CASCADE)



 # staff_image = models.TextField()