from importlib import reload

import classes
import json

with open('scraHS.json', 'r', encoding="utf-8") as fin:
    highskors = json.load(fin)
    sorths = sorted(highskors.items(), key=lambda x: x[1])

alp=1 #ο αλγοριθμος του υπολογιστη
print(
"┏━━━┓          ┏┓ ┏┓ ┏┓\n"
"┃┏━┓┃          ┃┃ ┃┃ ┃┃\n"
"┃┗━━┳━━┳━┳━━┳┓┏┫┗━┫┗━┫┃┏━━┓\n"
"┗━━┓┃┏━┫┏┫┏┓┃┗┛┃┏┓┃┏┓┃┃┃┃━┫\n"
"┃┗━┛┃┗━┫┃┃┏┓┃┃┃┃┗┛┃┗┛┃┗┫┃━┫\n"
"┗━━━┻━━┻┛┗┛┗┻┻┻┻━━┻━━┻━┻━━┛")

def selections():
  
  print("***** Scrambble *****\n "
        "---------------------\n"
        "1: Σκορ\n"
        "2: Ρυθμισεις \n"
        "3: Παιχνιδι \n"
        #αμα δωθει η επιλογη 3 τρεχει αυτοματα με τον smart fail
        #"d: Σχολια κωδικα\n"
        "q: Εξοδος\n"
        "---------------------\n")
  
  
  ap=input("Επιλεξτε καποια απο τις παραπανω επιλογες: ")
  return ap




def choice(ap):
  if(ap=='1'):
      pos=1
      
      for i,j in sorths[:5:-1]:
          print(pos,". Ονομα: ",i," Σκορ: ",j)
          pos+=1
      
        
  
  elif(ap=='2'):
      print("Αλγοριθμοι του Η/Υ στο scrambble")
      print("1. FAIL algorithm")
      print("2. MIN-MAX algorithm")
      print("3. SMART algorithm ")
      print("4. MAX algorithm")
      print("5. MIN algorithm")
      al = input("Επιλεξτε εναν απο τους αλγοριθμους και το παιχνιδι θα ξεκινησει αυτοματα με βαση την επιλογη: ")
      
      if (al=='1'):
          print("Ο υπολογιστης θα παιξει με FAIL αλγοριθμο")
          alp=1
      elif(al=='2'):
          print("Ο υπολογιστης θα παιξει με MIN-MAX αλγοριθμο")
          alp=2
      elif(al=='3'):
          print("Ο υπολογιστης θα παιξει με SMART αλγοριθμο")
          alp=3
      elif(al=='4'):
          print("Ο υπολογιστης θα παιξει με MAX αλγοριθμο")
          alp=4
      elif(al=='5'):
          print("Ο υπολογιστης θα παιξει με MIN αλγοριθμο")
          alp=5
      else:
          print ("Λαθος απαντηση ο υπολογιστης θα παιξει με τον προκαθορισμενο αλγοριθμο")
      game1 = classes.Game()
      game1.setup(alp)
  
  
  
  
  elif(ap=='3'):
      alp=1
      game1 = classes.Game()
      game1.setup(alp)
  elif(ap==">>> help(guidelines)"):
      print(classes.guidelines())
  else:
      print("Αντιο")
      exit(202)

ap = selections()
while True:
  choice(ap)
  ap=selections()