from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm
# import rules
# from rules.rulesets import test_rule
from rules.permissions import has_perm
# from rules.contrib.views import permission_required
from django.core.exceptions import PermissionDenied

# def get_post_by_pk(request, post_id):
#     return get_object_or_404(Post, pk=post_id)

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    u = 'Ala makota'
    author = request.user
    return render(request, 'blog/post_detail.html', {'post':post, 'author':author})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post_id=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})

@login_required
# @permission_required('blog.change_post', fn=get_post_by_pk)
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    # wynik = test_rule('can_edit_post', request.user, post)
    wynik = has_perm('blog.change_post', request.user, post)
    if not wynik:
        raise  PermissionDenied  
    if request.method == "POST":
        # uruchomienie widoku po Save - POST
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post_id=post.pk)
    else:
        # uruchomienie widoku z urla - GET
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    wynik = has_perm('blog.change_post', request.user, post)
    if not wynik:
        raise  PermissionDenied 
    post.publish()
    return redirect('post_detail', post_id=post.pk)

@login_required
def post_remove(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('post_list')

def add_comment_to_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            # comment = form.save(commit=False) # dla: forms.ModelForm
            # comment.post = post 
            cd = form.cleaned_data # dla: forms.Form
            comment = Comment(author=cd['author'], text=cd['text'], post=post) # koniec dla: forms.Form
            comment.save()
            request.session['username'] = comment.author
            return redirect('post_detail', post_id=post.pk)
    else:
        # value_true if <test> else value_false
        # u = request.user.username if request.user.username else 'gosc'        
        username = ""
        if request.session.has_key('username'):
            username = request.session['username']
        u = request.user.username or username or 'gosc'
        form = CommentForm(initial={'author':u})
    return render(request, 'blog/add_comment_to_post.html', {'form': form})