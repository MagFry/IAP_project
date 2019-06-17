from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Branch_Offices
from .serializers import Branch_OfficesSerializer


@csrf_exempt
def branch_offices_list(request):
    """
    List all branch offices.
    """
    if request.method == 'GET':
        branch_offices = Branch_Offices.objects.all()
        serializer = Branch_OfficesSerializer(branch_offices, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def add_branch_office(request):
    """
    Create new branch office.
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Branch_OfficesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(request, status=400, safe=False)


@csrf_exempt
def branch_offices_detail(request, pk):
    """
    Retrieve, update or delete a branch office.
    """
    try:
        branch_offices = Branch_Offices.objects.get(branch_office_id=pk)
    except Branch_Offices.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = Branch_OfficesSerializer(branch_offices)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = Branch_OfficesSerializer(branch_offices, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        branch_offices.delete()
        return HttpResponse(status=204)