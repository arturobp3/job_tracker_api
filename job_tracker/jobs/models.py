from django.db import models

# Create your models here.

class JobApplication(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    application_date = models.DateField()
    status = models.CharField(max_length=50, choices=[
        ('Guardada', 'Guardada'),
        ('Enviado', 'Enviado'),
        ('En Proceso', 'En Proceso'),
        ('Entrevistas', 'Entrevistas'),
        ('Ofrecido', 'Ofrecido'),
        ('Rechazado', 'Rechazado'),
    ])
    technologies = models.CharField(max_length=100, choices=[
        ('Java', 'Java'),
        ('Python', 'Python'),
        ('Javascript', 'Javascript')
    ])
    salary_benefits = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.company} | {self.position}"
