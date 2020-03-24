from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('results/<str:title>', views.get_results_by_search, name='results-search'),
        path('info-movie/<str:id_movie>', views.get_information_movie, name='info-movie'),
        path('watch_movie/<str:id_movie>', views.watch_movie, name="watch-movie")
]
