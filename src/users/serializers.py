from rest_framework import serializers
from users import models
from django.contrib.auth.hashers import make_password


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
	
				
	class Meta:
		model = models.UserProfile
		fields = ('id', 'firstName','password' ,'lastName', 'username','password', 'email', 'contact_num', 'roles', 'organisation')
		extra_kwargs = {'password': {'write_only': True}}


	def create(self, validated_data):
		password = validated_data.pop('password')
		s_roles = validated_data.pop('roles') # taking out roles data
		user = self.Meta.model(**validated_data)
		if password is not None:
			user.set_password(password)
		user.save()
		if s_roles is not None:
			user.roles.set(s_roles) # setting many2many relationship for user and roles
		return user
	
	def update(self, instance, validated_data):
		s_roles = None
		for attr, value in validated_data.items():
			if attr == 'password':
				instance.set_password(value)
			elif attr == 'roles':
				instance.roles.set(value)
			else:
				setattr(instance, attr, value)
		
		instance.save()
			
		return instance