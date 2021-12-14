from rest_framework.views import APIView
from rest_framework.response import Response

from .models import AiAnalysisLog
from .serializer import AiAnalysisLogSerializer

from . import validation

class AiAnalysisLogList(APIView):
    def get(self, request):
        ai_analysis_log = AiAnalysisLog.objects.all()
        serializer = AiAnalysisLogSerializer(ai_analysis_log, many=True)
        return Response(serializer.data)

    def post(self, request):
        validator = validation.Forge(request.data)
        if not validator.run():
            response = {
                "success" : validator.get_success(),
                "message" : validator.get_message(),
                "estimated_data" : {}
            }
            return Response(response, validator.get_http_status())

        response = {
            "success" : validator.get_success(),
            "message" : validator.get_message(),
            "estimated_data" : {
                "class" : 3,
                "confidence" : 0.8683
            }
        }

        return Response(response, validator.get_http_status())
