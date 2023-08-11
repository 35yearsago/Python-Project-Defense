from django.urls import path
from project_defence.web import views
from project_defence.web.views import My404View

urlpatterns = [
    path("", views.home_page, name='home page'),
    path("index/", views.index_page, name='index page'),  # visible for everyone

    #  profile pages
    # TODO add saved games !!!
    path("register/", views.profile_create_page, name='profile create page'),
    # path("register/", views.RegisterUserView, name='register_user'),
    # path("login/", views.LogUserView, name='login_user'),
    # path("logout/", views.LogoutUserView, name='logou_user'),
    path("profile/edit/", views.profile_edit_page, name='profile edit page'),
    path("profile/delete/", views.profile_delete_page, name='profile delete page'),
    path("profile/saved_games/", views.profile_saved_games_page, name='profile saved games'),
    path("about/", views.about_page, name='about page'),
    path("about-no-profile/", views.about_nop_page, name='about nop page'),
    path("login/", views.login_page, name='login page'),
    path("cart/", views.cart_page, name='cart page'),
    path("logout/", views.logout_page, name='logout page'),
    # games pages
    # TODO add static games, description for the dif. games!!!
    path("games/", views.games, name='games page'),
    path("more games/", views.more_games, name='more games page'),
    path("game info/", views.game_info, name='game info page'),
    path("recommended games/", views.recommended_games, name='recommended games'),
    path("trending games/", views.trending_games, name='trending games'),
    path("experts/", views.experts, name='experts page'),
    path("real-time strategy/", views.real_time_strategy, name='real-time strategy page'),
    path("shooter/", views.shooter, name='shooter page'),
    path("multiplayer-online-battle-arena/", views.multiplayer_online_battle_arena, name='multiplayer battle arena'),
    path("role-playing/", views.role_playing_games, name='role playing games'),
    path("simulation-sparts/", views.simulation_sports, name='simulation sparts'),
    path("sandbox/", views.sandbox_games, name='sandbox games'),
    path('404/', My404View.as_view(), name='404'),
]