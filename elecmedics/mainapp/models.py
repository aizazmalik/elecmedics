from django.db import models

class Patient(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    patient_name = models.CharField(max_length=255)
    cnic = models.BigIntegerField(unique=True)
    father_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=20)
    history = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_name

    class Meta:
        verbose_name = 'New Patient'
        verbose_name_plural = 'New Patient'

class Prescription(models.Model):
    token_number = models.AutoField(primary_key=True, unique=True)
    # token_number = models.AutoField(unique=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    prescription = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription for {self.patient_id} ({self.token_number})"

    class Meta:
        verbose_name = 'Existing Patient'
        verbose_name_plural = 'Existing Patient'
