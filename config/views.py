from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.db import connection

@api_view(['GET'])
def hello(request):
    return Response({"message": "hello world"})

@api_view(['GET'])
def health(request):
    try:
        connection.ensure_connection()
        return Response({"database": "connected"})
    except Exception as e:
        return Response({"database": str(e)})

