from django.shortcuts import render
from django.core.cache import cache
import os, json
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import *

# Create your views here.
@csrf_exempt
def get_info_about_exam(request):
    if request.method == 'POST':
        exam_type = request.POST['exam_type']
        # print(exam_type)
        database = 'default'
        try:
        	obj = BitsEnteranceExamInformation.objects.using(database).get(exam_type=exam_type)
        	response = {
        		'success':True,
        		'information' : obj.info
        	}
        except:
        	response = {'success':False}
    else:
    	response = {'success':False}
    return JsonResponse(response)


@csrf_exempt
def find_centers(request):
    if request.method == 'POST':
        exam_type = request.POST['exam_type']
        location_state = request.POST['location_state']

        database = 'default'

        try:
            obj = BitsEnteranceExamCenters.objects.using(database).filter(exam_type=exam_type).filter(state__iexact=location_state)
            # print(obj[0].examcentercity)
            centers = []
            for obj1 in obj:
            	centers.append(obj1.examcentercity)
            centers = list(dict.fromkeys(centers))
            response = {
        		'success':True,
        		'centers' : centers
        	}
        except:
        	response = {'success':False}
    else:
    	response = {'success':False}
    return JsonResponse(response)

@csrf_exempt
def fetch_address_of_exam_center(request):
    if request.method == 'POST':
        exam_type = request.POST['exam_type']
        location_state = request.POST['location_state']
        location_city = request.POST['location_city']

        database = 'default'

        try:
            # print(0)
            obj = BitsEnteranceExamCenters.objects.using(database).filter(exam_type=exam_type).filter(examcentercity__iexact = location_city)
            # print(obj[0].examcentercity)
            addr = []
            # print(obj)
            for obj1 in obj:
                # print(obj1.examcentercity)
                # print(obj1.examcenteraddress)
                addr.append(obj1.examcenteraddress)
            # print(2)
            response = {
                'success':True,
                'addr' : addr
            }
        except Exception as e:
            print(e)
            response = {'success':False}
    else:
        response = {'success':False}
    return JsonResponse(response)

@csrf_exempt
def fetch_course_info(request):
    if request.method == 'POST':
        course = request.POST['course']
        # print(exam_type)
        database = 'default'
        try:
            obj = BitsCourseInformation.objects.using(database).get(course__iexact=course)
            # print(obj)
            response = {
                'success':True,
                'information' : obj.info
            }
        except:
            response = {'success':False}
    else:
        response = {'success':False}
    return JsonResponse(response)

@csrf_exempt
def fetch_syllabus_for_exam(request):
    if request.method == 'POST':
        exam_type = request.POST['exam_type']
        try:
            branch = request.POST['branch']
        except:
            branch = None
        # print(exam_type)
        database = 'default'
        try:
            obj = BitsExamSyllabus.objects
            if exam_type == 'BITSAT':
                obj = BitsExamSyllabus.objects.using(database).get(exam_type=exam_type)
            elif exam_type == 'BITSHD':
                obj = BitsExamSyllabus.objects.using(database).filter(exam_type=exam_type).get(branch__iexact = branch)
            # print(obj)
            response = {
                'success':True,
                'syllabus' : obj.syllabus
            }
        except Exception as e:
            print(e)
            response = {'success':False}
    else:
        response = {'success':False}
    return JsonResponse(response)

@csrf_exempt
def fetch_fee_for_exam(request):
    if request.method == 'POST':
        exam_type = request.POST['exam_type']
        # print(exam_type)
        database = 'default'
        try:
            obj = BitsExamFee.objects.using(database).get(exam_type=exam_type)
            response = {
                'success':True,
                'fee' : obj.fee
            }
        except:
            response = {'success':False}
    else:
        response = {'success':False}
    return JsonResponse(response)

@csrf_exempt
def fetch_fee_for_course(request):
    if request.method == 'POST':
        course = request.POST['course']
        # print(exam_type)
        database = 'default'
        try:
            obj = BitsCourseFee.objects.using(database).get(course__iexact=course)
            response = {
                'success':True,
                'fee' : obj.fee
            }
        except:
            response = {'success':False}
    else:
        response = {'success':False}
    return JsonResponse(response)


@csrf_exempt
def fetch_branches_in_campus(request):
    if request.method == 'POST':
        course = request.POST['course']
        campus = request.POST['campus']
        # print(exam_type)
        database = 'default'
        try:
            obj = None
            if campus == 'All':  
                obj = BitsBranchCampusMapping.objects.using(database).filter(course__iexact=course)
            else:
                obj = BitsBranchCampusMapping.objects.using(database).filter(course__iexact=course).filter(campus__iexact=campus)
            campus_branch_mapping = {}
            for obj1 in obj:
                if obj1.campus not in campus_branch_mapping:
                    campus_branch_mapping[obj1.campus] = []
                campus_branch_mapping[obj1.campus].append(obj1.branch)
            response = {
                'success':True,
                'campus_branch_mapping' : campus_branch_mapping
            }
        except Exception as e:
            print(e)
            response = {'success':False}
    else:
        response = {'success':False}
    return JsonResponse(response)


@csrf_exempt
def fetch_campus_from_branch(request):
    if request.method == 'POST':
        course = request.POST['course']
        branch = request.POST['branch']
        # print(exam_type)
        database = 'default'
        try:
            obj = BitsBranchCampusMapping.objects.using(database).filter(course__iexact=course).filter(branch__iexact=branch)
            campus =[]
            for obj1 in obj:
                campus.append(obj1.campus)
            response = {
                'success':True,
                'campus' : campus
            }
        except Exception as e:
            print(e)
            response = {'success':False}
    else:
        response = {'success':False}
    return JsonResponse(response)
