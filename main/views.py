from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.mail import send_mail


def index_view(request):
    return render(request, 'index.html')


def contact_view(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        email = request.GET.get('email')
        message = request.GET.get('message')

        if name and email and message:
            try:
                html_message = render(request, 'email.html', {'name': name, 'message': message, 'email': email}).content.decode('utf-8')
                send_mail(
                    subject=f'پیام جدید از طرف {name}',
                    message='This is a plain text fallback message.',
                    from_email='info@mhnikoobakht.dev',
                    recipient_list=['m.h.nikoobakht@gmail.com'],
                    html_message=html_message
                )

                return JsonResponse({
                    'success': True,
                    'type': 'success',
                    'message': 'پیام شما دریافت شد و پاسخ به ایمیل شما ارسال خواهد شد.'
                })
            except Exception as e:
                print(e)
                return JsonResponse({
                    'success': False,
                    'error': str(e),
                    'type': 'error',
                    'message': 'مشکلی پیش آمده است لطفا مجددا تلاش کنید.'
                })

    return JsonResponse({
        'success': False,
        'type': 'error',
        'message': 'لطفا همه فیلدها را پر کنید.'
    })
