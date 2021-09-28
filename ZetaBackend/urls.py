from django.urls import include, path
from rest_framework import routers
from api.views import frisbee_view

router = routers.DefaultRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('frisbees/', frisbee_view.FrisbeeList.as_view()),
    path('frisbees/<int:pk>', frisbee_view.FrisbeeDetail.as_view()),

    path('frisbees_ingredient/', frisbee_view.FrisbeeIngredientList.as_view()),
    path('frisbees_ingredient/<int:pk>', frisbee_view.FrisbeeIngredientDetail.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]