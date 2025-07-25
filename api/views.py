from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WheelSpecification
from .serializers import WheelSpecificationSerializer, BogieChecksheetSerializer

# ------------------------
# Wheel Specification View
# ------------------------

class WheelSpecificationView(APIView):
    """
    Handles both POST (create) and GET (filtered list) requests
    for Wheel Specification form.
    """

    def post(self, request):
        serializer = WheelSpecificationSerializer(data=request.data)
        if serializer.is_valid():
            wheel_spec = serializer.save()
            return Response({
                "success": True,
                "message": "Wheel specification submitted successfully.",
                "data": {
                    "formNumber": wheel_spec.form_number,
                    "submittedBy": wheel_spec.submitted_by,
                    "submittedDate": wheel_spec.submitted_date,
                    "status": wheel_spec.status
                }
            }, status=status.HTTP_201_CREATED)

        return Response({
            "success": False,
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """
        Accepts optional filters:
        ?formNumber=...&submittedBy=...&submittedDate=...
        """
        filters = {
            'form_number': request.GET.get('formNumber'),
            'submitted_by': request.GET.get('submittedBy'),
            'submitted_date': request.GET.get('submittedDate')
        }
        # Remove any None values from filters
        filters = {k: v for k, v in filters.items() if v is not None}

        queryset = WheelSpecification.objects.filter(**filters)
        serializer = WheelSpecificationSerializer(queryset, many=True)

        return Response({
            "success": True,
            "message": "Filtered wheel specification forms fetched successfully.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)

# ------------------------
# Bogie Checksheet View
# ------------------------

class BogieChecksheetCreateView(APIView):
    """
    Handles POST request for Bogie Checksheet form submission.
    """

    def post(self, request):
        serializer = BogieChecksheetSerializer(data=request.data)
        if serializer.is_valid():
            bogie_obj = serializer.save()
            return Response({
                "success": True,
                "message": "Bogie checksheet submitted successfully.",
                "data": {
                    "formNumber": bogie_obj.form_number,
                    "inspectionBy": bogie_obj.inspection_by,
                    "inspectionDate": bogie_obj.inspection_date,
                    "status": bogie_obj.status
                }
            }, status=status.HTTP_201_CREATED)

        return Response({
            "success": False,
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
