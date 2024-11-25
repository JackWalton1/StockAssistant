from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def stocks(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())


def investment_form(request):
    if request.method == 'POST':
        # Process the submitted form data
        amount = request.POST.get('amount')
        term = request.POST.get('term')
        dividends = request.POST.get('dividends')
        
        context = {
            'amount': amount,
            'term': term,
            'dividends': dividends,
            'submitted': True
        }
        return render(request, 'form.html', context)

    return render(request, 'form.html', {'submitted': False})
