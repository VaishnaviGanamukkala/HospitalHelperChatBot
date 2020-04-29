## sideEffects query1
* greet
  - utter_greet
* options
  - utter_options
* sideEffectsQuery{"medicine": "humira"}
  - slot{"medicine": "humira"}
  - utter_forwardToSideEffects
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
* goodbye
  - utter_goodbye

## sideEffects query3
* greet
  - utter_greet
* sideEffectsQuery{"medicine": "amlodipine"}
  - slot{"medicine": "amlodipine"}
  - utter_forwardToSideEffects
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
* goodbye
  - utter_goodbye

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
