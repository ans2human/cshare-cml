from django.urls import path
from .views import ContactViewset, UserViewset, CustomAuthToken
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'contacts', ContactViewset, base_name="contacts")
router.register(r'users', UserViewset)
urlpatterns = router.urls

urlpatterns += [
    path('login/', CustomAuthToken.as_view())
]
