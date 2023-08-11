from django.shortcuts import render
from django.views.generic import DetailView, View

from handyhelpers.permissions import InAnyGroup
from handyhelpers.views import HandyHelperIndexView, HandyHelperListPlusCreateAndFilterView

# import models
# from {{ app_name }}.models import ()

# import forms
# from {{ app_name }}.forms import ()


class Index(HandyHelperIndexView):
    """render the {{ app_name }} index page"""

    title = """{{ app_name|title }}"""
    subtitle = "Select an option below"
    item_list = [
        {
            "url": "/{{ app_name }}/dashboard",
            "icon": "fas fa-tachometer-alt",
            "title": "Dashboard",
            "description": "Dashboard for {{ app_name|title }} ",
        },
        {
            "url": "/{{ app_name }}/rest",
            "icon": "fas fa-download",
            "title": "APIs",
            "description": "List RESTful APIs for {{ app_name|title }}",
        },
    ]
    protected_item_list = [
    ]
    protected_group_name = "admin"
