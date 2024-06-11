from django.db import models

class ScrapeJob(models.Model):
    job_id = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ScrapeTask(models.Model):
    job = models.ForeignKey(ScrapeJob, related_name="tasks", on_delete=models.CASCADE)
    coin = models.CharField(max_length=255)
    output = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
