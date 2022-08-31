from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from gardenyieldzapi.views import register_user, login_user
from gardenyieldzapi.views.plant import PlantView
from gardenyieldzapi.views.JournalView import JournalView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'plants', PlantView, 'plant')
router.register(r'journals', JournalView, 'journal')



urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]