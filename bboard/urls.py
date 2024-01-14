from django.urls import path
from .views import (index,
                    BbByRubricView,
                    BbCreateView,
                    RubricCreateView,
                    AllUsersView,
                    UserDetailsView,
                    SinglePostView,
                    ChronologicalPostsView)

app_name = 'bboard'

urlpatterns = [
    path('post/<int:post_id', SinglePostView.as_view(), name='single_post'),
    path('chronological_posts/', ChronologicalPostsView.as_view, name='chronological_posts'),
    path('chronological_posts_json/', ChronologicalPostsView.as_view(), name='chronological_posts_json'),
    path('all_users/', AllUsersView.as_view(), name='all_users'),
    path('user_details/<int:user_id>/', UserDetailsView.as_view(), name='user_details'),

    # path('add/', add_and_save, name='add'),
    path('add/rubric/', RubricCreateView.as_view(), name='add_rubric'),
    path('add/', BbCreateView.as_view(), name='add'),

    # path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('<int:rubric_id>/', BbByRubricView.as_view(), name='by_rubric'),
    path('', index, name='index'),
]
