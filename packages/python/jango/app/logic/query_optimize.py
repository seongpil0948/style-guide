from app.models import *
from app.utils.printing import only_print_info
from collections import defaultdict

REPEAT_TIME = 5

@only_print_info(repeat_time=REPEAT_TIME, print_queries=False)
def get_books_by_author():
    books = Book.objects.all()
    result = defaultdict(list)
    for book in books:
        author = book.author
        title_and_author = '{} by {}'.format(
            book.title,
            author.name
        )
        result[book.library_id].append(title_and_author)
    return result

@only_print_info(repeat_time=REPEAT_TIME, print_queries=False)
def get_books_by_author_select_related():
    books = Book.objects.all().select_related('author')
    result = defaultdict(list)
    for book in books:
        author = book.author
        title_and_author = '{} by {}'.format(
            book.title,
            author.name
        )
        result[book.library_id].append(title_and_author)
    return result


" In order to traverse "
" reverse ForeignKey or ManyToMany relationships we’ll need prefetch_related. "
"""
prefetch_related는 각 관계에 대해 별도의 쿼리를 만들고 결과를 파이썬으로 "결합"합니다.
이 접근 방식의 단점은 데이터베이스에 여러 번 왕복해야한다는 것입니다.
"""
# from django.db import connection, reset_queries
# Author.objects.all().prefetch_related('books').latest('books')
# Author.objects.all().prefetch_related('books').filter(name__startswith='성훈')
" first "
# PKS_OF_AUTHORS_FROM_FIRST_REQUEST= set(1, 2, 3, 4)
# caching = Book.objects.filter(author_id__in =PKS_OF_AUTHORS_FROM_FIRST_REQUEST)

"total 2"
# Author.objects.filter(name__startswith='성훈')
"or"
# Author.objects.first()

"""
초기 쿼리를 수행 한 후 모델의 관계에 액세스하려는 경우 select_related 및 prefetch_related를 사용합니다.
역 ForeignKey 또는 ManyToMany 관계를 따르는 경우 prefetch_related를 사용합니다. 
ForeignKey 또는 OneToOne 관계를 따르는 경우 select_related를 사용하지만 데이터의 특성에 따라 
prefetch_related가 이러한 유형의 관계에 더 나은 선택이 될 수 있습니다.
"""


"""
we’re serializing all of the fields 
We’re also are initializing a Django model instance for no reason since 
we’re not doing anything special with it (like calling model methods).    

Initializing Django model instances is expensive.
If you’re only using the data on the model 
you’re likely better off working with their dictionary or tuple representations.
"""
@only_print_info(repeat_time=REPEAT_TIME, print_queries=False)
def get_books_by_author_select_related_values():
    books = (
        Book.objects
         .all()
         .select_related('author')
         .values('title', 'library_id', 'author__name')
    )
    result = defaultdict(list)
    for book in books.iterator():
        title_and_author = '{} by {}'.format(
            book['title'],
            book['author__name']
        )
        result[book['library_id']].append(title_and_author)
    
    return result

@only_print_info(repeat_time=REPEAT_TIME, print_queries=False)
def get_books_by_author_select_related_values_list():
    books = (
        Book.objects
         .all()
         .select_related('author')
         .values_list('title', 'library_id', 'author__name')
    )
    result = defaultdict(list)
    for book in books.iterator():
        title_and_author = '{} by {}'.format(
            book[0],
            book[2]
        )
        result[book[1]].append(title_and_author)
    
    return result

get_books_by_author() # 36.23162483300001
get_books_by_author_select_related() # 1.1928956959999937
get_books_by_author_select_related_values() # 0.2026017329999945
get_books_by_author_select_related_values_list() # 0.162219102999984
