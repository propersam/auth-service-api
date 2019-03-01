from rest_framework import serializers
from users import models


class OrganisationSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Organisation
		fields = ('id', 'name', 'size', 'address', 'logo', 'email', 'website',
		'about_company', 'created_at', 'updated_at')


class RoleSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Role
		fields = ('id', 'name', 'desc', 'created_at', 'updated_at')

class UserSerializer(serializers.ModelSerializer):
	roles = serializers.SlugRelatedField(
		many=True,
		slug_field='name',
		queryset = models.Role.objects.all(),
		allow_null= True,
	)

	organisation_id = serializers.PrimaryKeyRelatedField(
		many = False,
		queryset = models.Organisation.objects.all(),
		read_only = False
	)

	class Meta:
		model = models.Users
		fields = ('id', 'firstName', 'lastName', 'username', 'email', 'contact_num', 'roles', 'organisation_id', )