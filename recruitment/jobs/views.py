from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import RequestContext, loader

from django.contrib.auth.models import User
from jobs.models import Cities, JobTypes, Job


def joblist(request):
    job_list = Job.objects.order_by('job_type')
    context = {'job_list': job_list}
    for job in job_list:
        job.city_name = Cities[job.job_city][1]
        job.type_name = JobTypes[job.job_type][1]
    return render(request, 'joblist.html', context)


def detail(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
        job.city_name = Cities[job.job_city][1]
        # logger.info('job retrieved from db :%s' % job_id)
    except Job.DoesNotExist:
        return render(request, 'job.html', {'job': None})
    return render(request, 'job.html', {'job': job})
