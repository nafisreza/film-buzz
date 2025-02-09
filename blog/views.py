from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Category
from .forms import CommentForm
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.


def blog(request):
    all_posts = Post.objects.all().order_by('-created_at')
    featured_post = all_posts.first()
    paginator = Paginator(all_posts[1:], 6)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'blog/blog.html',
                  {'posts': posts, 'featured_post': featured_post})


def details(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.all()
    form = CommentForm()
    return render(request, 'blog/details.html',
                  {'post': post, 'comments': comments, 'form': form})


def comment(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('details', category_slug=category_slug, slug=slug)
    else:
        form = CommentForm()
    comments = post.comments.all()
    return render(request, 'blog/details.html',
                  {'post': post, 'comments': comments, 'form': form})


def edit_comment(request, category_slug, comment_id, slug):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST' and comment.user == request.user:
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('details', category_slug=category_slug, slug=slug)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/edit_comment.html',
                  {'form': form, 'post': comment.post})


def delete_comment(request, category_slug, comment_id, slug):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST' and comment.user == request.user:
        comment.delete()
        return redirect('details', category_slug=category_slug, slug=slug)


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.all()
    return render(request, 'blog/category.html',
                  {'category': category, 'posts': posts})


def search(request):
    query = request.GET.get('query', '')
    posts = Post.objects.filter(Q(title__icontains=query))
    return render(request, 'blog/search.html',
                  {'posts': posts, 'query': query})
