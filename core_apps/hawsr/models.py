from django.db import models

from core_apps.account.models import BaseModel, User

# Create your models here.


class WORKER_TYPE(models.IntegerChoices):
    IT = 2, 'IT'
    WORKER = 5, 'Worker'
    CLEANER = 6, 'Cleaner'
    OTHER = 7, 'Other'


class Worker(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    worker_type = models.IntegerField(choices=WORKER_TYPE.choices, default=WORKER_TYPE.WORKER, db_index=True)
    is_busy = models.BooleanField(default=False, db_index=True)

    def _str_(self):
        return f'{self.user}: {self.worker_type}'


class Company(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=25, unique=True)

    def _str_(self):
        return f'{self.name}'


class Building(BaseModel):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, db_index=True)
    name = models.CharField(max_length=255, blank=True)
    floor_count = models.IntegerField(default=0, null=True)

    def _str_(self):
        return self.name or "Building"


class Office(BaseModel):
    building = models.ForeignKey(Building, on_delete=models.CASCADE, null=True, db_index=True)
    floor = models.IntegerField(default=0, db_index=True)
    number = models.IntegerField(default=0)

    def _str_(self):
        return f'{self.building} | {self.number}'


class UserOffice(BaseModel):
    Office = models.ForeignKey(Office, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def _str_(self):
        return f'{self.office}: {self.user}'
