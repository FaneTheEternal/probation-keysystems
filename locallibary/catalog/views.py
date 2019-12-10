from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic
# login decorator funcions
from django.contrib.auth.decorators import login_required
# login decorator class
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
@login_required
def index(request):
    """
    Функция отображения для домашней страници
    """
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status='a').count()
    num_author = Author.objects.count()  # all() run default

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_author': num_author,
            'num_visits': num_visits,
            },
    )


class BookListView(LoginRequiredMixin, generic.ListView):
    model = Book
    paginate_by = 2


class BookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Book


class AuthorListView(LoginRequiredMixin, generic.ListView):
    model = Author
    paginate_by = 2


class AuthorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Author


class LoanedBookByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view  listing books on load to current user
    """
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance\
            .objects\
            .filter(borrower=self.request.user)\
            .filter(status__exact='o')\
            .order_by('due_back')
