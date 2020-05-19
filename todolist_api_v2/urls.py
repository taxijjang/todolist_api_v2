from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from todolistapi import views

router = DefaultRouter()
router.register('dotitle',views.DoTitleViewSet)
router.register('dolist',views.DoListViewSet)
router.register('docomment',views.DoCommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
