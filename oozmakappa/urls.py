from django.urls import path, include

from django.contrib import admin
from django.urls import path, include

admin.autodiscover()

from rest_framework.routers import DefaultRouter
from products.views import ProductsViewSet
from users.views import UsersViewSet, OrdersViewSet, AddressViewSet, AddressUserViewSet

from products import views as products_view

router = DefaultRouter()
router.register(r'products', ProductsViewSet)
router.register(r'users', UsersViewSet)
router.register(r'orders', OrdersViewSet)
router.register(r'address', AddressViewSet)
router.register(r'addressusers', AddressUserViewSet)

urlpatterns = router.urls

urlpatterns += [
    #path("products/", products_view.allProducts, name='allProducts'),
    #path("products/<int:id>/", products_view.oneProduct),
    # path("", hello.views.index, name="index"),
    path("admin/", admin.site.urls),
    path('', include('payments.urls')),
    path('', include('products.urls')),
    path('', include('users.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
