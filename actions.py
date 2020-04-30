# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

# from typing import Any, Text, Dict, List

import urllib.request, json
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionGetSideEffects(Action):
     def name(self):
         return "action_get_side_effects"

     def run(self, dispatcher, tracker, domain):
         
         side_effects = []

         medicine = tracker.get_slot('medicine')
         url = "https://api.fda.gov/drug/event.json?search=patient.drug.medicinalproduct:\"" + medicine.upper() + "\"&limit=10"
         print(url)
         with urllib.request.urlopen(url) as record:
             values = json.load(record)
             record.close()
         for each_res in values['results']:
             for reaction in each_res['patient']['reaction']:
                 side_effects.append(reaction['reactionmeddrapt'])
         
         say_effects = ""
         for eff in side_effects:
             say_effects += (eff + " ")
         if len(side_effects) == 0:
             say_effects += "No side effects found"
         elif len(side_effects) == 1:
             say_effects += ("is the side effect caused due to" + medicine[0].upper() + medicine[1:].lower())
         else:
             say_effects += ("are the side effects caused due to " + medicine[0].upper() + medicine[1:].lower())
         dispatcher.utter_message(text=say_effects)

         return []
