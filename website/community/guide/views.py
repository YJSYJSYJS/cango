from django.shortcuts import render

# Create your views here.


def guide_main(request):
    return render(request, 'base.html')


