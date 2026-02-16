from django.http import JsonResponse
import requests

# Service endpoints - adjust these based on your Docker Compose setup
AUTH_SERVICE = "http://auth_service:8000"
STUDENT_SERVICE = "http://student_service:8000"
STAFF_SERVICE = "http://staff_service:8000"
FINANCE_SERVICE = "http://finance_service:8000"
NOTIFICATION_SERVICE = "http://notification_service:8000"
CURRICULUM_SERVICE = "http://curriculum_service:8000"


def auth_proxy(request):
    """Proxy requests to auth_service"""
    try:
        response = requests.request(
            method=request.method,
            url=f"{AUTH_SERVICE}{request.path.replace('/auth/', '/')}",
            headers=request.headers,
            data=request.body if request.method != 'GET' else None,
            params=request.GET,
            timeout=10
        )
        return JsonResponse(response.json(), status=response.status_code)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def students_proxy(request):
    """Proxy requests to student_service"""
    try:
        response = requests.request(
            method=request.method,
            url=f"{STUDENT_SERVICE}{request.path.replace('/students/', '/')}",
            headers=request.headers,
            data=request.body if request.method != 'GET' else None,
            params=request.GET,
            timeout=10
        )
        return JsonResponse(response.json(), status=response.status_code)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def staff_proxy(request):
    """Proxy requests to staff_service"""
    try:
        response = requests.request(
            method=request.method,
            url=f"{STAFF_SERVICE}{request.path.replace('/staff/', '/')}",
            headers=request.headers,
            data=request.body if request.method != 'GET' else None,
            params=request.GET,
            timeout=10
        )
        return JsonResponse(response.json(), status=response.status_code)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def finance_proxy(request):
    """Proxy requests to finance_service"""
    try:
        response = requests.request(
            method=request.method,
            url=f"{FINANCE_SERVICE}{request.path.replace('/finance/', '/')}",
            headers=request.headers,
            data=request.body if request.method != 'GET' else None,
            params=request.GET,
            timeout=10
        )
        return JsonResponse(response.json(), status=response.status_code)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def notifications_proxy(request):
    """Proxy requests to notification_service"""
    try:
        response = requests.request(
            method=request.method,
            url=f"{NOTIFICATION_SERVICE}{request.path.replace('/notifications/', '/')}",
            headers=request.headers,
            data=request.body if request.method != 'GET' else None,
            params=request.GET,
            timeout=10
        )
        return JsonResponse(response.json(), status=response.status_code)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


def curriculum_proxy(request):
    """Proxy requests to curriculum_service"""
    try:
        response = requests.request(
            method=request.method,
            url=f"{CURRICULUM_SERVICE}{request.path.replace('/curriculum/', '/')}",
            headers=request.headers,
            data=request.body if request.method != 'GET' else None,
            params=request.GET,
            timeout=10
        )
        return JsonResponse(response.json(), status=response.status_code)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)