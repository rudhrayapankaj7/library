from Book.models import Book

# to run python file in db shell 
# exec(open('F:\\Class\\B3-B4\\Django\\Library\\Book\\db_shell.py').read())
# ORM Queries

"""
# all data
# all_data = Book.objects.all()h
# print(all_data)
# print("-" * 50)
# single data
# sid = 1
# b2 = Book.objects.get(id=sid)
# print(b2)
# print("-" * 50)

# create data
b3 = Book.objects.create(name="Java",author="G UYGUC", qty=17, price=784)
print(b3.id)
print("-" * 50)

# update data
sid = 3
b4 = Book.objects.get(id=sid)
b4.name = "LMNOP"
b4.author = "JGUYQVUVYV"
b4.qty = 79
b4.save()
print("-" * 50)

# delete data
sid = 4
b5 = Book.objects.get(id=sid)
b5.delete()

"""

# all_data = Book.objects.all()   # len(all_data)
# print(all_data)
# for book in all_data:
#     print("--------- Details for ID Number:- ", book.id, "-----------")
#     print("Book Name:- ", book.name)
#     print("Author Name:- ", book.author)
#     print("Quantity:- ", book.qty)
#     print("Price per Book:- ", book.price)


# for updating and deleting records
# for book in all_data:
    # book.qty = 15
    # book.save()
    # book.delete()

# ------details for id number-----------
# book name:- 
# author name:- 
# qty:- 
# price per book:- 
# ------details for id number-----------



# all_data = Book.objects.all().values("id", "name", "qty")  # len(all_data)
# print(list(all_data))
# for i in all_data:
    # print(i)

# all_data = Book.objects.values_list()  # len(all_data)
# print(all_data) # 
# for i in all_data:
    # print(i[0])

# import random
# for i in range(1, 36):
#     Book(name=(chr(random.randint(65, 90))) * 5 ,author="ABC", qty=random.randint(15, 85), price=random.randint(200, 900)).save()
#     


#


# gt, gte, lt, lte

# books = Book.objects.filter(id__lt=15).values("id", "name")
# name__startswith, name__istartswith
# name__endsswith, name__iendswith

# books = Book.objects.filter(name__istartswith='j').values("id", "name")
# for i in books:
#     print(i)


# b = Book.objects.all().order_by("-name")    # Asc, Desc
# print(b)

# b = Book.objects.all()[0:5]           #.count()  # len(), count()
# print(b)

# l = [i for i in range(12, 20)]  #  [1,2,3....15]

# books = Book.objects.all().filter(id__in=l)
# print(books)

# books = Book.objects.exclude(id__in=l)
# print(books)
# try:
#     Book.objects.bulk_create([
#     Book(name="Java1",author="A UYGUC", qty=17),
#     Book(name="Java2",author="B UYGUC", qty=7),
#     Book(name="Java3",author="C UYGUC", qty=107),
#     Book(name="Java4",author="D UYGUC", qty=177),
#     Book(name="Java5",author="E UYGUC", qty=179)
#     ])
# except django.db.utils.IntegrityError as msg:
#     pass    



# objs = list(Book.objects.filter(id__in=[36,37,38,39,40]))

# Book.objects.bulk_update(objs, [])

# Book.objects.filter(id__in=[36,37,38,39,40]).update(price=900)


#### 


# Book.objects.bulk_create([
# Book(name="Java1",author="A UYGUC", qty=17, price=100),
# Book(name="Java2",author="B UYGUC", qty=7, price=200),
# Book(name="Java3",author="C UYGUC", qty=107, price=300),
# Book(name="Java4",author="D UYGUC", qty=177, price=400),
# Book(name="Java5",author="E UYGUC", qty=179, price=500)])