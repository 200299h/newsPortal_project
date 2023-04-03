from django.views.generic import ListView, DetailView
from .models import Category, Post


class CategoryDate:
    """ For getting all category's """

    @staticmethod
    def get_all_cat():
        return Category.objects.all()


class MainPage(CategoryDate, ListView):
    model = Post
    template_name = 'index.html'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.all().order_by('-date')


class CategoryPage(CategoryDate, ListView):
    template_name = 'index.html'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(main_category=self.kwargs['category']).order_by('-date')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.kwargs['category'])
        context['cat_selected'] = int(self.kwargs['category'])
        print(type(context['cat_selected']))
        return context


class NewsPage(CategoryDate, DetailView):
    """  News detail page """
    model = Post
    template_name = "news_show.html"
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'


class Filter(CategoryDate, ListView):
    """ For filtering news """
    model = Post
    template_name = 'index.html'

    def get_queryset(self):
        if self.request.GET.get('date') and self.request.GET.get('category') != '0':
            return Post.objects.filter(main_category=self.request.GET.get('category'),
                                       date__date=self.request.GET.get('date')).order_by('-date')
        else:
            if self.request.GET.get('date'):
                return Post.objects.filter(date__date=self.request.GET.get('date')).order_by('-date')
            return Post.objects.filter(main_category=self.request.GET.get('category')).order_by('-date')
