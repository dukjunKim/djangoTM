from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import viewsets, status
from rest_framework import permissions

from .models import TmabTbKt14
from .models import TmabTbKt10
from django.core.paginator import Paginator
from .serializers import tmabtbkt14Serializer
from .serializers import tmabtbkt10Serializer

# Create your views here.



class TmabTbKt14View(APIView):
    def get(self, request):
        return Response("ok", status=200)

    def post(self, request):
        tmabtbkt14_Serializer = tmabtbkt14Serializer(data=request.data)

        if tmabtbkt14_Serializer.is_valid():
            tmabtbkt14_Serializer.save()
            return Response(tmabtbkt14_Serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(tmabtbkt14_Serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, **kwargs): # get의 parameter가 되는 kt14_id는 blog_urls에서 설정 받으며, (int:kt14_id) 그 값을 appl_no 필드와 비교하여 그 값을 얻어온다.
        if kwargs.get('kt14_id') is None:       # 별 다른 주소가 뜨지 않으면 그냥 얘가 실행된다 다 뜨는 거
            kt14_queryset = TmabTbKt14.objects.all()
            kt14_queryset_serializer = tmabtbkt14Serializer(kt14_queryset, many=True)
            return Response(kt14_queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            kt14_id = kwargs.get('kt14_id')
            tmabtbkt14_Serializer = tmabtbkt14Serializer(TmabTbKt14.objects.get(appl_no=kt14_id))
            return Response(tmabtbkt14_Serializer.data, status=status.HTTP_200_OK)


    def put(self, request, **kwargs):
        if kwargs.get('kt14_id') is None:
            return Response('invalid request', status=status.HTTP_400_BAD_REQUEST)
        else:
            kt14_id = kwargs.get('kt14_id')
            kt14_object = TmabTbKt14.objects.get(appl_no=kt14_id)
            update_tmabtabkt14_Serializer = tmabtbkt14Serializer(kt14_object, data=request.data)
            if update_tmabtabkt14_Serializer.is_valid():
                update_tmabtabkt14_Serializer.save()
                return Response(update_tmabtabkt14_Serializer.data, status=status.HTTP_200_OK)
            else:
                return Response('invalid request', status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        if kwargs.get('kt14_id') is None:
            return Response('invalid request', status=status.HTTP_400_BAD_REQUEST)
        else:
            kt14_id = kwargs.get('kt14_id')
            kt14_object = TmabTbKt14.objects.get(appl_no=kt14_id)
            kt14_object.delete()
            return Response('test ok', status=status.HTTP_200_OK)

#kt_10 작업
class TmabTbKt10View(APIView):
    def get(self, request):
        return Response("ok", status=200)

    def post(self, request):
        tmabtbkt10_Serializer = tmabtbkt10Serializer(data=request.data)

        if tmabtbkt10_Serializer.is_valid():
            tmabtbkt10_Serializer.save()
            return Response(tmabtbkt10_Serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(tmabtbkt10_Serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, **kwargs): # get의 parameter가 되는 kt14_id는 blog_urls에서 설정 받으며, (int:kt14_id) 그 값을 appl_no 필드와 비교하여 그 값을 얻어온다.
        if kwargs.get('kt10_id') is None:       # 별 다른 주소가 뜨지 않으면 그냥 얘가 실행된다 다 뜨는 거
            kt10_queryset = TmabTbKt10.objects.all()
            kt10_queryset_serializer = tmabtbkt10Serializer(kt10_queryset, many=True)
            return Response(kt10_queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            kt10_id = kwargs.get('kt10_id')
            tmabtbkt10_Serializer = tmabtbkt10Serializer(TmabTbKt10.objects.get(appl_no=kt10_id))
            return Response(tmabtbkt10_Serializer.data, status=status.HTTP_200_OK)


    def put(self, request, **kwargs):
        if kwargs.get('kt10_id') is None:
            return Response('invalid request', status=status.HTTP_400_BAD_REQUEST)
        else:
            kt10_id = kwargs.get('kt10_id')
            kt10_object = TmabTbKt10.objects.get(appl_no=kt10_id)
            update_tmabtbkt10_Serializer = tmabtbkt10Serializer(kt10_object, data=request.data)
            if update_tmabtbkt10_Serializer.is_valid():
                update_tmabtbkt10_Serializer.save()
                return Response(update_tmabtbkt10_Serializer.data, status=status.HTTP_200_OK)
            else:
                return Response('invalid request', status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        if kwargs.get('kt10_id') is None:
            return Response('invalid request', status=status.HTTP_400_BAD_REQUEST)
        else:
            kt10_id = kwargs.get('kt10_id')
            kt10_object = TmabTbKt10.objects.get(appl_no=kt10_id)
            kt10_object.delete()
            return Response('test ok', status=status.HTTP_200_OK)



'''
def address_list(request):
    if request.method == 'GET':
        query_set = TmabTbKt14.objects.all()
        serializer = tmabtbkt14Serializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = tmabtbkt14Serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def address(request, pk):
    obj = TmabTbKt14.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = tmabtbkt14Serializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = tmabtbkt14Serializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)

'''

def index(request):
    posts = TmabTbKt14.objects.all()

    return render(
        request, 'blog/index.html', {
            'posts': posts
        }
    )

