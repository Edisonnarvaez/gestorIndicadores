from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

# ViewSet para User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Filtrar usuarios por el estado (activo/inactivo)
    @action(detail=False, methods=['get'])
    def active(self, request):
        active_users = User.objects.filter(status=True)
        serializer = self.get_serializer(active_users, many=True)
        return Response(serializer.data)

    # Búsqueda de usuarios por nombre de usuario
    @action(detail=False, methods=['get'])
    def search_by_username(self, request):
        username = request.query_params.get('username', None)
        if username:
            users = User.objects.filter(username__icontains=username)
            serializer = self.get_serializer(users, many=True)
            return Response(serializer.data)
        return Response({"error": "Username parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

# ViewSet para User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Actualizar el estado del usuario
    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        user = self.get_object()
        status = request.data.get('status', None)
        if status is not None:
            user.status = status
            user.save()
            return Response({'status': 'User status updated'})
        return Response({'error': 'Status is required'}, status=status.HTTP_400_BAD_REQUEST)
# ViewSet para User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Resetear el password del usuario
    @action(detail=True, methods=['post'])
    def reset_password(self, request, pk=None):
        user = self.get_object()
        new_password = request.data.get('new_password', None)
        if new_password:
            user.set_password(new_password)
            user.save()
            return Response({'status': 'Password updated successfully'})
        return Response({'error': 'New password is required'}, status=status.HTTP_400_BAD_REQUEST)
# ViewSet para User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Desactivar un usuario
    @action(detail=True, methods=['post'])
    def deactivate(self, request, pk=None):
        user = self.get_object()
        user.status = False
        user.save()
        return Response({'status': 'User deactivated'})

    # Activar un usuario
    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        user = self.get_object()
        user.status = True
        user.save()
        return Response({'status': 'User activated'})
# ViewSet para User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Obtener la última fecha de login de un usuario
    @action(detail=True, methods=['get'])
    def last_login(self, request, pk=None):
        user = self.get_object()
        return Response({'lastLogin': user.lastLogin})
