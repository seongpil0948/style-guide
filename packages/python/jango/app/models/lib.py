from django.db import models

__all__ = [
    'Library',
    'Author',
    'Book',
    'Page',
]

class Library(models.Model):
    name = models.CharField(max_length=200, default='')
    address = models.CharField(max_length=200, default='')


class Author(models.Model):
    name = models.CharField(max_length=200, default='')


class Book(models.Model):
    library = models.ForeignKey(
        Library,
        on_delete=models.CASCADE,
        related_name='books',
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )
    title = models.CharField(max_length=200, default='')
    address = models.CharField(max_length=200, default='')
    def get_page_count(self):
        return self.pages.count()


class Page(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='pages',
    )
    text = models.TextField(null=True, blank=True)
    page_number = models.IntegerField()

