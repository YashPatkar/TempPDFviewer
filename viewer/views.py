from django.shortcuts import render
import random

def generate_code():
    return ''.join(random.choices('0123456789', k=5))

# Create your views here.
def index(request):
    option = False
    if(request.method == 'POST'):
        option = True
        global code
        code = generate_code()
        return render(request, 'viewer/index.html', {'option': option, 'code': code})
    return render(request, 'viewer/index.html', {'option': option})

# def pdf(request):
#     return render(request, 'viewer/pdf.html', {'code': code})