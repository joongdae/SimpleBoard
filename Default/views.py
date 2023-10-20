from django.shortcuts import render , redirect
from django.views.decorators.csrf import csrf_exempt
from Default.models import Smember
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
import json

# Create your views here.

def DefaultLoad(request):
    return render(request,'Default.html')

@csrf_exempt
def LoginClick(request):
    # POST 요청일 때

    jsonObject = json.loads(request.body.decode('utf-8'))
    iID=jsonObject['sID']
    iPW=jsonObject['sPW']

    try:
        myResult = Smember.objects.filter(mid=iID, mpw=iPW).count()
    except Exception as ex:
        print('에러가 발생 했습니다', ex)

    if(myResult==1):
        request.session['myID'] = iID  # ☆ 세션 등록 ☆
        # return render(request, "Default.html", context)

        return JsonResponse({'msg':'Success'})
    else:
        return JsonResponse({'msg':'Fail'})
