from django.shortcuts import render
from .models import job
from django.core.paginator import Paginator


# Create your views here.
def job_list(request):
    job_list = job.objects.all()

    paginator = Paginator(job_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'jobs': page_obj}
    return render(request, 'job/job_list.html', context)


def job_detail(request, id):
    job_detail = job.objects.get(id=id)
    context = {'jobs': job_detail}
    return render(request, 'job/job_detail.html', context)
