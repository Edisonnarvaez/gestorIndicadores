from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from rest_framework import viewsets
from ..models import Result
from ..serializers.result_serializer import ResultSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

class ResultViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    
    # Método para listar todos los resultados (GET)
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # Método para obtener un resultado específico (GET)
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # Método para crear un nuevo resultado (POST)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Creamos el resultado
        self.perform_create(serializer)

        # Obtenemos la instancia del resultado recién creado
        result = Result.objects.get(id=serializer.data['id'])

        # Calculamos el valor automáticamente basado en el método de cálculo del indicador
        result.calculate_indicator()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # Método para actualizar un resultado existente (PUT/PATCH)
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        
        # Actualizamos el resultado
        self.perform_update(serializer)
        
        # Recalculamos el valor automáticamente
        instance.calculate_indicator()

        return Response(serializer.data)

    # Método para eliminar un resultado (DELETE)
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
