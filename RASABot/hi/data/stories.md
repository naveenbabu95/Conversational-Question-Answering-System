
<!-- *******************STORY FOR EXAM INFO******************** -->
## story1: get inforamtion about exam + exam center
* greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Adam"}
    - utter_how_can_i_help
* input_choice{"choice":"info"}
    - slot{"choice" : "info"}
    - utter_get_exam_type
    - utter_ask_exam_type
* enquire{"exam_type":"BITSHD"}
    - action_get_info_about_exam
    - utter_ask_need_exam_center
* affirm
    - slot{"choice" : "center"}
    - utter_ask_location_state
* enquire{"exam_type":"BITSHD", "location_state" : "Maharashtra"}
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
* input_choice{"choice":"info"}
    - slot{"choice" : "info"}
    - utter_get_exam_type
    - utter_ask_exam_type
* enquire{"exam_type":"BITSHD"}
    - action_get_info_about_exam
    - utter_ask_need_exam_center
* deny
    - utter_noworries


## story3: get inforamtion about exam directly + affirm for exam center
* greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Eve"}
    - utter_how_can_i_help
* input_choice{"choice":"info", "exam_type":"BITSHD"}
    - slot{"choice" : "info"}
    - action_get_info_about_exam
    - utter_ask_need_exam_center
* affirm
    - slot{"choice" : "center"}
    - utter_ask_location_state
* enquire{"exam_type":"BITSHD", "location_state" : "Rajasthan"}
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
* input_choice{"choice":"info", "exam_type":"BITSHD"}
    - slot{"choice" : "info"}
    - action_get_info_about_exam
    - utter_ask_need_exam_center
* deny
    - utter_noworries

## story4: get inforamtion about exam + change exam type
* greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Eve"}
    - utter_how_can_i_help
* input_choice{"choice":"info", "exam_type":"BITSHD"}
    - slot{"choice" : "info"}
    - action_get_info_about_exam
* change_exam_type{"exam_type":"BITSHD"}
    - action_get_info_about_exam
    - utter_ask_need_exam_center
* deny
    - utter_noworries

## story5: get info without greeting
* input_choice{"choice":"info", "exam_type":"BITSHD"}
    - slot{"choice" : "info"}
    - action_get_info_about_exam
    - utter_ask_need_exam_center
* deny
    - utter_noworries

## story6: get info without greeting
* input_choice{"choice":"info"}
    - slot{"choice" : "info"}
    - utter_get_exam_type
    - utter_ask_exam_type
* enquire{"exam_type":"BITSHD"}
    - action_get_info_about_exam
    - utter_ask_need_exam_center
* deny
    - utter_noworries

## story7: get inforamtion about exam + change exam type
* greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Eve"}
    - utter_how_can_i_help
* input_choice{"choice":"info", "exam_type":"BITSHD"}
    - slot{"choice" : "info"}
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
* input_choice{"choice":"center"}
    - slot{"choice" : "center"}
    - utter_help_find_centers
* enquire{"exam_type" : "BITSHD", "location_state" : "Delhi"}
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
* input_choice{"choice":"center"}
    - slot{"choice" : "center"}
    - utter_help_find_centers
* enquire{"exam_type" : "BITSHD", "location_state" : "Delhi"}
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
* input_choice{"choice":"center"}
    - slot{"choice" : "center"}
    - utter_help_find_centers
* enquire{"exam_type" : "BITSHD", "location_state" : "Delhi"}
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
* input_choice{"choice":"center", "exam_type":"BITSHD"}
    - slot{"choice" : "center"}
    - utter_help_find_centers
* enquire{"exam_type" : "BITSHD"}
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
* input_choice{"choice":"center", "exam_type":"BITSHD"}
    - slot{"choice" : "center"}
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
* deny
    - utter_noworries
* thankyou
    - utter_noworries

## story6: find exam center + change exam type
* greet
    - utter_greet_ask_name
* inputting_name{"name_of_user":"Naveen"}
    - utter_how_can_i_help
* input_choice{"choice":"center", "exam_type":"BITSHD"}
    - slot{"choice" : "center"}
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