""" report like pages for app models and data """

# from django.conf import settings
# from django.shortcuts import render
# from django.views.generic import View
from handyhelpers.views.report import AnnualTrendView, AnnualStatView, AnnualProgressView
# from handyhelpers.views.report import get_colors


# import models
# from {{ app_name }}.models import ()


class StoreMgrAnnualProgressView(AnnualProgressView):
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


class StoreMgrAnnualStatView(AnnualStatView):
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


class StoreMgrAnnualTrendView(AnnualTrendView):
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
