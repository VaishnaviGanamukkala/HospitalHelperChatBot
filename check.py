import urllib.request, json
import operator
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionHospitalSearch(Action):
     def name(self):
         return "action_hospital_search"

     def run(self, dispatcher, tracker, domain):
         
         hospital_search = []
         
         
        
        lat_long = {"hyderabad" : ("17.3850", "78.4867"), "bangalore" : ("12.9716", "77.5946"), "chennai" : ("13.0827", "80.2707"), "pune" : ("18.5204", "73.8567"), "delhi" : ("28.7041", "77.1025"), "kolkata" : ("22.5726", "88.3639"), "mumbai" : ("19.0760", "72.8777"), "jaipur" : ("26.9124", "75.7873"), "mysore" : ("12.2958", "76.6394"), "agra" : ("27.1767", "78.0081"), "vizag" : ("17.6868", "83.2185"), "goa" : ("15.2993", "74.1240"), "amritsar" : ("31.6340", "74.8723"), "kochi" : ("9.9312", "76.2673"), "ahmedabad" : ("23.0225", "72.5714"), "thiruvananthapuram" : ("8.5241", "76.9366"), "kolhapur" : ("16.7050", "74.2433"), "solapur" : ("17.6599", "75.9064"), "madurai" : ("9.9252", "78.1198"), "kanchipuram" : ("12.8185", "79.6947"), "lucknow" : ("26.8467", "80.9462")}

         location = tracker.get_slot('location')
         url = "https://api.tomtom.com/search/2/categorySearch/hospital.json?limit=10&lat=" + lat_long[location][0] + "&lon=" + lat_long[location][1] + "&radius=10000&key="your_api_key""
         print(url)
         with urllib.request.urlopen(url) as record:
             res = json.load(record)
             record.close()
         
         say_hospitals = ""

         for idx, each in enumerate(res['results']):
             say_hospitals += str(idx+1) + ". "+ each['poi']['name'] + " - "
             say_hospitals += each['address']['freeformAddress'] + "\n"

         dispatcher.utter_message(text=say_hospitals)

         return []
