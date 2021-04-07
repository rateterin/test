from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from my_test_webservice.models import Links
from my_test_webservice.serializers import LinksSerializer


@api_view(['GET', 'POST'])
def link_minimizer(request):
    if request.method == 'GET':
        return Response(status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = LinksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = {'status': 'ok', 'result': serializer.data['short']}
            return Response(res, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', ])
def link_deminimizer(request):
    __test = request.path[-12:]
    try:
        link = Links.objects.get(short=__test)
    except Exception as e:
        if e.args[0] == 'Links matching query does not exist.':
            res = {'status': 'error', 'result': 'link not found'}
            return Response(res)
        else:
            return Response('error', status=status.HTTP_400_BAD_REQUEST)
    if link.active:
        res = {'status': 'error', 'result': 'link not active'}
        return Response(res)
    link.active = True
    link.save()
    res = {'status': 'ok', 'result': link.link}
    return Response(res, status=status.HTTP_200_OK)
