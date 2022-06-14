import pyperclip

pss = { 'facebook': 'lucone123', 'instagram': 'lucanoig'}


z=0
while z!=1:
  print("Inserisci il nome del sito. \n")
  for sito in pss:
    print(" -"+sito)

  x = input()
  try:
    pselect = pss[x]
    pyperclip.copy(pselect)
    print("Ora puoi incollare la password")
    z=1
  except:
    print("hai scritto male fratm")
    z = 0
input()


#Programma fatto male ma funziona, non ho voglia di perfezionarlo.
