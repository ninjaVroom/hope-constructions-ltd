from rest_framework import routers
from django.urls import path, include

router = routers.SimpleRouter(trailing_slash=False)

# print({"router.urls": router.urls})

urlpatterns = router.urls

# URLconf
urlpatterns = [
    path('', include('rest_framework.urls')),
    path('', include('api.views.login.urls')),
    path('hope-construction/', include('api.views.hope_construction.urls')),
]+router.urls
