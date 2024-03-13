from django.shortcuts import render, redirect
import requests


def exchange(request):
    response = requests.get(
        url='API_TOKEN from ExchangeRate-API').json()
    currency = response.get('conversion_rates')

    if request.method == 'GET':

        context = {
            'currency': currency,
            'output_sum': request.session.pop('output_sum', None)

        }
        return render(request=request, template_name='exchange/index.html', context=context)

    if request.method == 'POST':
        input_sum = float(request.POST.get('input_Sum'))
        from_cur = request.POST.get('from_cur')
        to_cur = request.POST.get('to_cur')

        output_sum = round(
            input_sum / currency[from_cur] * currency[to_cur], 2)

        request.session['output_sum'] = output_sum

        return redirect(request.path)
