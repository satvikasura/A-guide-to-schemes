from django.db import models

# Create your models here.


class scheme_details(models.Model):
    name=models.CharField(max_length=100)
    department=models.CharField(max_length=30)
    description=models.TextField()
    eligibility_criteria=models.TextField()
    check_link=models.TextField()
    apply_link=models.TextField()
    website_link=models.TextField()

    def __str__(self):
        return self.name