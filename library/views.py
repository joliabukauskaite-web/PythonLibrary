from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'zmones': ['Tomas', 'Rokas', 'Ona'],
    }
    return render(request, template_name='index.html', context=context)

