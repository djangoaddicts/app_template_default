""" report like pages for app models and data """

# from django.conf import settings
from django.shortcuts import render
from django.views.generic import View
from handyhelpers.views.report import AnnualTrendView, AnnualStatView, AnnualProgressView
# from handyhelpers.views.report import get_colors

# import models
# from {{ app_name }}.models import ()


class {{ app_name|title }}Dashboard(View):
    """{{ app_name }} dashboard"""

    template_name = "{{ app_name }}/custom/dashboard.html"

    def get(self, request):
        """render dashboard for {{ app_name }} specific data"""
        context = {"title": "{{ app_name|title }} Dashboard"}
        return render(request, self.template_name, context=context)


class {{ app_name|title }}AnnualProgressView(AnnualProgressView):
    """ """
    dataset_list = [
        # dict(
        #     title="Model",
        #     queryset=Model.objects.all(),
        #     dt_field="created_at",
        #     icon=Model.get_icon(),
        #     list_view="/storemgr/list_models",
        # ),

    ]


class {{ app_name|title }}AnnualStatView(AnnualStatView):
    """ """
    dataset_list = [
        # dict(
        #     title="Model",
        #     queryset=Model.objects.all(),
        #     dt_field="created_at",
        #     icon=Model.get_icon(),
        #     list_view="/storemgr/list_models",
        # ),
    ]


class {{ app_name|title }}AnnualTrendView(AnnualTrendView):
    """ """
    dataset_list = [
        # dict(
        #     title="Model",
        #     queryset=Model.objects.all(),
        #     dt_field="created_at",
        #     icon=Model.get_icon(),
        #     list_view="/storemgr/list_models",
        # ),
    ]
