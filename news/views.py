from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm

# Create your views here.
def index(request):

    news = News.objects.all()

    context = {
        'news' : news,
    }

    return render(request, 'index.html', context)

def create(request):
    #모든 경우의수
    # - GET : form을 만들어서 html 문서를 사용자에게 리턴 (1~4의 과정)
    # - POST invalid data (검증 실패, 5~9의 과정)
    # - POST valid data (검증 성공, 10~14의 과정)

    # 5, 10. POST 요청
    if request.method == 'POST':
        # 6,11. 사용자 입력 데이터(request.POST)를 담아서 form을 생성
        form = NewsForm(request.POST)
        # 7, 12. 검증 성공, 실패 분기 나눠주기
        if form.is_valid():
            # 13. form을 저장
            form.save()
            # 14. index 페이지로 redirect
            return redirect('news:index')
    # 1. GET 요청
    else:
        # 2. 비어있는 form 생성
        form = NewsForm()
        # 3,8. context dict에 POST 요청
        context = {
            'form' : form,
        }
        # 4,9. create.html을 랜더링
        return render(request, 'create.html', context)

def delete(request, id):
    if request.method == 'POST':
        news = News.objects.get(id=id)
        news.delete()
    return redirect('news:index')

def update(request, id):
    news = News.objects.get(id=id)

    if request.method == 'POST':
        form = NewsForm(request.POST, instance=news)

        if form.is_valid():
            form.save()
            return redirect('news:index')
    else:
        form = NewsForm(instance=news)
    
    context = {
        'form' : form,
    }

    return render(request, 'update.html', context)

    


# def create(request):
#     #(2)
#     if request.method == 'POST':
#         form = NewsForm(request.POST)

#         #(2-1)
#         if form.is_valid():
#             form.save()
#             return redirect('news:index')
#         #(2-2)
#         else:
#             # form = NewsForm(request.POST)
#             context = {
#                 'form' : form,
#             }
#             return render(request, 'create.html', context)


#     #(1)
#     else:
#         form = NewsForm()

#         context = {
#             'form' : form,
#         }
#         return render(request, 'create.html', context)



