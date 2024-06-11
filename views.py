from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import ScrapeJob, ScrapeTask
from .serializers import ScrapeJobSerializer
from .tasks import scrape_coin_data
import uuid

class TaskManagerViewSet(viewsets.ViewSet):

    def start_scraping(self, request):
        coins = request.data
        if not all(isinstance(coin, str) for coin in coins):
            return Response({"error": "Invalid input"}, status=status.HTTP_400_BAD_REQUEST)

        job_id = str(uuid.uuid4())
        job = ScrapeJob.objects.create(job_id=job_id)

        for coin in coins:
            ScrapeTask.objects.create(job=job, coin=coin)
            scrape_coin_data.delay(job_id, coin)

        return Response({"job_id": job_id}, status=status.HTTP_202_ACCEPTED)

    def scraping_status(self, request, job_id=None):
        try:
            job = ScrapeJob.objects.get(job_id=job_id)
        except ScrapeJob.DoesNotExist:
            return Response({"error": "Job not found"}, status=status.HTTP_404_NOT_FOUND)

        job_serializer = ScrapeJobSerializer(job)
        return Response(job_serializer.data)
