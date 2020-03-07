from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CageViewSet
from rest_framework import routers

router = DefaultRouter()
router.register(r'', CageViewSet, basename='cages')
urlpatterns = router.urls


# router = routers.DefaultRouter()
# router.register(r'cages', views.CageView)


# urlpatterns = [
#     path('', PostListView.as_view(), name='rodent-home'),
#     path('', CageListView.as_view(), name='rodent-home'),
#     path('create/', CageCreateView.as_view()),
#     path('<pk>', CageDetailView.as_view()),
#     path('<pk>/update/', CageUpdateView.as_view()),
#     path('<pk>/delete/', CageDestroyView.as_view()),
#     path('about/', views.about, name='rodent-about'),
#     path('apiroot/', include(router.urls))
# ]
