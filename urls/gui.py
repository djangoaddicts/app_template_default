from django.urls import path
from {{ app_name }}.views import gui
from {{ app_name }}.views import report


urlpatterns = [
    # GUI views
    path("", gui.Index.as_view(), name=""),
    path("index", gui.Index.as_view(), name="index"),
    path("default", gui.Index.as_view(), name="default"),
    path("home", gui.Index.as_view(), name="home"),

    # list views
    # path("list_mymodels/", gui.ListMymodels.as_view(), name="list_mymodels"),
    
    # detail views
    # path("detail_mymodel/<int:pk>", gui.DetailMymodel.as_view(), name="detail_mymodel"),

    # report views
    path("dashboard/", report.{{ app_name|title }}Dashboard.as_view(), name="dashboard"),
    path("annual_progress/", report.{{ app_name|title }}AnnualProgressView.as_view(), name="annual_progress"),
    path("annual_stats/", report.{{ app_name|title }}AnnualStatView.as_view(), name="annual_stats"),
    path("annual_trends/", report.{{ app_name|title }}AnnualTrendView.as_view(), name="annual_trends"),

]
    