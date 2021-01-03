
from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction, Restarted
from rasa_sdk.forms import FormAction
import requests
from langdetect import detect
# from rasa_core.interpreter import RasaNLUInterpreter

baseurl = "http://127.0.0.1:8000/bitsbot/"

class BitsEnternaceExamCenterSearchInStateForm(FormAction):
    def name(self) -> Text:
        return "bits_enterance_examcenter_search_in_state"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""
        return ["location_state", "exam_type"]
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "exam_type": self.from_entity(entity="exam_type", not_intent="chitchat"),
            "location_state": [
                self.from_entity(
                    entity="location_state", intent=["find_an_exam_center", "need_more_info", "get_location_state"]
                )
            ]
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="utter_submit")
        return []

    @staticmethod
    def getAllStates() -> List[Text]:
        """Database of supported cuisines"""

        return ["Andra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Orissa","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telagana","Tripura","Uttaranchal","Uttar Pradesh","West Bengal"]

    def validate_location_state(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        # print("Inside value "+ value)
        if value.lower() in [x.lower() for x in self.getAllStates()] or detect(value) != 'en':
            
            return {"location_state": value}
        else:
            dispatcher.utter_message(template="utter_wrong_location_state")
            
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"location_state": None}

class ActionSearchExamCenter(Action):

    def name(self) -> Text:
        return "action_search_exam_centers"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        exam_type = tracker.get_slot("exam_type")
        # centres = ['Mumbai', 'Vashi']
        location_state = tracker.get_slot("location_state")
        
        url = baseurl + "find_centers/"
        request_body = {
            'exam_type': exam_type,
            'location_state' : location_state
        }
        response = (requests.post(url, data = request_body)).json()
        # print(response)
        if(response['success'] and len(response['centers']) > 0):
            dispatcher.utter_message(template="utter_found_exam_center" , centers = response['centers'])
            return[SlotSet("list_of_cities", response['centers'])]
        else:
            dispatcher.utter_message(template="utter_could_not_find_exam_center")
            return[SlotSet("list_of_cities", [])]
            # clear location_state slot
        return

class ActionGetInfoAboutExam(Action):

    def name(self) -> Text:
        return "action_get_info_about_exam"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        exam_type = tracker.get_slot("exam_type")
        
        url = baseurl + "get_info_about_exam/"
        request_body = {
            'exam_type': exam_type
        }
        response = (requests.post(url, data = request_body)).json()
        # print(response)
        try:
            if(response['success']):
                dispatcher.utter_message(response['information'])
            else:
                dispatcher.utter_message(template="utter_could_not_find_exam_center")
        except Exception as e:
            print(e)
            dispatcher.utter_message(template="utter_error_occurred")

class ActionGetAddressofExamCenters(Action):

    def name(self) -> Text:
        return "action_get_addr_exam_center"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        exam_type = tracker.get_slot("exam_type")
        location_state = tracker.get_slot("location_state")
        location_city = tracker.get_slot("location_city")
        if location_city.lower() not in [x.lower() for x in tracker.get_slot("list_of_cities")]:
            dispatcher.utter_message(template="utter_wrong_location_city")
            return
        url = baseurl + "fetch_address_of_exam_center/"
        request_body = {
            'exam_type': exam_type,
            'location_state' : location_state,
            'location_city' : location_city
        }
        response = (requests.post(url, data = request_body)).json()
        # print(response)
        try:
            if(response['success']):
                dispatcher.utter_message(template="utter_found_exam_center", centers=location_city)
                i = 1
                for addr in response['addr']:
                    dispatcher.utter_message(str(i) + ". " + addr)
                    i += 1
            else:
                dispatcher.utter_message(template="utter_could_not_find_exam_center")
        except Exception as e:
            print(e)
            dispatcher.utter_message(template="utter_error_occurred")

class ActionFetchCourseInfo(Action):

    def name(self) -> Text:
        return "action_fetch_course_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        course = tracker.get_slot("course")
        
        url = baseurl + "fetch_course_info/"
        request_body = {
            'course': course
        }
        response = (requests.post(url, data = request_body)).json()
        print(response)
        try:
            if(response['success']):
                dispatcher.utter_message(response['information'])
            else:
                dispatcher.utter_message(template="utter_error_occurred")
        except Exception as e:
            print(e)
            dispatcher.utter_message(template="utter_error_occurred")

