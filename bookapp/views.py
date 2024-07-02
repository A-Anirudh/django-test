from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Book
from .forms import *

def search(request):
    query = request.GET.get('q', '')
    startswithquery = request.GET.get('titlesearch', '')
    print(f"Query: {query}, StartswithQuery: {startswithquery}")
    if query or startswithquery:
        qset = (
            Q(title__icontains=query) | Q(author__fname__icontains=query) | Q(author__lname__icontains=query) | Q(title__startswith=startswithquery)
        )
        results = Book.objects.filter(qset).distinct()
        print(f"Results: {results}")
    else:
        results = []
    
    return render(request, 'search.html', {'results': results, 'query': query, 'startswithquery': startswithquery})



def feedback_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            print(topic, message, sender)
            
            return redirect('/home')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})
