#from django.shortcuts import render
from rest_framework import viewsets
from users.serializers import UserSerializer, RoleSerializer
from users.serializers import OrganisationSerializer
from users import models

# Create your views here.
class OrganisationViewSet(viewsets.ModelViewSet):
	queryset = models.Organisation.objects.all().order_by("-updated_at")
	serializer_class = OrganisationSerializer

class RoleViewSet(viewsets.ModelViewSet):
	queryset = models.Role.objects.all().order_by("-updated_at")
	serializer_class = RoleSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = models.User.objects.all().order_by("-updated_at")
	serializer_class = UserSerializer