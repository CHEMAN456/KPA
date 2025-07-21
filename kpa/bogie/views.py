from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import  status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView,ListAPIView
from .models import BogieChecksheet, WheelSpecification
from .serializers import Bogie_Checksheet,Wheel_Specification


# Create your views here.

# POST /api/forms/bogie-checksheet

class BogieChecksheetView(CreateAPIView):
    queryset = BogieChecksheet.objects.all()
    serializer_class = Bogie_Checksheet  

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)  
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer) 

        response_data = {
            "success": True,
            "message": "Bogie checksheet submitted successfully.",
            "url": request.path,
            "method": request.method,
            "request_body": request.data,
            "data": {
                "formNumber": serializer.data.get("formNumber"),
                "inspectionBy": serializer.data.get("inspectionBy"),
                "inspectionDate": serializer.data.get("inspectionDate"),
                "status": "Saved"
            }
        }
        return Response(response_data, status=status.HTTP_201_CREATED)
    

# GET /api/forms/wheel-specifications  

class WheelSpecificationListView(ListAPIView):
    serializer_class = Wheel_Specification

    def get_queryset(self):
        queryset = WheelSpecification.objects.all()
        form_number = self.request.query_params.get('formNumber')
        submitted_by = self.request.query_params.get('submittedBy')
        submitted_date = self.request.query_params.get('submittedDate')

        if form_number:
            queryset = queryset.filter(formNumber=form_number)
        if submitted_by:
            queryset = queryset.filter(submittedBy=submitted_by)
        if submitted_date:
            queryset = queryset.filter(submittedDate=submitted_date)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response({
            "success": True,
            "message": "Filtered Results fetched successfully.",
            "url": request.get_full_path(),
            "method": request.method,
            "filters": request.query_params,
            "data": serializer.data
        })
        

class LoginAPIView(APIView):
    
    def post(self,request):
        
        phone = request.data.get('phone')
        password = request.data.get('password')
        
        user  = authenticate(username=phone,password=password)
        
        if user is not None:
            
            return Response({
                "success":True,
                "message":"Log In Successful",
                "user_id": user.id,
                "phone": user.username     
            },status = status.HTTP_200_OK )
        else:
            return Response({
                "success":False,
                "message":"Invalid Credentials"    
            },status=status.HTTP_401_UNAUTHORIZED)    
            