from django.db import models


class SfdcLead(models.Model):
    year_created = models.IntegerField()
    Month_of_Year = models.CharField(max_length=20)
    super_region = models.CharField(max_length=20)
    sub_region = models.CharField(max_length=20)
    region = models.CharField(max_length=20)
    Lead_Type = models.CharField(max_length=20)
    lead_id = models.CharField(max_length=20)


