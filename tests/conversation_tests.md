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
  
## hospital question 4
* greet: hey!
  - utter_greet
* hospitalSearchQuery: tell the names of hospitals in Delhi
  - utter_forwardToHospitalSearch
  - action_get_hospital_search
* thanks: great thank you
  - utter_welcome
* goodbye: see you again
  - utter_goodbye      
  
## sideEffects question 1
* greet: hey!
  - utter_greet
* sideEffectsQuery: can you mention the side effects of paracetamol
  - utter_forwardToSideEffects
  - action_get_side_effects
* thanks: great thank you
  - utter_welcome
* goodbye: see you again
  - utter_goodbye      
  
## sideEffects question 2
* greet: hey there!
  - utter_greet
* sideEffectsQuery: may i know the health consequences of insulin
  - utter_forwardToSideEffects
  - action_get_side_effects
* thanks: thank you
  - utter_welcome
* goodbye: bye-bye
  - utter_goodbye     
  
## sideEffects question 3
* greet: hii!
  - utter_greet
* sideEffectsQuery: does nexium has any side effects
  - utter_forwardToSideEffects
  - action_get_side_effects
* thanks: i am soo thankful
  - utter_welcome
* goodbye: bye for now
  - utter_goodbye      
  
## sideEffects question 4
* greet: hi there!
  - utter_greet
* sideEffectsQuery: will there be any effects on using omeprazole
  - utter_forwardToSideEffects
  - action_get_side_effects
* thanks: thanks a lot
  - utter_welcome
* goodbye: see you soon
  - utter_goodbye        
  
## symptomsAnalysis question 1
* greet: hello!
  - utter_greet
* symptomsAnalysisQuery: can you suggest me the doctor that i have to visit
  - utter_forwardToSymptomsAnalysis
  - action_get_symptoms_analysis
* thanks: thanks
  - utter_welcome
* goodbye: bye for now
  - utter_goodbye      
  
## symptomsAnalysis question 2
* greet: hello there!
  - utter_greet
* symptomsAnalysisQuery: which doctor should i meet
  - utter_forwardToSymptomsAnalysis
  - action_get_symptoms_analysis
* thanks: great thank you
  - utter_welcome
* goodbye: bye-bye
  - utter_goodbye      
  
## symptomsAnalysis question 3
* greet: good day!
  - utter_greet
* symptomsAnalysisQuery: is there a need for me to meet a doctor
  - utter_forwardToSymptomsAnalysis
  - action_get_symptoms_analysis
* thanks: wow that's great
  - utter_welcome
* goodbye: all right then
  - utter_goodbye     
  
## symptomsAnalysis question 4
* greet: hii!
  - utter_greet
* symptomsAnalysisQuery: do i have any health issues
  - utter_forwardToSymptomsAnalysis
  - action_get_symptoms_analysis
* thanks: thanks
  - utter_welcome
* goodbye: see you soon
  - utter_goodbye     
  


## happy path 1
* greet: hello there!
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


## error question 2
* greet: hello there!
  - utter_greet
* symptomsAnalysisQuery: which doctor should i meet
  - utter_welcome
* thanks: great thank you
  - utter_forwardToSymptomsAnalysis
  - action_get_symptoms_analysis
* goodbye: bye-bye
  - utter_goodbye   
  
## error path 1
* greet: hello there!
  - utter_goodbye
* hospitalSearchQuery: list of health care centers located around Hyderabad
  - utter_forwardToHospitalSearch
  - action_get_hospital_search
* thanks: that's cool. much obliged
  - utter_welcome
* goodbye: see you later!
  - utter_greet
  
## error question 4
* greet: hi there!
  - utter_greet
* sideEffectsQuery: will there be any effects on using omeprazole
  - utter_forwardToSideEffects
  - action_get_side_effects
* thanks: thanks a lot
  - utter_goodbye
* goodbye: see you soon
  - utter_welcome