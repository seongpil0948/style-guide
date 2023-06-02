from django.db.models import query
from app.models import *
from django.db import transaction, connection, reset_queries
from datetime import datetime
from random import choice, choices

address = ['광명', '철산', '일산', '서울', '부산']
friends = ['성필', '성훈', '준회', '인재', '용기', '지현']
books = ['소설', '자기계발', '네트워크', '교과서', '지구과학']

@transaction.atomic
def lib_create():
    reset_queries()
    start = datetime.now()

    r = range(1, 1001)
    " max_batch_size of bulk_create each query is 999 "
    objects =  [
        Library(
            name=address[i % len(address)] + ' 도서관',
            address=address[i % len(address)]
        ) for i in r
    ]
    Library.objects.bulk_create(objects)

    end = datetime.now()
    queries = connection.queries
    print(f"Time Spend {len(list(r))} time ===> ", end - start)
    print(f"number of queries: {len(queries)}")
    print("========first query=======")
    print(queries[0])
    print("========Last Query ========")
    print(queries[-1])
""" 
number of queries: 3

first query
INSERT INTO "app_library" ("name", "address") SELECT \'철산 도서관\', \'철산\'
UNION ALL SELECT \'일산 도서관\', \'일산\' UNION ALL SELECT  ........

last query
'INSERT INTO "app_library" ("name", "address") SELECT \'부산 도서관\', \'부산\'
UNION ALL SELECT \'광명 도서관\', \'광명\'', 'time': '0.000'}
"""
@transaction.atomic
def author_create():
    r = range(1, 1001)
    objects =  [
        Author(
            name=friends[i % len(friends)]
        ) for i in r
    ]
    Author.objects.bulk_create(objects)

@transaction.atomic
def book_create():
    r = range(1, 10001)
    authors = Author.objects.all()[:5]
    libs = Library.objects.all()[:len(address)]
    objects =  [
        Book(
            title=books[i % len(books)],
            author=authors[i % len(authors)],
            library=libs[i % len(libs)],
            address=address[i % len(address)]
        ) for i in r
    ]
    Book.objects.bulk_create(objects)

@transaction.atomic
def page_create():
    r = range(1, 1000001)
    books = Book.objects.all()[:5]
    objects =  [
        Page(
            book=books[i % len(books)],
            text=None,
            page_number=choice(r)
        ) for i in r
    ]
    Page.objects.bulk_create(objects)