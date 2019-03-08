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

	class Meta:
		model = models.UserProfile
		fields = ('id', 'firstName', 'lastName', 'username','password', 'email', 'contact_num', 'roles', 'organisation_id')
		extra_kwargs = {'password': {'write_only': True}}