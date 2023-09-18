from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from report.models import Comment
from .forms import PostForm, EditForm
from django.urls import reverse_lazy
from report.models import Post
from django.shortcuts import render

# Create your views here.
def homeView(request):
    recent_bom = Post.objects.filter(category__name='BOM Comparison').latest('date_added')
    recent_cost = Post.objects.filter(category__name='Cost Review').latest('date_added')
    context={
        'recent_bom':recent_bom.id,
        'recent_cost':recent_cost.id
    }
    return render(request,'home.html', context)

class CommentView(ListView):
    template_name='comment.html'
    ordering=['-date_added']
    model=Comment

class CommentDetailView(DetailView):
    model=Comment
    template_name='comment_detail.html'

class CommentAddView(CreateView):
    model=Comment
    form_class=PostForm
    template_name='comment_add.html'
    success_url=reverse_lazy('comment_url')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentUpdateView(UpdateView):
    model=Comment
    form_class=EditForm
    template_name='comment_update.html'
    success_url=reverse_lazy('comment_url')
    
class CommentDeleteView(DeleteView):
    model=Comment
    template_name='comment_delete.html'
    success_url=reverse_lazy('comment_url')