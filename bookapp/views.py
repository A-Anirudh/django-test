from django.shortcuts import render
from django.db.models import Q
from .models import Book

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
