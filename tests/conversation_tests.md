#### This file contains tests to evaluate that your bot behaves as expected.
#### If you want to learn more, please see the docs: https://rasa.com/docs/rasa/user-guide/testing-your-assistant/

## hospital question 1
* greet: hi hello
  - utter_greet
* hospitalSearchQuery: list of health care centers located around Hyderabad
  - utter_forwardToHospitalSearch
  - action_get_hospital_search
* thanks: that's cool. much obliged
  - utter_welcome
* goodbye: see you later!
  - utter_goodbye

## say goodbye
* goodbye: bye-bye!
  - utter_goodbye
