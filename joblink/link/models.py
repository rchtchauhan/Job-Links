from django.db import models

class Job(models.Model):
    EXPERIENCE_CHOICES = (
        ('0-2', '0-2 years'),
        ('3-5', '3-5 years'),
        ('6-8', '6-8 years'),
        ('9-12', '9-12 years'),
        ('12+', '12+ years'),
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    experience_level = models.CharField(max_length=50, choices=EXPERIENCE_CHOICES)
    job_location = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    company_website = models.URLField()
    apply_link = models.URLField()

    def __str__(self):
        return self.title

# Create your models here.
