


#def play():
 # i = 0

  #if i%3==0 and i%5==0 == "FizzBuzz":
  #  print()
 # elif i%3==0 == "Fizz":
 #   print()
 # elif i%5==0 == "Buzz":
 #   print()

 
Einführung = """Wilkommen zum FizzBuzz Spiel,
in diesem Spiel geht es darum, dass du uns beweist, ob du dividieren kannst.
Das Spiel wird dich von der Zahl 1 anfangend abfragen ob die Zahl durch 3, 5,
und/oder durch beide teilbar ist.
_____________________________________________________________________________

Die Regeln:
1. Die Eingaben werden mit Enter bestätigt

2. Ist die Zahl durch 3 teilbar schreibe !!! Fizz !!!

3. Ist sie durch 5 teilbar schreibe !!! Buzz !!!

4. Sollte die Zahl durch 3 und 5 teilbar sein schreib !!! FizzBuzz !!!

5. Bei nicht teilbaren Zahlen gebe nichts ein und fahre mit Enter fort

______________________________________________________________________

Solltest du eine falsche Antwort eingeben ist das Spiel vorbei
"""


print(Einführung)

i = 0
while True:
  i += 1
  input(f"{i}: ")  
  if i%3==0 and i%5==0 == "FizzBuzz":
    print("")
  elif i%3 == 0 == "Fizz":
    print("")
  elif i%5 == 0 == "Buzz":
    print("")
  #elif not i%3==0 and i%5==0 == "":
    #print("")
  #elif not i%3 == 0 == "":
    #print("")
  #elif not i%5 == 0 == "":
    #print("")
  else:
    print("your answer is incorrect")
    break