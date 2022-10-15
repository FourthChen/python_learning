from django.shortcuts import render,HttpResponse

# Create your views here.

def test_view(request):
    print("执行业务逻辑中，计算一次多少钱。",request)
    print(dir(request))
    return HttpResponse("<h1 style='color:red'>500一次</h1>")

def login_view(reuqest):
    # html="""
    #
    # """
    # return HttpResponse(html)
    return render(reuqest,'form.html')