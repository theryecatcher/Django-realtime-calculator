from django.shortcuts import render

from .forms import CalculationForm
from .models import Calculation
from django.http import HttpResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def index(request):
    if request.method == 'POST':
        form = CalculationForm(request.POST)
        if form.is_valid():
            # pass  # does nothing, just trigger the validation
            calc = Calculation()
            calc.expression = (form.cleaned_data['expression'])
            calc.result = eval(calc.expression)
            calc.save()

            layer = get_channel_layer()
            async_to_sync(layer.group_send)('group_calci', {
                'type': 'calc_message',
                'message': '{} = {}'.format(calc.expression, calc.result)
            })

            calculations = Calculation.objects.order_by('-pk')[:10]
            return render(request, 'calculator/index.html',
                        {'form': form, 'calculations': calculations})

        else:
            return render(request, 'calculator/index.html',
                        {'form': form, 'errors': form.errors})
    else:
        form = CalculationForm()
        return render(request, 'calculator/index.html', {'form': form, 'errors': form.errors})