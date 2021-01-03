from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .views import *


urlpatterns = [
    path(
    	'find_centers/',
    	find_centers,
    	name='find_centers'
    	),
    path(
        'get_info_about_exam/',
        get_info_about_exam,
        name='get_info_about_exam'),
    path(
        'fetch_address_of_exam_center/',
        fetch_address_of_exam_center,
        name='fetch_address_of_exam_center'),
    path(
        'fetch_course_info/',
        fetch_course_info,
        name='fetch_course_info'),
    path(
        'fetch_syllabus_for_exam/',
        fetch_syllabus_for_exam,
        name='fetch_syllabus_for_exam'),
    path(
        'fetch_fee_for_exam/',
        fetch_fee_for_exam,
        name='fetch_fee_for_exam'),
    path(
        'fetch_fee_for_course/',
        fetch_fee_for_course,
        name='fetch_fee_for_course'),
    path(
        'fetch_branches_in_campus/',
        fetch_branches_in_campus,
        name='fetch_branches_in_campus'),
    path(
        'fetch_campus_from_branch/',
        fetch_campus_from_branch,
        name='fetch_campus_from_branch')
    ]
