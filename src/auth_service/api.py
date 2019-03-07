from rest_framework import routers
from users import views as user_views

router = routers.DefaultRouter()
router.register(r'roles', user_views.RoleViewSet, base_name='roles')
router.register(r'organisations', user_views.OrganisationViewSet, base_name='organisations')
router.register(r'users', user_views.UserViewSet, base_name='users')