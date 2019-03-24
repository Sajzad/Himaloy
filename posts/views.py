from django.shortcuts import render, get_object_or_404
from .models import Post, Signup, CourseOverview
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count, Q
from .forms import CommentForm



def get_category_count():
    queryset= Post.objects.values('categories__title').annotate(Count('categories__title'))
    return queryset



def index_view(request):
    All_post= Post.objects.all()
    course_overview= CourseOverview.objects.all()
    featured= All_post.filter(featured=True )
    if request.method=="POST":
        email_data=request.POST['email']
        new_signup=Signup()
        new_signup.email=email_data
        new_signup.save()
    context={
        'object_list': course_overview,
        'latest_post':latest_post
        }
    return render(request, 'index/index.html', context)


def blog_view(request):
    category_count= get_category_count()
    post=Post.objects.all()
    django_post_list= post.select_related("categories").filter(categories__title='Django')
    most_recent= Post.objects.order_by('-timestamp')[:6]
    paginator= Paginator(django_post_list,10)
    page_request_variable='page'
    page= request.GET.get(page_request_variable)
    try:
        paginated_queryset= paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset=paginator.page(1)
    except EmptyPage:
        paginated_queryset= paginator.page(paginator.num_pages)
    context={
    'category_count': category_count,
    'queryset': paginated_queryset,
    'page_request_variable':page_request_variable,
    'most_recent':most_recent,

    }
    return render(request, 'blog/blog.html',context)

    #python Post list

def python_list(request):
    category_count= get_category_count()
    post= Post.objects.all()
    most_recent= post.order_by('-timestamp')[:6]
    post_list= post.select_related("categories").filter(categories__title="Python")
    paginator=Paginator(post_list,10)
    page_request_variable="page"
    page= request.GET.get(page_request_variable)

    try:
        paginated_queryset= paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset=paginator.page(1)
    except EmptyPage:
        paginated_queryset=paginator.page(paginator.num_pages)

    context={
        'queryset':paginated_queryset,
        'page_request_variable':page_request_variable,
        'category_count': category_count,
        'most_recent':most_recent,
    }
    return render(request, 'blog/python_list.html',context)

    # C  list view
def C_list(request):
    category_count= get_category_count()
    post= Post.objects.all()
    most_recent= post.order_by('-timestamp')[:6]
    post_list= post.select_related("categories").filter(categories__title="Programming C")
    paginator=Paginator(post_list,10)
    page_request_variable="page"
    page= request.GET.get(page_request_variable)

    try:
        paginated_queryset= paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset=paginator.page(1)
    except EmptyPage:
        paginated_queryset=paginator.page(paginator.num_pages)

    context={
        'queryset':paginated_queryset,
        'page_request_variable':page_request_variable,
        'category_count': category_count,
        'most_recent':most_recent,
    }
    return render(request, 'blog/C_list.html',context)




def search(request):
    queryset= Post.objects.all()
    query= request.GET.get('q')
    if query:
        queryset= queryset.filter(
            Q(title__icontains= query)|
            Q(overview__icontains= query)).distinct()

    context={
    'queryset':queryset,


    }
    return render(request, 'search_result.html', context)



def post_detail(request, post_id):
    category_count= get_category_count()
    # most_recent= post.order_by('-timestamp')[:6]
    post=get_object_or_404(Post, id=post_id)
    form= CommentForm(request.POST or None)
    if request.method== 'POST':
        if form.is_valid():
            form.instance.user= request.user
            form.instance.post= post
            form.save()
    context= {
    'post':post,
    # 'most_recent':most_recent,
    'form':form,
    }

    return render(request, 'post/post_detail.html', context)


# Post list View

# def django_post_detail(request):
#     category_count= get_category_count()
#     post_list= Post.objects.all()
#     dajngo_featured_post= post_list.select_related("categories").filter(featured=True, categories__title='Django')
#     latest_post= post_list.filter(featured=True).order_by('-timestamp')[:5]
#
#     context={
#         'django_post_list': dajngo_featured_post,
#         'latest_post': latest_post,
#         'category_count': category_count,
#
#     }
#
#     return render(request, "post/django_post_detail.html",context)






















# Create your views here.
