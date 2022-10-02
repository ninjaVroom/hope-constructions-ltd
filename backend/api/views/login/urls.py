import api.views as apiViews
from rest_framework import routers
from django.urls import path

router = routers.SimpleRouter(trailing_slash=False)

urlpatterns = router.urls

# URLconf
urlpatterns = [
    path(
        'login', 
        apiViews.UserLoginApiView.as_view(),
        name='login'
    ),
] + router.urls
