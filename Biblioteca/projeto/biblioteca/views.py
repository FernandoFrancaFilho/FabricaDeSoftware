from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Livro
from .serializers import LivroSerializer

@csrf_exempt
def livro_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        livro = Livro.objects.all()
        serializer = LivroSerializer(livro, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LivroSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def livro_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        livro = Livro.objects.get(pk=pk)
    except Livro.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LivroSerializer(livro)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LivroSerializer(livro, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        livro.delete()
        return HttpResponse(status=204)
