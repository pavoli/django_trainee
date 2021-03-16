from django.shortcuts import render
from django.views import generic

from .models import Book, Author, BookInstance, Genre


# Create your views here.
def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(
        status__exact='a').count()

    num_genres = Genre.objects.all().count()
    num_books_war = Book.objects.filter(
        title__icontains='мир'
    ).count()

    num_authors = Author.objects.count()

    context = {
        'num_books': num_books, 'num_instances': num_instances,
        'num_instances_available': num_instances_available, 'num_authors': num_authors,
        'num_genres': num_genres, 'num_books_war': num_books_war
    }

    return render(
        request,
        'index.html',
        context=context,
    )


class BookListView(generic.ListView):
    model = Book
    paginate_by = 5

    context_object_name = 'book_list'
    queryset = Book.objects.all()


class BookDetailView(generic.DetailView):
    model = Book

    def book_detail_view(request, primary_key):
        book = get_object_or_404(Book, pk=primary_key)
        
        return render(request, 'catalog/book_detail.html', context={'book': book})


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 5

    context_object_name = 'author_list'
    queryset = Author.objects.all()


class AuthorDetailView(generic.DetailView):
    model = Author

    def author_detail_view(request, primary_key):
        author = get_object_or_404(Author, pk=primary_key)
        
        return render(request, 'catalog/author_detail.html', context={'author': author})