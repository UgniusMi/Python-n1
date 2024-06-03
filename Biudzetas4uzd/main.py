from biudzetas import Biudzetas

biudzetas = Biudzetas()

while True:
    pasirinkimas = input("Pasirinkite veiksma:\n1. Prideti pajamas\n2. Prideti islaidas\n3. Parodyti balansa\n4. Ataskaita\n5. Baigti\n")
   
    if pasirinkimas == "1":
        pajamos = float(input("Iveskite pajamas: "))
        siuntejas = input("Iveskite siunteja: ")
        papildoma_informacija = input("Iveskite papildoma informacija: ")
        biudzetas.prideti_pajamu_irasa(pajamos, siuntejas, papildoma_informacija)
   
    elif pasirinkimas == "2":
        islaidos = float(input("Iveskite islaidas: "))
        atsiskaitymo_budas = input("Iveskite atsiskaitymo buda: ")
        isigyta_preke_paslauga = input("Iveskite isigyta preke paslauga: ")
        biudzetas.prideti_islaidu_irasa(islaidos, atsiskaitymo_budas, isigyta_preke_paslauga)
 
    elif pasirinkimas == "3":
        print(f"Balansas: {biudzetas.gauti_balansa()} EUR")
 
    elif pasirinkimas == "4":
        print("Ataskaita:")
        print(biudzetas.gauti_ataskaita())
 
 
    elif pasirinkimas == "5":
        print("Programa baige darba.")
        break
 
    else:
        print("Netinkamas pasirinkimas. Bandykite dar karta.")