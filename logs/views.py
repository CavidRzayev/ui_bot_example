from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from logs.serializers import LogSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class AddLogAPIView(APIView):
    serializer_class = LogSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Transaction logged successfully!", "data": request.data})
