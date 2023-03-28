import uuid
from stdimage import StdImageField
from django.db import models


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    created = models.DateField('Criação', auto_now_add=True)
    modified = models.DateField('Modificado', auto_now=True)

    class Meta:
        abstract = True


class Job(Base):
    job = models.CharField('Job', max_length=50, blank=False, null=False)
    salary = models.DecimalField('Salary', max_length=12, decimal_places=2, max_digits=10, default=0)

    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
        ordering = ['id']

    def __str__(self):
        return self.job


class Employee(Base):
    name = models.CharField('Name', max_length=500, null=False, blank=False)
    job = models.ForeignKey('api1.job', verbose_name='Job', on_delete=models.CASCADE)
    image = StdImageField(
        'Image', upload_to=get_file_path,
        variations={'thumb': {'width': 480, 'height': 480, 'crop': True}}
    )
    active = models.BooleanField('Active', default=False)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'
        ordering = ['id']

    def __str__(self):
        return f'{self.name} work as {self.job}'


