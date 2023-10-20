from django.shortcuts import render , redirect
from django.views.decorators.csrf import csrf_exempt
from Default.models import Smember
from django.contrib.auth import authenticate, login
import datetime
from django.http import JsonResponse
import json

def MemberJoinLoad(request):
    return render(request,'Join.html')


@csrf_exempt
def Confirm1(request):
    # POST 요청일 때

    jsonObject = json.loads(request.body.decode('utf-8'))
    iID = jsonObject['sID']
    #iPW=jsonObject['sPW']
    print("MemJoin_Confirm1.............")

    try:
        myResult = Smember.objects.filter(mid=iID).count()
    except Exception as ex:
        print('에러가 발생 했습니다', ex)
        return JsonResponse({'msg': 'error'})

    if(myResult > 0):

        return JsonResponse({'msg':'disable'})
    else:
        return JsonResponse({'msg':'enable'})

@csrf_exempt
def Member_Insert(request):

    jsonObject = json.loads(request.body.decode('utf-8'))

    iID = jsonObject['sID']
    iPW = jsonObject['sPW']
    iName = jsonObject['sName']
    iAddr = jsonObject['sAddr']
    iRemark = jsonObject['sRemark']
    iAlias = jsonObject['sAlias']
    iBirthday = jsonObject['sBirthday']
    iPhone = jsonObject['sPhone']

    now = datetime.datetime.now()
    myResult = 0
    try:
        myResult = Smember.objects.filter(mid=iID).count()
    except Exception as ex:
        print('에러가 발생 했습니다', ex)
        return JsonResponse({'msg': 'error'})

    if myResult > 0:
        context = {
            "msg": "이미 등록된 아이디가 있습니다."
        }
        return JsonResponse({'msg': 'same_as'})

    try:
        rows = Smember.objects.create(mid=iID, mname=iName, mpw=iPW, malias=iAlias, mbirth=iBirthday, maddr=iAddr,
                                      mphone=iPhone, mmemo=iRemark, inst_dt=now)
    except Exception as ex:
        context = {
            "msg": "저장에서 Error가 발생 했습니다"
        }
        return JsonResponse({'msg': 'error'})

    return JsonResponse({'msg': 'enable'})
