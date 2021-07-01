from django.conf.urls import url, include
from rest_framework import routers

# Register API Endpoints
from services.productionplan import views as productionplans

router = routers.SimpleRouter()
router.register('productionplan', productionplans.ProductionplanViewSet, basename='productionplans')

urlpatterns = [
    url(r'^', include(router.urls)),
]
