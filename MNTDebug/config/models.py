from django.core.validators import RegexValidator
from django.db import models

# from gender.models import GenderModel
# from marital_status.models import MaritalStatusModel
# from religion.models import ReligionModel

# Create your models here.


class UserModel(models.Model):
    phone_regex = RegexValidator(
        regex=r'^01[13-9]\d{8}$',
        message="Phone number must be this format: '01*********'"
    )
    phone_number = models.CharField(
        validators=[phone_regex], max_length=11, unique=True)
    pin = models.CharField(max_length=255, null=True)
    amount = models.FloatField(default=0)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    # gender = models.ForeignKey(
    #     GenderModel, related_name='user_gender',
    #     on_delete=models.DO_NOTHING, null=True, blank=True
    # )
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True)
    nid = models.CharField(max_length=255, null=True, blank=True)
    # religion = models.ForeignKey(
    #     ReligionModel, on_delete=models.DO_NOTHING, null=True, blank=True)
    # marital_status = models.ForeignKey(
    #     MaritalStatusModel, on_delete=models.DO_NOTHING, null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True)
    occupation = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.phone_number}"

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'user'
