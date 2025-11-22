from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PartnershipRequestSerializer

@method_decorator(csrf_exempt, name='dispatch')
class PartnershipRequestCreateView(APIView):
    authentication_classes = []  
    permission_classes = []      

    def post(self, request):
        serializer = PartnershipRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Заявка успешно отправлена"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
