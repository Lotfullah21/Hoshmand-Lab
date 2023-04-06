from django.http import HttpResponse


def handler404(request, exception):
    return HttpResponse("<h1>Error 404, the page is not found</h1>")