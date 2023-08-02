from django.shortcuts import render, redirect

from .models import Blogpost, Entry
from .forms import TitleForm, EntryForm

def index(request):
    """Головна сторінка "Журналу спостережень"."""
    return render(request, 'blogs/index.html')

def titles(request):
    """Відображає всі теми."""
    titles = Blogpost.objects.order_by('date_added')
    context = {'titles': titles}
    return render(request, 'blogs/titles.html', context)

def title (request, title_id):
    """Show a single topic and all its entries."""
    title = Blogpost.objects.get(id=title_id)
    entries = title.entry_set.order_by('-date_added')
    # entries = topic.entry_set.order_by('-date_added')
    context = {'title': title, 'entries': entries}
    return render(request, 'blogs/title.html', context)

def new_title(request):
    """Add a new topic."""
    if request.method != 'POST':
        # Жодних даних не відправлено; створити порожню форму.
        form = TitleForm()
    else:
        # відправлений POST; обробити дані.
        form = TitleForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:titles')
    
    # показати порожню або недійсну форму.
    context = {'form': form}
    return render(request, 'blogs/new_title.html', context)

def new_entry(request, title_id):
    """Add a new entry for a particular topic."""
    title = Blogpost.objects.get(id=title_id)
    if request.method != 'POST':
        # if nothig, create empty form
        form = EntryForm()
    else:
        # get data at POST-request -> using data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.title = title
            new_entry.save()
    
    context = {'title': title, 'form': form}
    return render(request, 'blogs/new_entry.html', context)

def edit_entry(request, entry_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    title = entry.title

    if request.method != 'POST':
        # Initial request; pre-fill form with current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

