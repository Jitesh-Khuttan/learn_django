from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
import json

# Create your views here.

monthly_challenges = {
    "january": "Do 20 push ups daily!",
    "february": "Walk for 20 minutes daily!",
    "march": "Go to gym for an hour - 5 days a week!",
    "april": "Eat no fast food!",
    "may": "Eat no meat!",
    "june": "Do Competitve Programming for an hour daily!",
    "july": "Learn Django for an hour daily!",
    "august": "Learn Kubernetes for an hour daily from Udemy!",
    "september": "Do AWS certification!",
    "october": "Take 2 vacations!",
    "november": "Plant 100 trees.",
    "december": None
}

def index(request):
    all_months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", context={
        "months": all_months
    })

def monthly_challenge_by_number(request, month):
    all_months = list(monthly_challenges.keys())
    if month < 0 or month > len(all_months):
        return HttpResponseNotFound("Month not supported!")

    redirect_month = all_months[month-1]
    redirect_url = reverse("challenge-by-month-name", args=(redirect_month, ))
    return HttpResponseRedirect(redirect_url)



def monthly_challenge(request, month):
    current_challenege = monthly_challenges.get(month.lower(), "Month not supported!")
    return render(request, "challenges/challenge.html", context={
        "month": month,
        "challenge_text": current_challenege
    })
