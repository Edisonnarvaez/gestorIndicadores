from companies.models.company import Company
from companies.serializers.company_serializer import CompanySerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


# ViewSet para Company
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def get_queryset(self):
        """
        Sobrescribe el método para hacer filtros personalizados si es necesario.
        """
        queryset = Company.objects.all()
        # Puedes agregar lógica de filtrado aquí si es necesario
        return queryset
    
    # Método para listar todas las compañías (GET)
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # Método para obtener una compañía específica (GET)
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # Método para crear una nueva compañía (POST)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # Método para actualizar una compañía existente (PUT/PATCH)
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    # Método para eliminar una compañía (DELETE)
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Método personalizado para activar una compañía (POST)
    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        company = self.get_object()
        company.is_active = True
        company.save()
        return Response({'status': 'Company activated'})

