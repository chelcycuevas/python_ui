from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('builds/', views.BuildEditorView.as_view(), name='builds'),
    path('build/<int:pk>', views.BuildEditorDetailView.as_view(), name='build-detail'),
    path('alliances/', views.AlliancesView.as_view(), name='alliances'),
    path('alliance/<int:pk>', views.AlliancesDetailView.as_view(), name='alliance-detail'),
    path('races/', views.RacesView.as_view(), name='races'),
    path('race/<int:pk>', views.RacesDetailView.as_view(), name='race-detail'),
    path('classes/', views.ClassesView.as_view(), name='classes'),
    path('class/<int:pk>', views.ClassesDetailView.as_view(), name='class-detail'),
    path('skills/', views.SkillsView.as_view(), name='skills'),
    path('skill/<int:pk>', views.SkillsDetailView.as_view(), name='skill-detail'),
    path('zones/', views.ZonesView.as_view(), name='zones'),
    path('zone/<int:pk>', views.ZonesDetailView.as_view(), name='zone-detail')
]