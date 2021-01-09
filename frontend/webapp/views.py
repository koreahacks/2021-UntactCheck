from django.shortcuts import render

# urls에서 요청이 오면 first_view로 오는데, 이 때 ~.html을 rendering 해줘라
def first_view(request):
    return render(request, 'webapp/first_view.html', {})