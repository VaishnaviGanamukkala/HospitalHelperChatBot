## intent:greet
- hi there
- hi
- hey
- hello
- hello there
- good day
- good morning
- morning
- good afternoon
- good evening

## intent:goodbye
- bye
- bye bye
- see you again
- see you later
- see you soon
- see you
- i’m off
- i’m out
- goodbye
- peace out
- catch you later
- nice chatting with you
- talk to you later
- it’s nice meeting you
- all right then
- bye for now

## intent:thanks
- thanks
- thank you
- thank you so much
- great thank you
- wow that’s great
- thanks a lot
- thank you very much
- that’s great thank you
- i appreciate your help, thank you
- i am so thankful

## intent:options
- how can you help me
- what can you do
- what can you provide
- what do you do
- can you help me
- what support you offer
- what help you provide
- how can you be helpful
- what can I expect from you
- what can you do?

## intent:sideEffectsQuery
- what are the side effects of [paracetamol](medicine)
- does [ibuprofen](medicine) have any after effects
- will anything happen with [insulin](medicine) intake
- [omeprazole](medicine) side effects
- health consequences of [calcium](medicine)
- aftermaths resulting due to [prednisone](medicine)
- is body harm caused by [nexium](medicine)
- side effects of [sodium](medicine)

## intent:hospitalSearchWithNoLocation
- can i find the hospitals near me?
- what health facilities are near me?
- health centers near me
- best hospitals around me
- i want to know the clinics in the area i live in

## intent:hospitalSearchQuery
- what are the hospitals in [hyderabad](location)
- can you name the hospitals in [bangalore](location)
- give the names of hospitals in [chennai](location)
- find out the hospitals in [pune](location)
- does [delhi](location) has any hospitals
- what are the best hospitals in [mumbai](location)

## intent:symptomsAnalysisQuery
- can you diagonise my symptoms
- what diseases could i have
- what can be the possible diseases for my symptoms
- which doctor should i meet with my present health signs
- which medical specialization should i visit with my symptoms
- do i have a disease
- should i visit a doctor
- do i have any medical disorders
- which doctor should i visit
- could i be having any health issues
- which hospital should i go

## intent:informSymptoms
- I'm having [Headache](symptoms) , [Nausea](symptoms) and [Tiredness](symptoms)
- I have the symptoms [weakness](symptoms) , [Weight gain](symptoms)
- [Vomiting](symptoms) , [Sweating](symptoms) , [Palpitations](symptoms) , and [Nausea](symptoms)
- [Dizziness](symptoms) is the trouble i have
- [Cough](symptoms) , [Fever](symptoms) , [Runny nose](symptoms) , [Shortness of breath](symptoms) , [Sore throat](symptoms) are the symptoms i have
- I feel [Chest pain](symptoms) , [Chest tightness](symptoms) , [Chills](symptoms) , [Cold sweats](symptoms) , [Heartburn](symptoms) and get [Sputum](symptoms)
- I have [Burning eyes](symptoms) , [Dry eyes](symptoms) and [Eye redness](symptoms)
- i have [cold cough](symptoms) and [fever](symptoms)
- i have [fever](symptoms) and [cough](symptoms)

## intent:informYOB
- i'm born in [1969](year_of_birth)
- my year of birth is [2012](year_of_birth)
- i was born in the year [2001](year_of_birth)
- my birth year is [1999](year_of_birth)
- [1899](year_of_birth)

## intent:informLocation
- i'm in [hyderabad](location)
- my city is [bangalore](location)
- [chennai](location)
- i'm near [pune](location)

## intent:informGender
- i'm a [female](gender)
- my gender is [male](gender)
- [hetero](gender)
- my sex is [asexual](gender)
- i'm [transgender](gender)
- [gay](gender)
- i'm identified as [lesbian](gender)
- my gender identity is [bisexual](gender)


## synonym:female
- girl
- woman
- lady
- f

## synonym:male
- boy
- man
- gent
- m

## regex:year_of_birth
- [0-9]{4}

## lookup:medicine
  data/lookup_tables/medicinalproducts.txt
  
## lookup:location
  data/lookup_tables/cities.txt

## lookup:symptoms
  data/lookup_tables/symptoms_sandbox.txt
