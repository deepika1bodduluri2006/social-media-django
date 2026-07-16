from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.feed,
        name="feed",
    ),

    path(
        "create/",
        views.create_post,
        name="create_post",
    ),

    path(
        "edit/<int:post_id>/",
        views.edit_post,
        name="edit_post",
    ),

    path(
        "like/<int:post_id>/",
        views.like_post,
        name="like_post",
    ),

    path(
        "comment/<int:post_id>/",
        views.add_comment,
        name="add_comment",
    ),

    path(
        "comment/delete/<int:comment_id>/",
        views.delete_comment,
        name="delete_comment",
    ),

    path(
        "delete/<int:post_id>/",
        views.delete_post,
        name="delete_post",
    ),

]