# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

# from typing import Any, Text, Dict, List

import urllib.request, json
import operator
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class ActionGetSideEffects(Action):
     def name(self):
         return "action_get_side_effects"

     def run(self, dispatcher, tracker, domain):
         
         side_effects = {}

         medicine = tracker.get_slot('medicine')
         url = "https://api.fda.gov/drug/event.json?search=patient.drug.medicinalproduct:\"" + medicine.upper() + "\"&limit=10"
         print(url)
         with urllib.request.urlopen(url) as record:
             values = json.load(record)
             record.close()
         for each_res in values['results']:
             for reaction in each_res['patient']['reaction']:
                 se = reaction['reactionmeddrapt']
                 if se in side_effects:
                     side_effects[se] += 1
                 else:
                     side_effects[se] = 1
         
         
         sorted_effects = sorted(side_effects.items(), key = operator.itemgetter(1), reverse = True)
         say_effects = ""
         count = len(sorted_effects)
         if count > 7:
             i = 1
             for eff in sorted_effects:
                 say_effects += (eff[0] + ", ")
                 if i == 7:
                     break
                 i += 1
             say_effects += ("are the side effects caused due to " + medicine[0].upper() + medicine[1:].lower())
         else:
             if count == 0:
                 say_effects += "No side effects found. Please check if you gave the right spelling of the medicine."
             else:
                 for eff in sorted_effects:
                    say_effects += (eff[0] + ", ")
                 if count == 1:
                     say_effects += ("is the side effect caused due to" + medicine[0].upper() + medicine[1:].lower())
                 else:
                     say_effects += ("are the side effects caused due to " + medicine[0].upper() + medicine[1:].lower())

         dispatcher.utter_message(text=say_effects)

         return []


class ActionGetDiagnosisAndSpecializations(Action):
     def name(self):
         return "action_get_diagnosis_and_specializations"

     def run(self, dispatcher, tracker, domain):
         auth_token = "your_api_key"

         with open('Symptoms_Sandbox.json') as f:
             data = json.load(f)
             f.close()
         symptoms_id_map = {}
         for each in data:
             symptoms_id_map[each['Name'].lower()] = each['ID']
         url = "https://sandbox-healthservice.priaid.ch/diagnosis?symptoms=["
         symptoms = tracker.get_slot('symptoms')
         gender = tracker.get_slot('gender')
         yob = tracker.get_slot('year_of_birth')

         symptoms_ids = []
         check= set([])
         for each in symptoms:
             each = each.lower()
             if each in symptoms_id_map:
                 if symptoms_id_map[each] not in check:
                    symptoms_ids.append(symptoms_id_map[each])
                    check.add(symptoms_id_map[each])
         print(symptoms_ids, gender, yob)
         for idx, sid in enumerate(symptoms_ids):
             url += str(sid)
             if idx != len(symptoms_ids)-1:
                 url += ","
         url += "]&gender="
         if type(gender) == list:
            url += gender[0]
         else:
             url += gender
         url += "&year_of_birth="
         url += yob[0]
         url += "&token="
         url += auth_token
         url += "&format=json&language=en-gb"

         print(url)
         with urllib.request.urlopen(url) as record:
             results = json.load(record)
             record.close()

         say_diseases = ""
         for each in results:
             say_diseases += "You may have " + each['Issue']['Name'] + " with a predicted accuracy of " + str(each['Issue']['Accuracy']) + ". "
             if len(each['Specialisation']) != 0:
                 say_diseases += "Please visit "
                 for idx, specialist in enumerate(each['Specialisation']):
                     say_diseases += specialist['Name']
                     if idx != len(each['Specialisation']) - 1:
                         say_diseases += ", "
                 
                 if len(each['Specialisation']) == 1:
                     say_diseases += " department. "
                 else:
                     say_diseases += " departments. "

         if say_diseases == "":
             say_diseases += "No possible diseases found!"

         dispatcher.utter_message(text=say_diseases)

         return []


class SymptomsForm(FormAction):

    def name(self):
        return "symptoms_analysis_form"

    @staticmethod
    def required_slots(tracker):
        return ["symptoms", "gender", "year_of_birth"]

    def submit(self, dispatcher, tracker, domain):
        dispatcher.utter_message(template="utter_submit")
        return []
