#from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
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

	# @action(detail=True, methods=['put'], name='Change Password')
	# def change_password(self, request, pk=None):
	# 	""" Update the user's password. """
	# 	user = self.get_object()
	# 	serializer = PasswordSerializer(data=request.data)
	# 	if serialzer.is_valid():
	# 		user.set_password(serializer.data['password'])
	# 		user.save()
	# 		return Response({'status': 'password set'})
	# 	else:
	# 		return Response(serializer.errors,
	# 								status=status.HTTP_400_BAD_REQUEST)