class ActionFetchSyllabusForExam(Action):

    def name(self) -> Text:
        return "action_fetch_syllabus_for_exam"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        exam_type = tracker.get_slot("exam_type")
        branch = tracker.get_slot("branch")
        if exam_type == 'BITSHD' and branch is None:
            # branch = tracker.get_slot("branch")
            dispatcher.utter_message(template="utter_ask_branch")
            # interpreter = RasaNLUInterpreter('../en/model/current/nlu')
            # out = (interpreter.parse(input))
            # action_listen()
            # text = (tracker.latest_message)['text']
            # print("Text= " + text)
            return

        # print(out)
        url = baseurl + "fetch_syllabus_for_exam/"
        request_body = {
            'exam_type': exam_type,
            'branch':  branch
        }
        response = (requests.post(url, data = request_body)).json()
        print(response)
        try:
            if(response['success']):
                dispatcher.utter_message(template="utter_syllabus" , Syllabus = response['syllabus'])
            else:
                dispatcher.utter_message(template="utter_error_occurred")
        except Exception as e:
            print(e)
            dispatcher.utter_message(template="utter_error_occurred")
class ActionFetchFeeForExam(Action):

    def name(self) -> Text:
        return "action_fetch_fee_for_exam"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        exam_type = tracker.get_slot("exam_type")
        url = baseurl + "fetch_fee_for_exam/"
        request_body = {
            'exam_type': exam_type
        }
        response = (requests.post(url, data = request_body)).json()
        print(response)
        try:
            if(response['success']):
                dispatcher.utter_message(template="utter_fee_for_exam", feeInRupee= response['fee'])
            else:
                dispatcher.utter_message(template="utter_error_occurred")
        except Exception as e:
            print(e)
            dispatcher.utter_message(template="utter_error_occurred")
class ActionFetchFeeForCourse(Action):

    def name(self) -> Text:
        return "action_fetch_fee_for_course"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        course = tracker.get_slot("course")
        url = baseurl + "fetch_fee_for_course/"
        request_body = {
            'course': course
        }
        response = (requests.post(url, data = request_body)).json()
        print(response)
        try:
            if(response['success']):
                dispatcher.utter_message(template="utter_fee_for_program", feeInRupee= response['fee'])
            else:
                dispatcher.utter_message(template="utter_error_occurred")
        except Exception as e:
            print(e)
            dispatcher.utter_message(template="utter_error_occurred")

class ActionFetchBranchesForACampus(Action):

    def name(self) -> Text:
        return "action_fetch_branches_in_campus"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        course = tracker.get_slot("course")
        campus = tracker.get_slot("campus")
        url = baseurl + "fetch_branches_in_campus/"
        request_body = {
            'course': course,
            'campus' : campus
        }
        response = (requests.post(url, data = request_body)).json()
        print(response)
        try:
            if(response['success']):
                index = 1
                separator = ', '
                campus_branch_mapping = "\nThe courses are as follows \n"
                # response['campus_branch_mapping']
                for campuses, branches in response['campus_branch_mapping'].items():
                    campus_branch_mapping += str(index) + ". " + campuses + " - " + separator.join(branches) + "\n"
                    index += 1

                dispatcher.utter_message(template="utter_branches_available_in_campus", branches= campus_branch_mapping)
            else:
                dispatcher.utter_message(template="utter_error_occurred")
        except Exception as e:
            print(e)
            dispatcher.utter_message(template="utter_error_occurred")

class ActionFetchCampusFromBranch(Action):

    def name(self) -> Text:
        return "action_fetch_campus_from_branch"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        course = tracker.get_slot("course")
        branch = tracker.get_slot("branch")
        url = baseurl + "fetch_campus_from_branch/"
        request_body = {
            'course': course,
            'branch' : branch
        }
        response = (requests.post(url, data = request_body)).json()
        print(response)
        try:
            if(response['success']):
                dispatcher.utter_message(template="utter_specific_branch_available_in_campus", campus= response['campus'])
            else:
                dispatcher.utter_message(template="utter_error_occurred")
        except Exception as e:
            print(e)
            dispatcher.utter_message(template="utter_error_occurred")

class ActionRestarted(Action):

    def name(self):
        return "action_chat_restart"

    def run(self, dispatcher, tracker, domain):
        return [Restarted()]