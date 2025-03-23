from django.db import models

class Book(models.Model):
    book_name_english = models.TextField(blank=True, null=True)
    book_name_devanagari = models.TextField(blank=True, null=True)
    book_name_perso_arabic = models.TextField(blank=True, null=True)
    author_name_english = models.TextField(blank=True, null=True)
    author_name_devanagari = models.TextField(blank=True, null=True)
    author_name_perso_arabic = models.TextField(blank=True, null=True)
    collection_location = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    other_details = models.TextField(blank=True, null=True)
    image = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.book_name_english or "Untitled Book"
    
    class Meta:
        db_table = 'books'  # Must match the real table name
        managed = False 
