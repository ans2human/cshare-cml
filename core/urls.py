from django.urls import path
from .views import ContactViewset, UserViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'contacts', ContactViewset, base_name="contacts")
router.register(r'users', UserViewset, base_name="users")
urlpatterns = router.urls
