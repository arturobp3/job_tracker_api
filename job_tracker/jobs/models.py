from django.db import models

# Create your models here.

class JobApplication(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    application_date = models.DateField()
    status = models.CharField(max_length=50, choices=[
        ('Enviado', 'Enviado'),
        ('En Proceso', 'En Proceso'),
        ('Entrevista', 'Entrevista'),
        ('Ofrecido', 'Ofrecido'),
        ('Rechazado', 'Rechazado'),
    ])
    responsibilities = models.TextField(blank=True)
    technologies = models.CharField(max_length=100, blank=True)
    experience_level = models.CharField(max_length=50, blank=True)
    salary_benefits = models.CharField(max_length=100, blank=True)
    contact = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.position} at {self.company}"
