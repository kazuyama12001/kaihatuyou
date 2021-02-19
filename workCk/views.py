from django.shortcuts import render, get_object_or_404
from .models import Work
from django.utils import timezone

# Create your views here.
Work.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

def work_ck(request):
#    work = Work.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    work = Work.objects.all()
    return render(request, 'workCk/work_ck.html',  {'work': work})

def work_detail(request, pk):
    work = get_object_or_404(Work, pk=pk)
    return render(request, 'workCk/work_detail.html',  {'work': work})