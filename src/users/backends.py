from users.models import UserProfile
import logging


class MyAuthBackend(object):
    def authenticate(self, email, password):    
        try:
            user = UserModel.objects.get(email=email)
            if user.check_password(password):
                return user
            else:
                return None
        except UserModel.DoesNotExist:
            logging.getLogger("error_logger").error("user with login %s does not exists " % login)
            return None
        except Exception as e:
            logging.getLogger("error_logger").error(repr(e))
            return None

    def get_user(self, user_id):
        try:
            user = UserModel.objects.get(sys_id=user_id)
            if user.is_active:
                return user
            return None
        except UserModel.DoesNotExist:
            logging.getLogger("error_logger").error("user with %(user_id)d not found")
            return None

class UserChangeForm(forms.ModelForm):
    #A form for updating users. Includes all the fields on
    #the user, but replaces the password field with admin's
    #password hash display field.
    
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = UserModel
        fields = ('email', 'password', 'username','firstName','lastName','organisation',
        'roles','contact_num','profile_pics','is_active','is_staff')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'is_active', 'is_staff')
    list_filter = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# Now register the new UserAdmin...
admin.site.register(UserModel, UserAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)