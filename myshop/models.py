from django.db import models

# Create your models here.
class Books(models.Model):
    book_name = models.CharField(max_length=255,verbose_name='Kitaptin ati:')
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=10,decimal_places=2,)
    description = models.TextField()
    janr = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media')
    
    class Meta:
        verbose_name = 'Kitap'
        verbose_name_plural = 'Kitaplar'

    def __str__(self):
        return self.book_name #admin panelde kitaptin ati turiwi ushin

