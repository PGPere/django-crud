from django.urls import path
from .views import HomePageView, AboutView, SnacksList, SnacksDetail
from .views import SnacksCreateView, SnacksDeleteView, SnacksUpdateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path(' ', SnacksList.as_view(), name='snacks_list'),
    path('<int:pk>', SnacksDetail.as_view(), name='snacks_detail'),
    path('create/', SnacksCreateView.as_view(), name='snacks-create'),
    path('<int:pk>/update/',
         SnacksUpdateView.as_view(), name='snacks-update'),
    path('<int:pk>/delete/', SnacksDeleteView.as_view(), name='snacks-delete'),
]
