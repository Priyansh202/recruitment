from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Jobs

def home(request):
    query = request.GET.get('q')
    employment_type = request.GET.get('employment_type')
    company_name = request.GET.get('company_name')

    jobs = Jobs.objects.all()

    if query:
        jobs = jobs.filter(title__icontains=query)
    
    if employment_type:
        jobs = jobs.filter(employment_type=employment_type)
    
    if company_name:
        jobs = jobs.filter(company_name=company_name)

    paginator = Paginator(jobs, 5)  # Show 10 jobs per page
    page = request.GET.get('page')
    jobs = paginator.get_page(page)
    
    return render(request, 'app/home.html', {'jobs': jobs, 'query': query, 'employment_type': employment_type, 'company_name': company_name})
