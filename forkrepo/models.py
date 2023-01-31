from django.db import models

class RepoProfile(models.Model):

    repository = models.CharField(default='gbowering/takehome',max_length=100)
    access_token = models.CharField(max_length=100)
