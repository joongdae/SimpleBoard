from django.shortcuts import render, redirect
from Default.models import Board
from Default.models import Smember
from django.views.decorators.csrf import csrf_exempt
from django.db import connections
from django.http import HttpResponse
import datetime

# Create your views here.

def writeboard1(request):
    print("List_WriteBoard:")
    #BoardData = Board.objects.all().get(boardno=id)
    context={ 'myID': request.session['myID'] }
    return render(request, "WriteBoard.html",context)



@csrf_exempt
def Board_Insert(request):

    sboardTitle = request.POST['iTitle']
    sboardContent = request.POST['iContent']
    iID=request.session['myID']
    now = datetime.datetime.now()
    if iID != "":
        try:
            rows = Board.objects.create(boardtitle=sboardTitle, boardcontent=sboardContent, mid=iID, boarddate=now ,boardcount=0)
        except Exception as ex:
            print('저장에서 Error가 발생 했습니다', ex)
            return redirect("/List")

    print('게시판글쓰기가 정상저장 했습니다')
    #return render(request, "List/List.html")
    return redirect("/List")

