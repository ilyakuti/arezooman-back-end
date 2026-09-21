from django.shortcuts import render, get_object_or_404
from .models import *


def homepage(request):
    context = {
        'categories': Category.objects.all(),
        'wishes': Wishes.objects.all()[:6],
        'angels': Person.objects.filter(role='angel')[:6],
        'stories': Story.objects.all(),
        'pending_wishes': Wishes.objects.count(),
        'total_angels': Person.objects.filter(role='angel').count(),
        'fulfilled': Wishes.objects.filter(progress=100).count(),
    }
    return render(request, 'index.html', context)

def wish_detail(request, pk):
    wish = get_object_or_404(Wishes, pk=pk)
    return render(request, 'wish_detail.html', {'wish': wish})


def angel_detail(request, pk):
    angel = get_object_or_404(Person, pk=pk)
    return render(request, 'angel_detail.html', {'angel': angel})


def category_wishes(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'category_wishes.html', {
        'category': category,
        'wishes': Wishes.objects.filter(category=category),
    })