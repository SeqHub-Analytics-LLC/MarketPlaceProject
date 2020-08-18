from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

jobs = [
    {
        'company': 'SeqHub Analytics',
        'title': 'Backend Developer needed!!!',
        'content': 'We are looking for a young and committed backend developer who is familiar with the following web technologies: HTML, CSS, javascript, php(Laravel), python(django) ',
        'date_posted': 'August 7, 2020'

    },
    {
        'company': 'Data Science Nigeria',
        'title': 'Community Manager urgently needed.',
        'content': 'Our team is need of a young recent graduate who can manage the operations of managing our large community in Africa, spanning through west africa. We are looking for skills within the social space so a degree in the humanities would be an advantage',
        'date_posted': 'August 7, 2020'

    }
]


def home(request):
    context = {
        'jobs': jobs
    }
    return render(request, 'jobPost/home.html', context)


def about(request):
    return render(request, 'jobPost/about.html', {'title': 'About'})
