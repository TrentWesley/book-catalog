from django.views.generic import ListView
from .models import Book, Publisher, Review


class BookListView(ListView):
    model = Book
    template_name = "book_list.html"


class PublisherListView(ListView):
    model = Publisher
    template_name = "publisher_list.html"


class ReviewListView(ListView):
    model = Review
    template_name = "review_list.html"