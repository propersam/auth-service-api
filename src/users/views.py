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
	queryset = models.UserProfile.objects.all()
	serializer_class = UserSerializer

	def create(self, validated_data):
		user = models.UserProfile(validated_data)
		user.set_password(validated_data['password'])
		user.save()
		return user

	def update(self, instance, validated_data):
		for f in UserSerializer.Meta.fields + UserSerializer.Meta.write_only_fields:
			set_attr(instance, f, validated_data[f])
		instance.set_password(validated_data['password'])
		instance.save()
		return instance