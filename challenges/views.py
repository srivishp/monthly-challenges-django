from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenge_list = {
    "january": "Challenge 1 for Jan",
    "february": "Challenge 2 for Feb",
    "march": "Challenge 3 for Mar",
    "april": "Challenge 4 for Apr",
    "may": "Challenge 5 for May",
    "june": "Challenge 6 for Jun",
    "july": "Challenge 7 for Jul",
    "august": "Challenge 8 for Aug",
    "september": "Challenge 9 for Sep",
    "october": "Challenge 10 for Oct",
    "november": "Challenge 11 for Nov",
    "december": "Challenge 12 for Dec",
}
# Create your views here.

# > In this function we are dynamically creating a list using HTML, reverse functions & f-strings.
# We should also add this index function the urls.py
# * The below HTML will be rendered on localhost:8000/challenge


def index(request):

    list_items = ""
    months = list(monthly_challenge_list.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'> {capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


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
    # > Using the reverse function and a named URL to avoid hardcoding the URL everywhere
    # #The reverse function also has args[] that can hold the number of dynamic segments in the URL. Here we have only one, which is redirect_month
    # Hardcoded like this: return HttpResponseRedirect("/challenges/" + redirect_month)
    # The line below generates --> /challenges/january
    redirect_path = reverse("month-challenge", args=[redirect_month])
    # ? The reverse function figures out how to properly build the full URL path taking into account any prefixes(/challenges/) that the path already has
    return HttpResponseRedirect(redirect_path)


def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenge_list[month]
        response_data = f"<h1>Challenge for this month is: {challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>404: Month not found</h1>")
