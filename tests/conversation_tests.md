#### This file contains tests to evaluate that your bot behaves as expected.
#### If you want to learn more, please see the docs: https://rasa.com/docs/rasa/user-guide/testing-your-assistant/

## hospital question 1
* greet: hello there!
  - utter_greet
* hospitalSearchQuery: list of health care centers located around Hyderabad
  - utter_forwardToHospitalSearch
  - action_get_hospital_search
* thanks: thank you
  - utter_welcome
* goodbye: see you later!
  - utter_goodbye
  
## hospital question 2
* greet: hii!
  - utter_greet
* hospitalSearchQuery: can you name the health care centers in Bangalore
  - utter_forwardToHospitalSearch
  - action_get_hospital_search
* thanks: thanks
  - utter_welcome
* goodbye: bye!
  - utter_goodbye  
  
## hospital question 3
* greet: hello!
  - utter_greet
* hospitalSearchQuery: give the names of hospitals near Chennai
  - utter_forwardToHospitalSearch
  - action_get_hospital_search
* thanks: thank you so much
  - utter_welcome
* goodbye: ok then i will take a leave!
  - utter_goodbye    
  


## happy path 1
* greet: hello there!
  - utter_greet
* mood_great: amazing
  - utter_happy

## happy path 2
* greet: hello there!
  - utter_greet
* mood_great: amazing
  - utter_happy
* goodbye: bye-bye!
  - utter_goodbye

## sad path 1
* greet: hello
  - utter_greet
* mood_unhappy: not good
  - utter_cheer_up
  - utter_did_that_help
* affirm: yes
  - utter_happy

## sad path 2
* greet: hello
  - utter_greet
* mood_unhappy: not good
  - utter_cheer_up
  - utter_did_that_help
* deny: not really
  - utter_goodbye

## sad path 3
* greet: hi
  - utter_greet
* mood_unhappy: very terrible
  - utter_cheer_up
  - utter_did_that_help
* deny: no
  - utter_goodbye

## say goodbye
* goodbye: bye-bye!
  - utter_goodbye

## bot challenge
* bot_challenge: are you a bot?
  - utter_iamabot
