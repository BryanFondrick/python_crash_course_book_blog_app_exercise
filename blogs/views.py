from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.
def index(request):
    """The home page for Blog"""
    
    #posts = BlogPost.objects.order_by('date_added')
    #posts = BlogPost.objects.all()
    #context = {'posts': posts}
    titles=BlogPost.objects.order_by('date_added')
    context = {'titles': titles}
    #can there be more than one dictionary?
    return render(request, 'blogs/index.html', context)

def titles(request):
    """Show all titles."""
    titles= BlogPost.objects.order_by('date_added')
    context = {'titles': titles}
    return render(request, 'blogs/titles.html', context)
    
def title(request,title_id):
    """Show a single blog"""
    title = BlogPost.objects.get(id=title_id)# get all data for an individual title
    #posts = BlogPost.objects.order_by('date_added')# not needed
    context = {'title': title}
    return render(request,'blogs/title.html', context)

def new_entry(request):
    """Add a new entry to the blog page."""
    title = BlogPost.objects.all()
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = BlogPostForm()
    else:
        # POST data submitted; process data
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            new_title = form.save(commit=False)
            #new_title.title = title
            new_title.save()
            return HttpResponseRedirect(reverse('blogs:index'))# go back to this page after posting
    context = {'title': title,'form': form} #can I remove entry? and leave only form?
    return render(request, 'blogs/new_entry.html', context)
    
def edit_entry(request,title_id):
    """Edit an existing entry."""
    
    title = BlogPost.objects.get(id=title_id) #just need an individual blog post
    #text = titles.text 
    
    
    if request.method != 'POST':
        #Initial request; pre-fill form with current entry.
        form = BlogPostForm(instance=title)
    else:
        # POST data submitted; process data.
        form = BlogPostForm(instance=title, data=request.POST)
        if form.is_valid():
            form.save()
            #should go back to the individual title, with a filled out form
            return HttpResponseRedirect(reverse('blogs:index',args=[title.id]))
    context = {'title': title}
    #context = {'form': form }
    #context = {'title': form,'form': form}
    return render(request, 'blogs/edit_entry.html', context)
    
