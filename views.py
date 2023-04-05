from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse

def url_response(request):
    path = request.path
    response = HttpResponse("This is working very fine")
    path = request.path
    method = request.method
    scheme = request.scheme
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    header_response = HttpResponse()
    header_response.headers['Location'] = "Hyderabad"
    message = f" path {path}\n\
       <br> method {method}\n\
           <br> scheme {scheme}\n\
              <br>  address {address}\n\
                 <br>   path_informatin {path_info}\n\
                    <br>    user agent {user_agent}\n\
                    <br> response {header_response.headers}\n\
                        "
    return HttpResponse(message,content_type='text/html',charset='utf-8')