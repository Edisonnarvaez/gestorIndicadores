from users.models.role import Role
from users.serializers.role_serializer import RoleSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets


# ViewSet para Role
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    # Búsqueda de roles por nombre
    @action(detail=False, methods=['get'])
    def search_by_name(self, request):
        name = request.query_params.get('name', None)
        if name:
            roles = Role.objects.filter(name__icontains=name)
            serializer = self.get_serializer(roles, many=True)
            return Response(serializer.data)
        return Response({"error": "Name parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
