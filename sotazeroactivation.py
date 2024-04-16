"""
16/04/2024
Questa versione ad oggi riporta questi risultati:

Totale cime SOTA in Toscana: 238
Totale cime Non Valide/Inactive: 11
Totale cime Valide: 227
Cime mai attivate Valide: 115

che ad un controllo sia su SOTL.AS che SOTAMPAS.ORG risultano corretti
"""
import json
import datetime

# Apri il file tuscanysummit.json in modalità lettura
with open('tuscanysummit.json', 'r') as file:
    # Carica il contenuto JSON dal file
    data = json.load(file)

    # Data e ora corrente
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Crea una lista per gli elementi JSON con "ActivationCount" uguale a "0"
    never_activated = [item for item in data if item.get("ActivationCount") == "0"]

    # Identifica le cime non valide
    inactive_summits = [item for item in data if item.get("ValidTo") != "31/12/2099"]

    # Identifica le cime mai attivate che sono valide
    valid_never_activated = [item for item in never_activated if item.get("ValidTo") == "31/12/2099"]

    # Calcola i totali
    total_elements = {
        "Data elaborazione": current_datetime,
        "Totale cime SOTA in Toscana": len(data),
        "Cime mai attivate": len(never_activated),
        "Totale cime Inactive": len(inactive_summits),
        "Totale cime Valide": len(data) - len(inactive_summits),
        "Cime mai attivate Valide": len(valid_never_activated)  # Correttamente filtrate
    }

    # Scrive tutto in un unico file JSON, includendo il timestamp
    output_data = {"Timestamp": current_datetime, "Data": total_elements}
    with open('tuscanyzeroactivation.json', 'w') as outfile:
        json.dump(output_data, outfile, indent=4)

    # Stampa a console con timestamp
    print("======================================")
    print(f"Data elaborazione: {current_datetime}")
    print("======================================")
    print(f"Totale cime SOTA in Toscana: {total_elements['Totale cime SOTA in Toscana']}")
    print(f"Totale cime Non Valide/Inactive: {total_elements['Totale cime Inactive']}")
    print(f"Totale cime Valide: {total_elements['Totale cime Valide']}")
    print(f"Cime mai attivate Valide: {total_elements['Cime mai attivate Valide']}")  # Stampato il valore corretto
