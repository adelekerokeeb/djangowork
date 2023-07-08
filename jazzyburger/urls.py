from django.urls import path
from jazzyburger.views import (
    ProductView,
    ProductDetailView,
    ProductUpdateView,
    AddProductView,
    CreateUserView,
    ProductDeleteView,
)
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', ProductView.as_view(), name='home'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='detail'),
    path('detail/<int:pk>/update', ProductUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/delete/', ProductDeleteView.as_view(), name = 'delete'),
    path('addproduct/', AddProductView.as_view(), name='addproduct'),
    path('adduser/', CreateUserView.as_view(), name='adduser'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

# Setting for media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
