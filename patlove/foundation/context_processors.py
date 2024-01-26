def tenant_name(request):
    foundation = request.tenant
    return {
        'foundation_name': foundation.name
    }