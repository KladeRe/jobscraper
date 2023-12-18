from duuni_app.models import JobListing
from django.http import JsonResponse, HttpResponse
import json
from duuni_scraper.languages import programming_languages
# Create your views here.


def get_all(request):
    job_listings = JobListing.objects.all()
    data = []

    language_entry = {
        "all_languages": programming_languages,
    }

    data.append(language_entry)

    for job in job_listings:
        entry = {
            "title": job.title,
            "url": job.url,
            "programming_languages": [language.name for language in job.programming_languages.all()]
        }
        data.append(entry)
    return JsonResponse(data, safe=False)



