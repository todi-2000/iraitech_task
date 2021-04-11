from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class MathFunctionView(APIView):
    def get(self, request):
        x1 = int(request.data.get("x"))
        n1 = int(request.data.get("n"))
        ans = 0
        previous = 1
        for i in range(n1):
            ans += previous*(1/x1)
            previous *= (1/x1)
        response_msg = {
            "ans": ans
        }
        return Response(response_msg)