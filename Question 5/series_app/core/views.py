import requests
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def home(request):
    try:
        x1 = request.GET['x']
        n1  = request.GET['n']
        payload = {
            "x": int(x1),
            "n": int(n1)
        }
        headers = {
            "Authorization": 'Token dcca117fe2ab39f244b07e1ee0a7155b4d67b871'
        }
        r = requests.get('http://127.0.0.1:8000/api/v1/calculate', data=payload, headers=headers)
        if r.status_code == 401:
            messages.warning(request, "Authorization token wrong")
        else:
            data  = r.json()
            ans = data["ans"]
            messages.success(request,f'Ans is {ans}')
    except:
        pass
    return render(request,"core/home.html")