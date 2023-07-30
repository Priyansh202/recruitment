from django.db import models

class Jobs(models.Model):
    JOB_TYPES = [
        ('Full-Time', 'Full-Time'),
        ('Part-Time', 'Part-Time'),
        ('Contract', 'Contract'),
    ]

    title = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=20, choices=JOB_TYPES)
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.title
