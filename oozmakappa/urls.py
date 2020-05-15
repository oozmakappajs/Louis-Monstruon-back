from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

from rest_framework.routers import DefaultRouter
from products.views import DressViewSet
from users.views import UsersViewSet

router = DefaultRouter()
router.register(r'products', DressViewSet)
router.register(r'users', UsersViewSet)

urlpatterns = router.urls

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns += [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    path('', include('payments.urls')),    
]
