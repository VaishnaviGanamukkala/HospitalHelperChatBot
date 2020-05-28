## sideEffects query1
* greet
  - utter_greet
* options
  - utter_options
* sideEffectsQuery{"medicine": "humira"}
  - slot{"medicine": "humira"}
  - utter_forwardToSideEffects
  - action_get_side_effects
* thanks
  - utter_welcome
* goodbye
  - utter_goodbye

## sideEffects query2
* greet
  - utter_greet
* options
  - utter_options
* sideEffectsQuery{"medicine": "prednisone"}
  - slot{"medicine": "prednisone"}
  - utter_forwardToSideEffects
  - action_get_side_effects
* goodbye
  - utter_goodbye

## sideEffects query3
* greet
  - utter_greet
* sideEffectsQuery{"medicine": "amlodipine"}
  - slot{"medicine": "amlodipine"}
  - utter_forwardToSideEffects
  - action_get_side_effects
* thanks
  - utter_welcome
* goodbye
  - utter_goodbye

## sideEffects query4
* greet
  - utter_greet
* sideEffectsQuery{"medicine": "fentanyl"}
  - slot{"medicine": "fentanyl"}
  - utter_forwardToSideEffects
  - action_get_side_effects
* goodbye
  - utter_goodbye

## sideEffects query5
* greet
  - utter_greet
* sideEffectsQuery{"medicine": "asprin"}
  - slot{"medicine": "asprin"}
  - utter_forwardToSideEffects
  - action_get_side_effects
  
## hospitalSearch query1
* greet
  - utter_greet
* options
  - utter_options
* hospitalSearchQuery{"location": "hyderabad"}
  - slot{"location": "hyderabad"}
  - utter_forwardToHospitalSearch
  - action_get_hospital_search
* thanks
  - utter_welcome
* goodbye
  - utter_goodbye
  
## hospitalSearch query2
* greet
  - utter_greet
* options
  - utter_options
* hospitalSearchQuery{"location": "bangalore"}
  - slot{"location": "bangalore"}
  - utter_forwardToHospitalSearch
  - action_get_hospital_search
* goodbye
  - utter_goodbye
  
## hospitalSearch query3
* greet
  - utter_greet
* hospitalSearchQuery{"location": "chennai"}
  - slot{"location": "chennai"}
  - utter_forwardToHospitalSearch
  - action_get_hospital_search
* thanks
  - utter_welcome
* goodbye
  - utter_goodbye
  
## hospitalSearch query4
* greet
  - utter_greet
* hospitalSearchQuery{"location": "pune"}
  - slot{"location": "pune"}
  - utter_forwardToHospitaSearch
  - action_get_hospital_search
* goodbye
  - utter_goodbye
  
## hospitalSearch query5
* greet
  - utter_greet
* hospitalSearchQuery{"location": "delhi"}
  - slot{"location": "delhi"}
  - utter_forwardToHospitalSearch
  - action_get_hospital_search

## query path1
* greet
  - utter_greet
* options
  - utter_options
* thanks
  - utter_welcome
* goodbye
  - utter_goodbye

## query path2
* options
  - utter_options
* thanks
  - utter_welcome
* goodbye
  - utter_goodbye

## query path3
* options
  - utter_options
* goodbye
  - utter_goodbye

## casual path
* greet
  - utter_greet
* goodbye
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## fallback
- utter_unclear
