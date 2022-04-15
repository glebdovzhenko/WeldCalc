from django.http import HttpResponse
from django.template import loader

import plotly.express as px

from .calculate import parabola, parabola_kwargs


def weldcalc(request):
    # setting up the template and its context
    page = loader.get_template('index.html')
    context = dict()

    # parsing the request
    try:
        params = {key: float(val) for key, val in request.GET.dict().items()}
    except Exception:
        params = parabola_kwargs
    else:
        if set(params.keys()) != set(parabola_kwargs.keys()):
            params = parabola_kwargs

    # generating data and populating the plot
    xs, ys = parabola(**params)
    context['plot'] = px.line(x=xs, y=ys, title='Parabola').to_html(full_html=False)

    # adding parameter values to the context
    context['parameters'] = tuple([{'name': key, 'value': params[key]} for key in sorted(params.keys())])

    return HttpResponse(page.render(context, request))
