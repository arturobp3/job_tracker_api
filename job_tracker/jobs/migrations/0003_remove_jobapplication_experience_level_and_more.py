# Generated by Django 5.1.2 on 2024-10-29 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_remove_jobapplication_contact_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='experience_level',
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='status',
            field=models.CharField(choices=[('Guardada', 'Guardada'), ('Enviado', 'Enviado'), ('En Proceso', 'En Proceso'), ('Entrevistas', 'Entrevistas'), ('Ofrecido', 'Ofrecido'), ('Rechazado', 'Rechazado')], max_length=50),
        ),
    ]