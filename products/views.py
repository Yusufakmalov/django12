from django.shortcuts import render

from products.models import ProductModel



def index_html(request):
     return render(request, 'index.html')
def article_page(request):
     return render(request, 'article.html')


def login_page(request):
     return render(request, 'login.html')