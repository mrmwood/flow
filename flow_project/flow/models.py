#There are two modern ways to create a custom user
#model in Django: AbstractUser and AbstractBaseUser.
#In both cases we can subclass them to extend existing
#functionality however AbstractBaseUser requires much more work.
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager



class Role(models.Model):
  # The Role entries are managed by the system,
  # automatically created via a Django data migration.
  STUDENT = 1
  TEACHER = 2
  HOD = 3
  HOG = 4
  SLT = 5
  ADMIN = 6
  ROLE_CHOICES = (
      (STUDENT, 'student'),
      (TEACHER, 'teacher'),
      (HOD, 'Head Of Department'),
      (HOG, 'Head OF Group'),
      (SLT, 'Senior Leadership Team'),
      (ADMIN, 'admin'),
  )

  id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

  def __str__(self):
      return self.get_id_display()


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    roles = models.ManyToManyField(Role)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email



class Teacher(models.Model):
    #teacher_id = models.AutoField(primary_key=True)
    #teacher_initials = models.CharField(max_length=3, unique=True)
    custom_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

class Student(models.Model):
    #student_id = models.AutoField(primary_key=True)
    custom_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
