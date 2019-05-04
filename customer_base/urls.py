from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import (
    CustomerViewSet,
    ProfessionViewSet,
    DataSheetViewSet,
    DocumentViewSet
)

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('customers', CustomerViewSet, base_name='customer')
router.register('professions', ProfessionViewSet)
router.register('data-sheet', DataSheetViewSet)
router.register('documents', DocumentViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
