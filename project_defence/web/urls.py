from django.urls import path
from project_defence.web import views

urlpatterns = [
    path("", views.index_page, name='index page'),  # visible for everyone

    #  profile pages
    # TODO add saved games !!!
    path("profile/create/", views.profile_create_page, name='profile create page'),
    path("profile/edit/", views.profile_edit_page, name='profile edit page'),
    path("profile/delete/", views.profile_delete_page, name='profile delete page'),
    path("profile/saved_games/", views.profile_saved_games_page, name='profile saved games'),

    # games pages
    # TODO add static games, description for the dif. games!!!
    path("browse games", views.browse_games, name='browse games page'),
    path("game info", views.game_info, name='game info page'),
    path("recommended games", views.recommended_games, name='recommended games'),
    path("trending games", views.trending_games, name='trending games'),


]