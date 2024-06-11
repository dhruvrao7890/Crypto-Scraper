from rest_framework import serializers
from .models import ScrapeJob, ScrapeTask

class ScrapeTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScrapeTask
        fields = "__all__"

class ScrapeJobSerializer(serializers.ModelSerializer):
    tasks = ScrapeTaskSerializer(many=True, read_only=True)

    class Meta:
        model = ScrapeJob
        fields = "__all__"

