from django.db import models

# Create your models here.

class App(models.Model):
    level = [("Undergraduate","UNDERGRADUATE"),
            ("Postgraduate", "POSTGRADUATE"),
            ("Phd", "PhD")]
    categories = [("None", "NONE"),
                 ("National","NATIONAL"),
                 ("International", "INTERNATIONAL")]
    name = models.CharField(max_length=64, help_text = "Enter Name of Scholarship")
    providedby = models.CharField(max_length=64, verbose_name = "Provided By", help_text="Enter name of sponsor or organization")
    eligibilitycriteria = models.CharField(max_length=512, verbose_name = "Eligibility Criteria", help_text="Enter Eligibility Criteria")
    exam = models.CharField(max_length=64, help_text="Enter if any exam is required")
    scholarshipamount = models.CharField(max_length = 18, verbose_name = "Scholarship Amount")
    applicationfees = models.CharField(max_length = 18, verbose_name = "Application Fees")
    deadline = models.CharField(max_length=32)
    link = models.CharField(max_length=128, help_text="Enter 404 if not available")
    category = models.CharField(choices=categories, blank=True, verbose_name = "Category", max_length=200, null=True)
    levels = models.CharField(choices=level, blank=True, verbose_name = "Levels", max_length=200, null=True)
    def __str__(self):
        return f"{self.id}: {self.name} awarded by {self.providedby} requires {self.eligibilitycriteria}, {self.category} citizenship and {self.exam} can get you upto {self.scholarshipamount} and application fees of {self.applicationfees} must be paid until {self.deadline}"


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=256)
    message = models.TextField(max_length=4098)

    def __str__(self):
        return self.email
