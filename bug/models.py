from django.db import models
import re

class UserManager(models.Manager):
    def validator(self, postData):
        errors={}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData["first_name"]) < 2:
            errors["first_name"] = "Is that really your name shortstack?"
        if len(postData["last_name"]) < 2:
            errors["last_name"] = "extendo nameo"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Um I can't reach ya there!"
        if len(postData["password"]) < 8:
            errors["password"] = "Not secure enough ya dolt. Might want to make it longer"
        if postData["confirm_password"] != postData["password"]:
            errors["confirm_password"] = "Now I know why your S/O dresses you! You're terrible at matching!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=255)
    admin = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()










class TicketManager(models.Manager):
    def ticket_validator(self, postData):
        errors={}
        if len(postData["ticket_name"]) < 3:
            errors["name"] = "A ticket name must consist of at least 3 characters"
        if postData["app"] == 'null':
            errors["app"] = "Please select an app"
        if len(postData["description"]) < 10:
            errors["description"] = "Describe the problem"
        return errors

class Ticket(models.Model):
    name = models.CharField(max_length=45)
    app = models.CharField(max_length=45)
    description = models.TextField()
    creator = models.ForeignKey(User, related_name="submitter", on_delete = models.CASCADE)
    action_phase = models.IntegerField(default=0)
    vote = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def vote_vote(self):
        self.vote+=1

    objects = TicketManager()