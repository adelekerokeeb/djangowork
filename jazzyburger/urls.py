from django.urls import path
from jazzyburger.views import ProductView, ProductDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ProductView.as_view(), name='home'),  
    path('detail/<int:pk>', ProductDetailView.as_view(), name='detail')   
]

# setting for media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)