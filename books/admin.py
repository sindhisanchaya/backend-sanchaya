from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'book_name_english',
        'author_name_english',
        'collection_location',
        'book_name_devanagari',
    )

    search_fields = (
        'book_name_english',
        'book_name_devanagari',
        'author_name_english',
        'author_name_devanagari',
        'collection_location',
    )

    list_filter = (
        'collection_location',
        'author_name_english',
    )

    ordering = ['book_name_english']
