from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="news/images/")
    content = models.TextField()
    date = models.DateTimeField()


class OurTeam(models.Model):
    image = models.ImageField(upload_to="OurTeam/images/")
    full_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    facebook_url = models.URLField()
    twitter_url = models.URLField()
    instagram_url = models.URLField()
    date = models.DateTimeField()


class Teacher(models.Model):
    name = models.CharField(max_length=200)


class Category(models.Model):
    image = models.ImageField(upload_to="category/images/")
    name = models.CharField(max_length=200)


class Course(models.Model):
    image = models.ImageField(upload_to="Course/images/")
    full_name = models.CharField(max_length=200)
    price = models.PositiveSmallIntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class HomeCarusel(models.Model):
    bg_img = models.ImageField(upload_to="Home_carusel/images/")
    min_content = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200, null=True, blank=True)
    bt1_name = models.CharField(max_length=200)
    bt1_url = models.CharField(max_length=200)
    btn2_name = models.CharField(max_length=200)
    btn2_url = models.CharField(max_length=200)


class ServiceStart(models.Model):
    icon = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    content = models.CharField(max_length=200)


class AboutStartSkills(models.Model):
    name = models.CharField(max_length=200)


class AboutStart(models.Model):
    min_content = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    btn_name = models.CharField(max_length=200)
    btn_url = models.CharField(max_length=200)
    skills = models.ManyToManyField(AboutStartSkills)
    image = models.ImageField(upload_to="AboutStart/images/")

class TestimonialItem(models.Model):
    image = models.ImageField("TestimonialItems/images/")
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    content = models.TextField()

class Testimonial(models.Model):
    min_content = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    items = models.ManyToManyField(TestimonialItem)

class ContactInformation(models.Model):
    image = models.ImageField("ContactInformation/images/")
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)

class ContactMessages(models.Model):
    name = models.CharField(max_length=200)
    fullname = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    content = models.TextField()


class Contact(models.Model):
    min_title = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    min_content = models.CharField(max_length=200)
    contact = models.ManyToManyField(ContactInformation)
    contact_map = models.TextField()
    contact_messages = models.ForeignKey(ContactMessages, on_delete=models.CASCADE)

class FooterIcon(models.Model):
    icon = models.CharField(max_length=200)

class FooterIcons(models.Model):
    icons = models.ManyToManyField(FooterIcon)