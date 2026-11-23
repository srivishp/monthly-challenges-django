from django.urls import path
from . import views

urlpatterns = [
    # Points to the actual monthly challenges
    # > Using dynamic path here for months
    # A Django URL path converter captures dynamic segments from a URL pattern, validates their format,
    # and converts them into specific Python data types before passing them to a view.
    # ? You define them inside angle brackets using the <converter:variable_name> syntax within your urls.py file.
    path("<int:month>", views.monthly_challenges_by_number),
    # Naming a URL
    path("<str:month>", views.monthly_challenges, name="month-challenge"),

]
