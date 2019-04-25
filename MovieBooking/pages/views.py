from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from pages.models import MovieDetails
# Create your views here.from django.views.generic import TemplateView


class HomePageView(View):
    template_name = 'pages/home.html'
    def get(self,request,*args,**kwargs):
        data = MovieDetails.objects.all()
        context ={
        'result' : data,
        }
        return render(request,'pages/home.html',context)
        # HttpResponse('HomePage Get View')
    def post(self,request,*args,**kwargs):
        return HttpResponse("Post Method")
    def fetchMovieDetails():
        pass
        # HttpResponse('HomePage Get View')

class BookingAction(View):
    template_name = 'pages/booking.html'

    def get(self,request,*args,**kwargs):
        return render('request',self.template_name,{})

