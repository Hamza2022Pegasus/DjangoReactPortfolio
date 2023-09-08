"""Module to create models for DB"""
from django.db import models

# Create your models here.
class IntroBannerHero(models.Model):
    """Class based model for intro banner"""
    welcomeText = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Text to welcome users"
        )
    name = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Your Full Name"
        )
    job_title = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="Job Title"
    )
    introPara = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="Introduction Paragraph"
    )
    image= models.CharField(
        max_length=30,
        blank=True,
        null=True,
        verbose_name="Google Drive id only for image"
    )
    emailAddress = models.CharField(
        verbose_name="Your personal email to recieve emails on",
        blank=True,
        null=True,
        max_length=50,
    )
    linkToCV = models.CharField(
        verbose_name="URL link for CV",
        blank=True,
        null=True,
        max_length=50,
    )

    class Meta:
        """Class meta for this model"""
        verbose_name = "Intro Banner Text"

    def __str__(self):
        """function to define name of class"""
        return str(self.name)

class AboutMeSeciton(models.Model):
    """Class based model for about me section"""
    name= models.CharField(verbose_name="Title for About me Section",max_length=30)
    subTitle = models.CharField(verbose_name="Subtitle",max_length=200,blank=True,null=True)
    desctiprion = models.CharField(verbose_name="Description",max_length=200,blank=True,null=True)

    class Meta:
        """Class meta for this model"""
        verbose_name = "About me Section Text"

    def __str__(self):
        """Function to define name of class"""
        return str(self.name)

class Services(models.Model):
    """Class based model for services"""
    image = models.CharField(verbose_name="Google drive image id",
                             max_length=100,blank=True,null=True)
    name = models.CharField(verbose_name="Name of offered Service",
                            blank=True,null=True,max_length=50)
    backgroundIcon = models.CharField(max_length=50,null=True,blank=True,)
    description = models.CharField(max_length=200,blank=True,null=True,
                                   verbose_name="Description for the service")

    class Meta:
        """Class meta for this model"""
        verbose_name = "Services by You"

    def __str__(self):
        """Function to define name of class"""
        return str(self.name)

class Technologies(models.Model):
    """Class based model for technologies"""
    experienceLevel = (
        ("Beginner","Beginner"),
        ("Junior","Junior"),
        ("Intermediate","Intermediate"),
        ("Experienced","Experienced"),
        )
    logo = models.CharField(max_length=200,blank=True,null=True,verbose_name="Technology Icon Image:(icons8.com)")
    name = models.CharField(max_length=50,blank=True,null=True,verbose_name="Name of programming language")
    experience = models.CharField(choices=experienceLevel,blank=True,max_length=100,verbose_name="Experience Level") 

    class Meta:
        """Class meta for this model"""
        verbose_name="Technologies"

    def __str__(self):
        return str(self.name)

class Jobs(models.Model):
    """Class based model for completed Projects"""
    technology = models.CharField(max_length=50,blank=True,null=True,verbose_name="Language used for this project")
    image = models.CharField(max_length=50,blank=True,null=True,verbose_name="GDrive image id for logo")
    date =models.DateTimeField(auto_now_add=False,null=True,auto_now=True,blank=True)
    name = models.CharField(max_length=100,blank=True,null=True,verbose_name="Name of Project")
    description = models.CharField(max_length=200,blank=True,null=True,verbose_name="Description of Job")
    link = models.URLField(max_length=200,blank=True,null=True,verbose_name="Github URL of the Project")
    demo = models.URLField(max_length=200,blank=True,null=True,verbose_name="Demo Link of the Project")

    class Meta:
        """Class meta for this model"""
        verbose_name="Completed jobs"

    def __str__(self):
        return str(self.name)

class Contact(models.Model):
    """Class based model for Contact Me"""
    icon = models.CharField(max_length=100,blank=True,null=True,verbose_name="Icon eg:fa fa-light")
    info = models.CharField(max_length=100,blank=True,null=True,verbose_name="Contact Info (eg: johndoe2@gmail.com)")
    name = models.CharField(max_length=100,blank=True,null=True,verbose_name="Contact Name ( this whole section is flawed)")

    class Meta:
        """Class meta for this model"""
        verbose_name="Contact Me section"

    def __str__(self):
        return str(self.name)

class SMLinks(models.Model):
    """Class based model for Social media Links"""
    name = models.CharField(max_length=100,blank=True,null=True)
    link = models.URLField(max_length=100,blank=True,null=True)
    icon = models.CharField(max_length=50,null=True,blank=True,verbose_name="Icon eg: fa fa-light")

    class Meta:
        """Class meta for this model"""
        verbose_name="Social Media Links Section"

    def __str__(self):
        return str(self.name)
