from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Post, Comment
from .forms import PostForm, CommentForm


@login_required
def feed(request):

    posts = Post.objects.all().order_by("-created_at")

    comment_form = CommentForm()

    return render(
        request,
        "posts/feed.html",
        {
            "posts": posts,
            "comment_form": comment_form,
        },
    )


@login_required
def create_post(request):

    if request.method == "POST":

        form = PostForm(request.POST, request.FILES)

        if form.is_valid():

            post = form.save(commit=False)

            post.user = request.user

            post.save()

            return redirect("feed")

    else:

        form = PostForm()

    return render(
        request,
        "posts/create_post.html",
        {
            "form": form
        }
    )


@login_required
def edit_post(request, post_id):

    post = get_object_or_404(
        Post,
        id=post_id,
        user=request.user
    )

    if request.method == "POST":

        form = PostForm(
            request.POST,
            request.FILES,
            instance=post
        )

        if form.is_valid():

            form.save()

            return redirect("feed")

    else:

        form = PostForm(instance=post)

    return render(
        request,
        "posts/edit_post.html",
        {
            "form": form
        }
    )


@login_required
def like_post(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    if request.user in post.likes.all():

        post.likes.remove(request.user)

    else:

        post.likes.add(request.user)

    return redirect("feed")


@login_required
def add_comment(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":

        form = CommentForm(request.POST)

        if form.is_valid():

            comment = form.save(commit=False)

            comment.post = post

            comment.user = request.user

            comment.save()

    return redirect("feed")


@login_required
def delete_post(request, post_id):

    post = get_object_or_404(
        Post,
        id=post_id,
        user=request.user
    )

    if request.method == "POST":

        post.delete()

    return redirect("feed")


@login_required
def delete_comment(request, comment_id):

    comment = get_object_or_404(
        Comment,
        id=comment_id,
        user=request.user
    )

    if request.method == "POST":

        comment.delete()

    return redirect("feed")