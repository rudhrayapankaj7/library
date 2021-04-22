from django.db import models

# Create your models here.


# app name-  Book, model name - Book
class BookActiveManager(models.Manager):  # Custom Manager
    def get_queryset(self):
        return super(BookActiveManager, self).get_queryset().filter(is_deleted='N')   

class BookInactiveManager(models.Manager):  # Custom Manager
    def get_queryset(self):
        return super(BookInactiveManager, self).get_queryset().filter(is_deleted='Y')   



class Book(models.Model):
    # id is created by django default   
    # columns wil generate for below fields
    name = models.CharField(max_length=100)   # 
    author = models.CharField(max_length=100)   
    qty = models.IntegerField()
    price = models.FloatField()
    is_published = models.BooleanField(default=False)
    is_deleted = models.CharField(max_length=1, default="N")   # "Y", "N"

    # columns wil not generate for below fields
    active_objects = BookActiveManager()
    inactive_objects = BookInactiveManager()
    objects = models.Manager()  # mandate

    def __str__(self):
        return f"{self.id} --- {self.name} --- {self.author}"

    class Meta:
        db_table = "bookinfo"

    


# appname_modelname  - small case
# create table book_book (id int unique AUTO_INCREMENT, name varchar(100), author varchar(100), qty int, price float)


# "rename table {} to {}".format(abc, pqr)
"""
denv) F:\Class\B3-B4\Django\Library>python manage.py shell
Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from Book.models import Book
>>> Book.objects.all()
<QuerySet [<Book: Wings of fire --- APJ Sir>, <Book: XYZ --- PQr>]>
>>> b = Book.objects.all() 
>>> b
<QuerySet [<Book: Wings of fire --- APJ Sir>, <Book: XYZ --- PQr>]>
>>> type(b) 
<class 'django.db.models.query.QuerySet'>
>>> list(b) 
[<Book: Wings of fire --- APJ Sir>, <Book: XYZ --- PQr>]
>>> b1 = list(b) 
>>> type(b1) 
<class 'list'>
>>> b2 = Book.objects.get(id=3) 
>>> b2
<Book: XYZ --- PQr>
>>> type(b2) 
<class 'Book.models.Book'>
>>> Book.objects.create(name='XYZ',author="QWERTY", qty=75, price=647) 
<Book: XYZ --- QWERTY>
>>> Book()          
<Book:  --- >
>>> b4 = Book(name='XYZ',author="QWERTY", qty=75, price=647) 
>>> b4.save()
>>> b5 = Book.objects.get(id=4) 
>>> b5
<Book: XYZ --- QWERTY>
>>> b5.name = 'PQR' 
>>> b5.save()
>>> b6 = Book.objects.get(id=5) 
>>> b6
<Book: XYZ --- QWERTY>
>>> b6.delete()
(1, {'Book.Book': 1})
>>> 
"""

