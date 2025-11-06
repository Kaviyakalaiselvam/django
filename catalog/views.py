from django.shortcuts import render
from . import data

def index(request):
    return render(request, 'catalog/index.html', {'books': data.BOOKS[:3], 'authors': data.AUTHORS})

def book_list(request):
    books = data.BOOKS
    return render(request, 'catalog/book_list.html', {'books': books, 'authors': data.AUTHORS})

def book_detail(request, book_slug):
    book = next((b for b in data.BOOKS if b['slug'] == book_slug), None)
    if not book:
        return render(request, '404.html', status=404)
    author = next((a for a in data.AUTHORS if a['slug'] == book['author_slug']), None)
    return render(request, 'catalog/book_detail.html', {'book': book, 'author': author})

def author_list(request):
    return render(request, 'catalog/author_list.html', {'authors': data.AUTHORS})

def author_detail(request, author_slug):
    author = next((a for a in data.AUTHORS if a['slug'] == author_slug), None)
    if not author:
        return render(request, '404.html', status=404)
    books = [b for b in data.BOOKS if b['author_slug'] == author_slug]
    return render(request, 'catalog/author_detail.html', {'author': author, 'books': books})
