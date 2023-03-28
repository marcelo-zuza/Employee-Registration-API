from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api1.views import IndexView, JobViewSet, EmployeeViewSet

router = SimpleRouter()
router.register('jobs', JobViewSet)
router.register('employees', EmployeeViewSet)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

]
