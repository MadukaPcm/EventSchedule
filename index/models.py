from django.db import models
from django.contrib.auth.models import AbstractUser
from geopy.distance import geodesic

# Create your models here.
class User(AbstractUser, models.Model):
    email = models.EmailField(unique = True)

class Choices(models.Model):
    choice = models.CharField(max_length=5000)
    is_answer = models.BooleanField(default=False)

class Questions(models.Model):
    question = models.CharField(max_length= 10000)
    question_type = models.CharField(max_length=20)
    required = models.BooleanField(default= False)
    answer_key = models.CharField(max_length = 5000, blank = True)
    score = models.IntegerField(blank = True, default=0)
    feedback = models.CharField(max_length = 5000, null = True)
    choices = models.ManyToManyField(Choices, related_name = "choices")

class Answer(models.Model):
    answer = models.CharField(max_length=5000)
    answer_to = models.ForeignKey(Questions, on_delete = models.CASCADE ,related_name = "answer_to")

class Form(models.Model):
    code = models.CharField(max_length=30)
    title = models.CharField(max_length=200)
    cover_photo = models.ImageField(upload_to="ImageStore", default="")
    description = models.CharField(max_length=10000, blank = True)
    creator = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "creator")
    background_color = models.CharField(max_length=20, default = "#d9efed")
    text_color = models.CharField(max_length=20, default="#272124")
    collect_email = models.BooleanField(default=True)
    authenticated_responder = models.BooleanField(default = False)
    edit_after_submit = models.BooleanField(default=False)
    confirmation_message = models.CharField(max_length = 10000, default = "Your response has been recorded.")
    is_quiz = models.BooleanField(default=False)
    allow_view_score = models.BooleanField(default= True)
    createdAt = models.DateTimeField(auto_now_add = True)
    updatedAt = models.DateTimeField(auto_now = True)
    questions = models.ManyToManyField(Questions, related_name = "questions")

class EventLocation(models.Model):
    event = models.ForeignKey(Form, related_name="event_form", blank=True,null=True,on_delete=models.CASCADE)
    event_location_name = models.CharField(max_length=100, blank=True,null=True)
    event_latitude = models.CharField(max_length=50,null=True,blank=True)
    event_longtude = models.CharField(max_length=50,null=True,blank=True)
    

class PhoneNumbers(models.Model):
    phone = models.CharField(max_length=30, unique=True)
    form = models.ForeignKey(Form,on_delete=models.CASCADE)


class MessageSent(models.Model):
    message = models.CharField(max_length=10000)
    form = models.OneToOneField(Form, on_delete=models.CASCADE)

class Responses(models.Model):
    response_code = models.CharField(max_length=20)
    response_to = models.ForeignKey(Form, on_delete = models.CASCADE, related_name = "response_to")
    responder_ip = models.CharField(max_length=30)
    responder = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "responder", blank = True, null = True)
    responder_email = models.EmailField(blank = True)
    response = models.ManyToManyField(Answer, related_name = "response")
    
    def calculate_distance(self):
        home_location = HomeLocation.objects.filter(response=self).first()
        if home_location and home_location.home_latitude and home_location.home_longtude:
            event_location = self.response_to.event_form.first()
            if event_location and event_location.event_latitude and event_location.event_longtude:
                home_coords = (float(home_location.home_latitude), float(home_location.home_longtude))
                event_coords = (float(event_location.event_latitude), float(event_location.event_longtude))
                distance = geodesic(home_coords, event_coords).meters
                return distance
        return None
    
class HomeLocation(models.Model):
    response = models.ForeignKey(Responses, related_name="event_form_response", blank=True,null=True,on_delete=models.CASCADE)
    home_location_name = models.CharField(max_length=100, blank=True,null=True)
    home_latitude = models.CharField(max_length=50,null=True,blank=True)
    home_longtude = models.CharField(max_length=50,null=True,blank=True)
    
   