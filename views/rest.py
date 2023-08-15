""" DRF viewsets for applicable app models """

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_flex_fields import is_expanded
from handyhelpers.drf_permissions import InAnyGroup

# import models
# from {{ app_name }}.models import ()

# import serializers
# from {{ app_name }}.serializers import ()

# import filtersets
# from {{ app_name }}.filtersets import ()
