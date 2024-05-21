from django.db import models


class Book(models.Model):
    DIRECTION_CHOICES = [
        ('Darslik', 'Darslik'),
        ('O\'quv qo\'llanma', 'O\'quv qo\'llanma'),
        ('Monografiya', 'Monografiya'),
        ('Uslubiy qo\'llanma', 'Uslubiy qo\'llanma'),
        ('Uslubiy ko\'rsatma', 'Uslubiy ko\'rsatma'),
    ]
    title = models.CharField(max_length=100)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=14)
    description = models.TextField()
    direction = models.CharField(max_length=50, choices=DIRECTION_CHOICES)
    confirmed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    file1 = models.FileField(upload_to='books1/')
    file2 = models.FileField(upload_to='books2/')
    file3 = models.FileField(upload_to='books3/')
    file4 = models.FileField(upload_to='books4/')
    file5 = models.FileField(upload_to='books5/')

    def __str__(self):
        return self.title


class CheckBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    description = models.TextField()
    confirmed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book.title
