from django.db.models import Count
from django.core.paginator import Paginator
from django.utils import timezone


def comment_count(queryset):
    return queryset.annotate(comment_count=Count("comments"))


def get_published_posts(queryset):
    now = timezone.now()
    return queryset.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=now
    )


def get_published_posts_with_no_filter(queryset):
    return queryset.published()


def get_paginator(request, queryset, per_page=10):
    paginator = Paginator(queryset, per_page)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)


def is_post_visible_to_user(post, user):
    now = timezone.now()
    return (post.is_published and post.pub_date <= now) or post.author == user