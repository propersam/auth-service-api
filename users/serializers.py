from rest_framework import serializers
from users import models


class OrganisationSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Organisation
		fields = ('__all__')


class RoleSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Role
		fields = ('id', 'name', 'desc')

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Users
		fields = ('__all__')