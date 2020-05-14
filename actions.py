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
