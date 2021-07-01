from services.productionplan.serializers import ProductionplanSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status



class ProductionplanViewSet(
    GenericViewSet
):
    serializer_class = ProductionplanSerializer

    def create(self, request, format=None):
        serializer = ProductionplanSerializer(data = request.data)
        if serializer.is_valid():
            return Response({}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    # def list(self, request, format=None):
    #     return Response({}, status=status.HTTP_200_OK)
