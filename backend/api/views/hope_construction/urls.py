import api.views as apiViews
from rest_framework import routers
from django.urls import path

router = routers.SimpleRouter(trailing_slash=False)

# router.register(r'test', apiViews.TestViewSet, basename='test')

router.register(r'about', apiViews.AboutHCViewSet,
    basename='about-us'
)
router.register(r'contact-info', apiViews.FilesHCViewSet,
    basename='contact-info'
)
router.register(r'files', apiViews.FilesHCViewSet,
    basename='files'
)
router.register(r'gallery', apiViews.GalleryHCViewSet,
    basename='gallery'
)
router.register(r'message', apiViews.MessageHCViewSet,
    basename='message'
)
router.register(r'services', apiViews.ServiceHCViewSet,
    basename='services'
)
router.register(r'sliders', apiViews.SliderHCViewSet,
    basename='sliders'
)
router.register(r'subscribers', apiViews.SubscriberHCViewSet,
    basename='subscribers'
)
router.register(r'testimonials', apiViews.TestimonialHCViewSet,
    basename='testimonials'
)
router.register(r'banner', apiViews.BannerHCViewSet,
    basename='banner'
)
router.register(r'bundled-data', apiViews.BundledHCViewSet,
    basename='bundled-data'
)
urlpatterns = router.urls

# URLconf
urlpatterns = [
    # path(
    #     'register', 
    #     apiViews.ClientAccountRegisterViewSet.as_view(),
    #     name='clients->register'
    # ),

] + router.urls
