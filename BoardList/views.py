from django.shortcuts import render, redirect
from Default.models import Board
from Default.models import Smember
from django.views.decorators.csrf import csrf_exempt
from django.db import connections
from django.http import HttpResponse
import datetime
# Create your views here.
def BoardListLoad(request):
    BoardList = Board.objects.all().order_by('boardno')
    print(BoardList)
    if (request.session['myID'] == None):
        return redirect('/')
    iID = request.session['myID']
    print(request.session['myID'])
    myResult = Smember.objects.filter(mid=iID)
    context = {
        "BoardList": BoardList,
        "Member": myResult
    }
    return render(request, "BoardList.html", context)
# return render(request,"BoardList.html",{'BoardList': BoardList})


def viewdata1(request, id):
    if (request.session['myID'] == None):
        return redirect('/')

    try:
        with connections['default'].cursor() as cursor:
            SQL = " Update  Board Set BoardCount = BoardCount " + " + 1 "
            SQL += " Where BoardNo=" + str(id)
            cursor.execute(SQL)

    except Exception as ex:
        print(' Error가 발생 했습니다', ex)
        return render(request, "BoardList.html")

    BoardData = Board.objects.all().get(boardno=id)

    context = {
        "BoardData": BoardData,
        "sID": request.session['myID']
    }
    return render(request, "ViewData.html", context)


def Itemdelete(request, id):
    if (id == None):
        return redirect('/List')

    Board.objects.filter(boardno=id).delete()
    return redirect('/List')


@csrf_exempt
def ItemSave(request):
    sNum = request.POST['iNum']
    sboardTitle = request.POST['iTitle']
    sboardContent = request.POST['iContent']

    iID = request.session['myID']
    now = datetime.datetime.now()
    if iID != None:
        try:
            with connections['default'].cursor() as cursor:
                SQL = " Update  Board Set BoardTitle='" + sboardTitle + "' , BoardContent='" + sboardContent + "' "
                SQL += " , Last_DT=getdate() "
                SQL += " Where BoardNo=" + sNum
                cursor.execute(SQL)
        except Exception as ex:
            print('저장에서 Error가 발생 했습니다', ex)
            return render(request, "List/List.html")
    # return response({"success": False, "msg": "에러입니다."})

    print(' 업데이트가 정상저장 되었습니다')
    return redirect('/List')
    # return HttpResponse(sNum)


def logout(request):
    request.session['myID'] = None
    return redirect('/')
