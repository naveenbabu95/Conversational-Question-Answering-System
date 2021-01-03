
<!-- *******************STORY FOR EXAM INFO******************** -->
## story1: get inforamtion about exam + exam center
* greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Adam"}
    - utter_how_can_i_help
* need_more_info
    - utter_ask_exam_type
* get_exam_type{"exam_type":"BITSHD"}
    - action_get_info_about_exam
    - utter_ask_need_exam_center
* affirm
    - utter_ask_location_state
* get_location_state{"location_state" : "Maharashtra"}
    - bits_enterance_examcenter_search_in_state
    - form{"name": "bits_enterance_examcenter_search_in_state"}
    - form{"name": null}
    - utter_slots_values
    - action_search_exam_centers
* thankyou
    - utter_noworries


## story2: get inforamtion about exam happy path
* greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Eve"}
    - utter_how_can_i_help
* need_more_info{"exam_type":"BITSHD"}
    - action_get_info_about_exam
    - utter_ask_need_exam_center
* deny
    - utter_noworries


## story3: get inforamtion about exam directly + affirm for exam center
* greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Eve"}
    - utter_how_can_i_help
* need_more_info{"location_state":"Maharashta", "exam_type":"BITSHD"}
    - action_get_info_about_exam
    - utter_ask_need_exam_center
* affirm
    - bits_enterance_examcenter_search_in_state
    - form{"name": "bits_enterance_examcenter_search_in_state"}
    - form{"name": null}
    - utter_slots_values
    - action_search_exam_centers
* thankyou
    - utter_noworries

## story4: get inforamtion about exam directly
* greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Eve"}
    - utter_how_can_i_help
* need_more_info{"exam_type":"BITSHD"}
    - action_get_info_about_exam
    - utter_ask_need_exam_center
* deny
    - utter_noworries

## story5: get inforamtion about exam + change exam type
* greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Eve"}
    - utter_how_can_i_help
* need_more_info{"exam_type":"BITSAT"}
    - action_get_info_about_exam
* change_exam_type{"exam_type":"BITSHD"}
    - action_get_info_about_exam
    - utter_ask_need_exam_center
* deny
    - utter_noworries

## story6: get info without greeting
* need_more_info{"exam_type":"BITSHD"}
    - action_get_info_about_exam
    - utter_ask_need_exam_center
* deny
    - utter_noworries

## story7: get info without greeting
* need_more_info
    - utter_ask_exam_type
* get_exam_type{"exam_type":"BITSHD"}
    - action_get_info_about_exam
    - utter_ask_need_exam_center
* deny
    - utter_noworries

## story6: get inforamtion about exam + change exam type
* greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Eve"}
    - utter_how_can_i_help
* need_more_info{"exam_type":"BITSHD"}
    - action_get_info_about_exam
    - utter_ask_need_exam_center
* deny
* change_exam_type {"exam_type":"BITSHD"}
    - utter_sure
    - action_get_info_about_exam
* thankyou
    - utter_noworries


<!-- *******************STORY FOR EXAM CENTERS******************** -->
## story1: get exam center + addr happy path
* greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Naveen"}
    - utter_how_can_i_help
* find_an_exam_center
    - utter_help_find_centers
* find_an_exam_center{"exam_type" : "BITSHD", "location_state" : "Delhi"}
    - bits_enterance_examcenter_search_in_state
    - form{"name": "bits_enterance_examcenter_search_in_state"}
    - form{"name": null}
    - utter_slots_values
    - action_search_exam_centers
    - utter_can_help_you_find_examcenter_in_city
* affirm
    - utter_get_city
* get_location_city{"location_city" : "Mumbai"}
    - action_get_addr_exam_center
* thankyou
    - utter_noworries


## story2: get exam center  + no addr happy path
* greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Naveen"}
    - utter_how_can_i_help
* find_an_exam_center
    - utter_help_find_centers
* find_an_exam_center{"exam_type" : "BITSHD", "location_state" : "Delhi"}
    - bits_enterance_examcenter_search_in_state
    - form{"name": "bits_enterance_examcenter_search_in_state"}
    - form{"name": null}
    - utter_slots_values
    - action_search_exam_centers
    - utter_can_help_you_find_examcenter_in_city
* deny
    - utter_noworries


## story3: get exam center + addr 
* greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Naveen"}
    - utter_how_can_i_help
* find_an_exam_center{"exam_type" : "BITSHD", "location_state" : "Delhi"}
    - bits_enterance_examcenter_search_in_state
    - form{"name": "bits_enterance_examcenter_search_in_state"}
    - form{"name": null}
    - utter_slots_values
    - action_search_exam_centers
    - utter_can_help_you_find_examcenter_in_city
