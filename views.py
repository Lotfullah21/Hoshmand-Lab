from django.shortcuts import render

# Create your views here.

def courses(request):
    courses = {
        "mains":[
        {"name":"Artificial Intelligence","price":"$10"},
        {"name":"Deep Learning","price":"$10"},
        {"name":"Machine Learning","price":"$10"},
        {"name":"Reinforcement Learnig","price":"$32"},
        {"name":"Data Structures","price":"$12"},
        {"name":"Algorithms","price":"$21"}

        ]}
    return render(request,"about.html",courses)

    
    














#     cotext = {"about_me":"I am Lotfullah Andishmand, with all the obstacles and temporary friction, I believe I can prevail, because god says he loves the ones who do \
#             useful staff and bring something new to the table that can lead to positive changes in a society"}
#     return render(request, "about.html",cotext)