from django.db import models
from django.contrib import admin
class book_DB(models.Model):
    bookno=models.IntegerField(primary_key="bookno");
    bookname=models.CharField(max_length=20);
    authorname=models.CharField(max_length=20);
    year=models.DateField();
    price=models.IntegerField();
    pages=models.IntegerField();

class book_DBAdmin(admin.ModelAdmin):
   list_display=("bookno","bookname","authorname","year","price","pages");