* get_location_city{"location_city" : "Mumbai"}
    - action_get_addr_exam_center
* thankyou
    - utter_noworries


## story4: get exam center
* greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Naveen"}
    - utter_how_can_i_help
* find_an_exam_center{"exam_type" : "BITSHD"}
    - bits_enterance_examcenter_search_in_state
    - form{"name": "bits_enterance_examcenter_search_in_state"}
    - form{"name": null}
    - utter_slots_values
    - action_search_exam_centers
    - utter_can_help_you_find_examcenter_in_city
* deny
    - utter_noworries
* thankyou
    - utter_noworries

## story5: get exam center
* greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Naveen"}
    - utter_how_can_i_help
* find_an_exam_center{"exam_type" : "BITSHD", "location_state" : "Delhi"}
    - bits_enterance_examcenter_search_in_state
    - form{"name": "bits_enterance_examcenter_search_in_state"}
    - form{"name": null}
    - utter_slots_values
    - action_search_exam_centers
    - utter_can_help_you_find_examcenter_in_city
* deny
    - utter_noworries
* thankyou
    - utter_noworries

## story5: find exam center + change exam type
* greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Naveen"}
    - utter_how_can_i_help
* find_an_exam_center{"exam_type":"BITSHD"}
    - utter_help_find_centers
* get_location_state{"location_state" : "Maharashra"}
    - bits_enterance_examcenter_search_in_state
    - form{"name": "bits_enterance_examcenter_search_in_state"}
    - form{"name": null}
    - utter_slots_values
    - action_search_exam_centers
* change_exam_type
    - slot{"exam_type" : null}
    - utter_sure
    - bits_enterance_examcenter_search_in_state
    - form{"name": "bits_enterance_examcenter_search_in_state"}
    - form{"name": null}
    - utter_slots_values
    - action_search_exam_centers
    - utter_can_help_you_find_examcenter_in_city
* deny
    - utter_noworries
* thankyou
    - utter_noworries

## story6: find exam center + change exam type
* greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Naveen"}
    - utter_how_can_i_help
* find_an_exam_center{"exam_type":"BITSHD"}
    - utter_help_find_centers
* get_location_state{"location_state" : "Maharashra"}
    - bits_enterance_examcenter_search_in_state
    - form{"name": "bits_enterance_examcenter_search_in_state"}
    - form{"name": null}
    - utter_slots_values
    - action_search_exam_centers
* change_exam_type
    - utter_sure
    - bits_enterance_examcenter_search_in_state
    - form{"name": "bits_enterance_examcenter_search_in_state"}
    - form{"name": null}
    - utter_slots_values
    - action_search_exam_centers
    - utter_can_help_you_find_examcenter_in_city
* affirm
    - utter_get_city
* get_location_city{"location_city" : "Mumbai"}
    - action_get_addr_exam_center
* thankyou
    - utter_noworries


## story7: get exam center
* greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Naveen"}
    - utter_how_can_i_help
* find_an_exam_center
    - utter_ask_exam_type
* get_exam_type{"exam_type":"BITSHD"}
    - bits_enterance_examcenter_search_in_state
    - form{"name": "bits_enterance_examcenter_search_in_state"}
    - form{"name": null}
    - utter_slots_values
    - action_search_exam_centers
    - utter_can_help_you_find_examcenter_in_city
* deny
    - utter_noworries
* thankyou
    - utter_noworries

## story8: get exam center
* greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Naveen"}
    - utter_how_can_i_help
* find_an_exam_center
    - utter_ask_exam_type
* get_exam_type{"exam_type":"BITSHD", "location_state":"Maharashtra"}
    - bits_enterance_examcenter_search_in_state
    - form{"name": "bits_enterance_examcenter_search_in_state"}
    - form{"name": null}
    - utter_slots_values
    - action_search_exam_centers
    - utter_can_help_you_find_examcenter_in_city
* deny
    - utter_noworries
* thankyou
    - utter_noworries


<!-- Course Info -->
## story1: get_course_info
 * greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Naveen"}
    - utter_how_can_i_help
* get_course_info{"course":"BE"}
    - action_fetch_course_info
* thankyou
    - utter_noworries

## story2: get_course_info + ask_degree
 * greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Naveen"}
    - utter_how_can_i_help
* get_course_info
    - utter_ask_degree
* get_degree{"course":"BE"}
    - action_fetch_course_info
* thankyou
    - utter_noworries

## story3: get_course_info + nogreet
* get_course_info
    - utter_ask_degree
* get_degree{"course":"BE"}
    - action_fetch_course_info
* thankyou
    - utter_noworries

<!-- Ask fee for course -->
## story1: ask_fee_for_course
 * greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Naveen"}
    - utter_how_can_i_help
