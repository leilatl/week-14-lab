from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    city = models.CharField(max_length=100)
    address = models.TextField()

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return '{}. {}'.format(self.id, self.name)

class Vacancy(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Vacancies"

    def __str__(self):
        return '[{}] {}'.format(self.company.name, self.name)
