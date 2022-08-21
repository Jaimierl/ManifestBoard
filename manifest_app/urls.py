from django.urls import path
from .views import HomePageView,ManifestCreateView,ManifestUpdateView,ManifestDeleteView,ManifestDetailView, ManifestListView

urlpatterns = [
    # path("",HomePageView.as_view(),name = "manifest_home"),
    path("",ManifestListView.as_view(),name = "manifest_list"),
    path('<int:pk>/', ManifestDetailView.as_view(), name='detail_manifestation'),
    path('create/', ManifestCreateView.as_view(), name='create_manifestation'),
    path('<int:pk>/update/', ManifestUpdateView.as_view(), name='update_manifestation'),
    path('<int:pk>/delete/', ManifestDeleteView.as_view(), name='delete_manifestation'),
]