from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from app.models import Phones, Review
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from statsmodels.compat import urlencode
from app.forms import UserRegistrationForm, ReviewForm


def view_index(request):

    data = Phones.objects.all().order_by('id')[3:]
    template = 'index.html'
    context = {'phones': data}
    return render(request, template, context)


def view_smartphones(request):

    data = Phones.objects.all()
    page_num = int(request.GET.get('page', 1))
    paginator = Paginator(data, 3)

    page = paginator.page(page_num)
    new_data = page.object_list

    if page.has_next() == True:
        next_page_url = reverse(view_smartphones) + '?%s' % urlencode({'page': page_num + 1})
    else:
        next_page_url = None

    if page.has_previous() == True:
        prev_page_url = reverse(view_smartphones) + '?%s' % urlencode({'page': page_num - 1})
    else:
        prev_page_url = None

    template = 'smartphones.html'

    context = {'phones': new_data,
               'current_page': page,
               'prev_page_url': prev_page_url,
               'next_page_url': next_page_url,
               }
    return render(request, template, context)


def view_phone(request, slug):

    template = 'phone.html'
    #product = get_object_or_404(Phones, slug=slug)
    #x = request.session.get('reviewed_products', [])
    #if request.method == 'POST' and slug not in x:
    #    form = ReviewForm(request.POST)
    #    text = request.POST.get("text")
    #    b = Review(text=text, product=product)
    #    b.save()
    #    x.append(slug)
    #    request.session['reviewed_products'] = x
    #else:
    #    form = ReviewForm()
    form = ReviewForm()
    phone = Phones.objects.get(slug=slug)
    context = {'phone': phone,
               'form': form}
    return render(request, template, context)


def view_empty_section(request):

    template = 'empty_section.html'
    context = {}
    return render(request, template, context)


def view_cart(request):

    template = 'cart.html'
    context = {}
    return render(request, template, context)


def view_login(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
    else:
        user_form = UserRegistrationForm()
    template = 'login.html'
    context = {'user_form': user_form}
    return render(request, template, context)
