import time
import os
import sys

def clear_screen():             #s tímhle pomohl GPT
    if os.name == 'nt':  
        os.system('cls')
    else:  
        os.system('clear')

clear_screen()

#loading

import time

def loading():
    print("""
XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX

       Loading [----------------------]

XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX           
""")
    time.sleep(0.5)
    clear_screen()
    print("""
XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX

       Loading [##--------------------]

XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX           
""")
    time.sleep(0.5)
    clear_screen()
    print("""
XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX

       Loading [#####-----------------]

XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX           
""")
    time.sleep(0.5)
    clear_screen()
    print("""
XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX

       Loading [########--------------]

XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX           
""")
    time.sleep(0.5)
    clear_screen()
    print("""
XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX

       Loading [###############-------]

XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX           
""")
    time.sleep(0.5)
    clear_screen()
    print("""
XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX

       Loading [######################]

XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX           
""")
    time.sleep(1.5)
    clear_screen()
    print("""
XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX

              Loaded ... starting

XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX           
""")
    time.sleep(4)
    clear_screen()

pokoj1 = '''
     _______________
    | stůl |        |
    |------+        |
    |    +-------+  |
    o    |koberec|  |
    k    |       |  |
    n    +-------+  |
    o               |
    |-----+         |
    |skříň|         |
    |_____|__  |____|

'''

objekty = {
    "okno": "Na okně nevidíte nic neobvyklého.",
    "stul": "Pod stolem není nic kromě prachu a pavučin.",
    "skrin": "Skříň je zamčená. Chcete ji odemknout?",
    "koberec": "Koberec je zahnutý. Chcete ho zvednout?"
}

klic = 0

print(loading())

#vytvořit účet

print(""" 
XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX
      
   Před začátkem hry si prosím vytvořte účet

XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX  
            """)

jmeno = str(input("Zadejte herní nick: "))
vek = int(input("Zadejte váš věk: "))

if vek < 18:
    print(" Co děláš na počítači? Běž ven!")
    time.sleep(2)
    sys.exit()
else:
    pass

print("Zadejte číslo kreditní karty: ")
time.sleep(1)
print("Just kidding! :)                                                                                                                   ...maybe")
time.sleep(3)
clear_screen()

#start

print(f"""
XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX
      
  Hmm "{jmeno}", zajímavé jméno. Takže ty jsi
   ten nový vyšetřovatel jo? No tak schválně,
    předveď, co umíš. Čas ti přidělit nějaký
               pořádný případ.
      
XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX     
      """)
time.sleep(12)
clear_screen()

print("""
XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX 

                Úkol číslo 1

XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX
""")
print(pokoj1)

print("Jste na místě činu. Byla zde u okna nalezena mrtvola. Ta vás teď ale nezajímá. Vaším úkolem je najít všechny důkazy, které by nám mohli pomoci")
print("Až nebudete chtít dále pokračovat v hledání, napište konec")
print()
while True:
    objekt = input("Co chcete prohledat (okno, stul, skrin, koberec)? ").lower()
    if objekt in objekty:
            if objekt == "skrin":
                odpoved = input("Skříň je zavřená. Chcete ji otevřít (ano/ne)? ").lower()
                if odpoved == "ano":
                    print("Otevřeli jste skříň, kde se schovával vrah, který vás zabil. Hodně štěstí příště...")
                    time.sleep(3)
                    sys.exit()
                else:
                    print("Rozhodli jste se neodemknout skříň.")

            elif objekt == "koberec":
                odpoved = input("Chcete zvednout koberec (ano/ne)? ").lower()
                if odpoved == "ano":
                    print("Pod kobercem je klíč, který tu stihla oběť ukrýt, než byla zabita!")
                    klic = 1
                else:
                    print("Rozhodli jste se nezvedat koberec.")
            else:
                print(objekty[objekt])
    elif objekt == "konec":
        break
    else:
        print("Tohle nelze prohledat. Zkuste to znovu.")

clear_screen()
print("""
XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX 

     Doufám, že jsi něco našel. Mám tu pro
   tebe ještě něco, co jsme tu našli před tím,
     než jsi přišel ty. Je to starý trezor
         od kterého však nemáme klíč.
           Neviděl jsi ho náhodou?

XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX
""")
time.sleep(6)

if klic == 1:
    print("Ty: Ano viděl, našel jsem ho pod kobercem.")
    time.sleep(4)
    print("Velitel: Tak safe je tvůj, já už mám dnes padla.")
    time.sleep(5)
else:
    print("Ty: Žádný klíč jsem neviděl")
    time.sleep(3)
    print("Velitel: Tak se na to podíváme jindy, pro dnešek hotovo. Můžeš jít domů. Přeji hezký zbytek dne.")
    time.sleep(5)
    sys.exit()
clear_screen()
print("""
XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX 

                Úkol číslo 2

XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX
""")
print("Otevřel jsi trezor s klíčem a našli jste morseovskou zprávu.")
print("Zpráva zní: ...-  .-.  .-  ....  .  -- / .---  . / .---  .-  .-.  ---  ... .-..  .-  ...- ")
print("Tvým úkolem je tuto zprávu rozluštit z morseovy abecedy na text a najít jméno vraha.")
print()
odpoved = input("Napište jméno vraha z této zprávy: ").strip()
print()
if odpoved.lower() == "Jaroslav".lower():
    print("Správně! Jméno vraha bylo Jaroslav, který dříve oběti vyhrožoval pokud mu nedá jeho peníze. Pro jistotu oběť dala zašifrovanou zprávu do trezoru, pro případ, že by mu Jaroslav opravdu něco udělal.")
    time.sleep(8)
else:
    print(f"Bohužel, jméno vraha nebylo {odpoved} ale Jaroslav. Hru jste neprohráli ale nejse ani moc dobrý vyšetřovatel. Třeba to bude příště lepší")
    time.sleep(6)

clear_screen()
print("""
XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX     

                 Konec hry!

XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX
""")
time.sleep(5)
sys.exit()
