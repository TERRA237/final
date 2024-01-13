from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator

User = get_user_model()

class BusinessPlan(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE,null=True)
    business_name = models.CharField(max_length=255,null=True,unique=True,db_index=True)
    email = models.EmailField(null=True)
    description = models.TextField(null=True,max_length=1000)
    plan_doc = models.FileField(upload_to='media/',blank=True,validators=[FileExtensionValidator(allowed_extensions=['pdf','doc','docx'])])
    created_on = models.DateTimeField(auto_now_add=True,null=True)
    modified_on = models.DateTimeField(auto_now=True, null=True)
    business_logo = models.ImageField(null=True, upload_to='media/',blank=False)


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.business_name
    
    def get_absolute_url(self):
        return reverse("author-detail", kwargs={"pk": self.pk})