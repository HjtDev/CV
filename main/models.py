from django.db import models


class Contact(models.Model):
    name = models.CharField('نام و نام خانوادگی', max_length=255)
    email = models.EmailField('ایمیل', max_length=255)
    message = models.TextField('پیام', blank=True, null=True, default='', max_length=1000)
    created_at = models.DateTimeField('تاریخ ایجاد', auto_now_add=True)

    def __str__(self):
        return f'{self.name} از طرف '