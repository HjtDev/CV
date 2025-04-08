from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect
import json
from .models import Contact


def index_view(request):
    return render(request, 'index.html')


def contact_view(request):
    if request.method == 'GET':
        try:
            # Load JSON data from the request body
            data = dict(request.GET)

            name = data.get('name')[0]
            email = data.get('email')[0]
            message = data.get('message')[0]

            if name and email and message:
                Contact.objects.create(name=name, email=email, message=message)

                return JsonResponse({
                    'success': True,
                    'type': 'success',
                    'message': 'پیام شما دریافت شد و پاسخ به ایمیل شما ارسال خواهد شد.'
                })
            else:
                return JsonResponse({
                    'success': False,
                    'type': 'error',
                    'message': 'لطفا همه فیلدها را پر کنید.'
                })
        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'type': 'error',
                'message': 'فرمت داده‌ها صحیح نیست.'
            }, status=400)
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
        'message': 'متد درخواستی صحیح نیست.'
    })

