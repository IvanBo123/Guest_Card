from django.shortcuts import render
from django.views import View
from .models import *

# Create your views here.


class MainPageView(View):
    def get(self, request):
        about_us = About_usInfo.objects.all()
        statistic = StatisticInfo.objects.all()
        types = Type_ofCompanions.objects.all()
        companions = Companions.objects.all()
        social_hubs = Social_Hubs.objects.all()
        return render(request, "guest_main/main.html", {
            "about_us": about_us,
            "statistic": statistic,
            "types": types,
            "companions": companions,
            "social_hubs": social_hubs,
            "range": range(1, 6),
        })
