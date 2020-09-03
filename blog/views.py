from django.shortcuts import render,get_object_or_404,reverse
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from blog.models import Article
from . forms import ArticleModelForm

# Create your views here.
class ArticleListView(ListView):
    queryset = Article.objects.all()
    template_name = 'articles/list.html'



class ArticleDetailsView(DetailView):
    template_name = 'articles/details.html'
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article,id=id_)

class ArticleCreateView(CreateView):
    template_name = 'articles/create.html'
    form_class = ArticleModelForm

    def form_valid(self,form):
        return super().form_valid(form)

    def get_success_url(self):
        return '/article'

class ArticleUpdateView(UpdateView):
    template_name = 'articles/create.html'
    queryset = Article.objects.all()
    form_class = ArticleModelForm

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article,id=id_)
    
class ArticleDeleteView(DeleteView):
    template_name = 'articles/delete.html'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article,id=id_)
    
    def get_success_url(self):
        return reverse('blog:article-list')

    
    