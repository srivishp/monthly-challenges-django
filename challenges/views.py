from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
# Create your views here.

monthly_challenge_list = {
    "january": "Challenge 1",
    "february": "Challenge 2",
    "march": "Challenge 3",
    "april": "Challenge 4",
    "may": "Challenge 5",
    "june": "Challenge 6",
    "july": "Challenge 7",
    "august": "Challenge 8",
    "september": "Challenge 9",
    "october": "Challenge 10",
    "november": "Challenge 11",
    "december": "Challenge 12",
}

# In this function, we are forwarding/redirecting the numbers of months to the challenges
# * The month in the argument will be the index of the above dict, because since Python 3.6 all dicts are now ordered by default.
# We're taking advantage of that.


def monthly_challenges_by_number(request, month):
    months = list(monthly_challenge_list.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid Month")
    # using the month as the index and months as the list,
    # deducting 1 because index starts at 0
    redirect_month = months[month-1]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenge_list[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("404: Month not found")
