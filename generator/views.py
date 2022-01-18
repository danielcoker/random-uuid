from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Vault


@api_view(['POST'])
def generate_uuid(request):
    Vault.objects.create()
    vaults = Vault.objects.values()
    uuids = {}

    for vault in enumerate(vaults):
        uuids[str(vault[1]['created_at'])] = vault[1]['uuid']

    return Response(uuids, status=status.HTTP_201_CREATED)