* ask_fee_for_course{"course":"BE"}
    - action_fetch_fee_for_course
* thankyou
    - utter_noworries

## story2: ask_fee_for_course + ask_degree
 * greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Naveen"}
    - utter_how_can_i_help
* ask_fee_for_course
    - utter_ask_degree
* get_degree{"course":"BE"}
    - action_fetch_fee_for_course
* thankyou
    - utter_noworries

## story3: ask_fee_for_course + nogreet
* ask_fee_for_course
    - utter_ask_degree
* get_degree{"course":"BE"}
    - action_fetch_fee_for_course
* thankyou
    - utter_noworries


<!-- Fee for exam -->
## story1: ask_fee_for_exam
 * greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Naveen"}
    - utter_how_can_i_help
* ask_fee_for_exam{"exam_type":"BITSAT"}
    - action_fetch_fee_for_exam
* thankyou
    - utter_noworries

## story2: ask_fee_for_exam + ask_exam_type
 * greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Naveen"}
    - utter_how_can_i_help
* ask_fee_for_exam
    - utter_ask_exam_type
* get_exam_type{"exam_type":"BITSAT"}
    - action_fetch_fee_for_exam
* thankyou
    - utter_noworries

## story3: ask_fee_for_exam + nogreet
* ask_fee_for_exam
    - utter_ask_exam_type
* get_exam_type{"exam_type":"BITSAT"}
    - action_fetch_fee_for_exam
* thankyou
    - utter_noworries

<!-- syallabus for exam -->
## story1: ask_syllabus_of_exam BITSAT
 * greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Naveen"}
    - utter_how_can_i_help
* ask_syllabus_of_exam{"exam_type":"BITSAT"}
    - action_fetch_syllabus_for_exam
* thankyou
    - utter_noworries

## story2: ask_syllabus_of_exam BITSAT
 * greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Naveen"}
    - utter_how_can_i_help
* ask_syllabus_of_exam
    - utter_ask_exam_type
* get_exam_type{"exam_type":"BITSAT"}
    - action_fetch_syllabus_for_exam
* thankyou
    - utter_noworries

## story3: ask_syllabus_of_exam BITSAT
 * greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Naveen"}
    - utter_how_can_i_help
* ask_syllabus_of_exam
    - utter_ask_exam_type
* get_branch{"exam_type":"BITSHD", "branch":"Computer Engineering"}
    - action_fetch_syllabus_for_exam
* thankyou
    - utter_noworries

## story4: ask_syllabus_of_exam BITSAT
 * greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Naveen"}
    - utter_how_can_i_help
* ask_syllabus_of_exam
    - utter_ask_exam_type
* get_exam_type{"exam_type":"BITSAT"}
    - action_fetch_syllabus_for_exam
* get_branch{"branch":"Computer Engineering"}
    - action_fetch_syllabus_for_exam
* thankyou
    - utter_noworries


<!-- get bracnes in campuses -->
## story1: get_streams
* greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Naveen"}
    - utter_how_can_i_help
* get_branches_in_a_campus{"course" : "BE", "campus" : "Pilani"}
    - action_fetch_branches_in_campus
* thankyou
    - utter_noworries

## story2: get_streams + get_branch
* greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Naveen"}
    - utter_how_can_i_help
* get_branches_in_a_campus{"campus" : "Pilani"}
    - utter_ask_degree
* get_degree{"course" : "BE"}
    - action_fetch_branches_in_campus
* thankyou
    - utter_noworries

## story3: get_streams + get_campus
* greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Naveen"}
    - utter_how_can_i_help
* get_branches_in_a_campus{"course" : "BE"}
    - utter_ask_campus
* get_campus{"campus" : "Pilani"}
    - action_fetch_branches_in_campus
* thankyou
    - utter_noworries


<!-- get campus from branch -->
## story1: which_campus_has_branch + get_degree
* greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Naveen"}
    - utter_how_can_i_help
* ask_which_campus_has_branch{"branch":"Computer Engineering"}
    - utter_ask_degree
* get_degree{"course" : "BE"}
    - action_fetch_campus_from_branch
* thankyou
    - utter_noworries

## story1: which_campus_has_branch
* greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Naveen"}
    - utter_how_can_i_help
* ask_which_campus_has_branch{"branch":"Computer Engineering", "course": "BE"}
    - action_fetch_campus_from_branch
* thankyou
    - utter_noworries

<!-- *******************MISC******************** -->
## story1: chitchat
* chitchat
    - utter_chitchat


## story2: bot challenge
* bot_challenge
  - utter_iamabot


## story3: restart the bot1
* stop
    - utter_restart
    - action_chat_restart

## story4: restart the bot2
* restart
    - utter_restart
    - action_chat_restart