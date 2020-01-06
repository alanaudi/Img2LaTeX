from django.shortcuts import render

def _JsonResponse(data): # {{{
    return JsonResponse(data, json_dumps_params={'ensure_ascii':False}, safe=False)

    # }}}

def index(request): # {{{
    return render(request, 'index.html')
    # }}}
