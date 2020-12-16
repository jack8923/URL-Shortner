from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import shortURL
import random, string
import datetime
# Create your views here.


@login_required(login_url='/login')
def dashboard(request):
    current = request.user
    urls = shortURL.objects.filter(user=current)
    return render(request, 'dashboard.html', {'urls':urls})


def randomCode():
    return ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(6))


@login_required(login_url='/login')
def edit(request, pk=None):
    current = request.user
    urls = shortURL.objects.filter(user=current)
    to_edit_url = shortURL.objects.get(id=pk)
    if request.method == 'POST':
        if request.POST['short']:
            to_edit_url.short_url = request.POST['short']
            to_edit_url.save()
            return render(request, 'dashboard.html', {'urls': urls})
        else:
            generated_code = False
            while not generated_code:
                short = randomCode()
                to_edit_url.short_url = short
                to_edit_url.save()
                return render(request, 'dashboard.html', {'urls': urls})
    else:
        return render(request, 'edit.html', {'url': to_edit_url})


@login_required(login_url='/login')
def generate(request):
    if request.method == 'POST':
        if request.POST['original'] and request.POST['short']:
            current = request.user
            original = request.POST['original']
            short = request.POST['short']

            if len(short) < 4:
                messages.error(request, 'Length of Short URL should be greater than 4')
                return redirect(dashboard)

            exist = shortURL.objects.filter(short_url=short)

            if not exist:
                new = shortURL(user=current, original_url=original, short_url=short)
                new.save()
                return redirect(dashboard)
            else:
                messages.error(request, 'Short URL Already Exists')
                return redirect(dashboard)

        elif request.POST['original']:
            current = request.user
            original = request.POST['original']
            generated_code = False
            while not generated_code:
                short = randomCode()
                exist = shortURL.objects.filter(short_url=short)

                if not exist:
                    new = shortURL(user=current, original_url=original, short_url=short)
                    new.save()
                    return redirect(dashboard)
                else:
                    continue
        else:
            messages.error(request, 'Empty Fields')
            return redirect(dashboard)
    else:
        return redirect(dashboard)


def home(request, query=None):
    if not query or query is None:
        return render(request, 'home.html')
    else:
        try:
            exist = shortURL.objects.get(short_url=query)
            exist.visits = exist.visits + 1
            exist.last_visited = datetime.datetime.now()
            exist.save()
            return redirect(exist.original_url)
        except shortURL.DoesNotExist:
            return render(request, 'home.html', {'error': "error"})


@login_required(login_url='/login')
def delete(request):
    if request.method == "POST":
        short = request.POST['delete']
        try:
            exist = shortURL.objects.filter(short_url=short)
            exist.delete()
            return redirect(dashboard)
        except shortURL.DoesNotExist:
            return redirect(home)
    else:
        return redirect(home)


@login_required(login_url='/login')
def stats(request, query=None):
    if not query or query is None:
        return render(request, 'home.html', {'error : Invalid Query Passed'})
    else:
        try:
            exist = shortURL.objects.get(short_url=query)
            current = request.user
            return render(request, 'details.html', {'url': exist, 'user': current})
        except shortURL.DoesNotExist:
            return render(request, 'home.html', {'error': "error"})