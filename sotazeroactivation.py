"""
16/04/2024
deve essere fatto un controllo con i dati presenti su https://www.sotamaps.org/
perchè lì risultano 227 cime valide, mentre il risultato del programma attualmente è
il seguente:

       "Totale cime SOTA in Toscana": 236,
        "Cime mai attivate": 108,
        "Totale cime Inattive": 11,
        "Totale cime Valide": 225

RISULTATI DA VERIFICARE

"""
import json

# Apri il file tuscanysummit.json in modalità lettura
with open('tuscanysummit.json', 'r') as file:
    # Carica il contenuto JSON dal file
    data = json.load(file)

    # Crea una lista per gli elementi JSON con "ActivationCount" uguale a "0"
    filtered_data = [item for item in data if item.get("ActivationCount") == "0"]

    # Conta tutti gli elementi che hanno il campo "ValidTo" diverso da 31/12/2099
    count_inactive = sum(1 for item in data if item.get("ValidTo") != "31/12/2099")

    # Calcola il totale di elementi mai attivati escludendo quelli inattivi
    total_never_activated = len(filtered_data) - count_inactive

    # Calcola il totale di elementi trovati
    total_elements = {
        "Totale cime SOTA in Toscana": len(data),  # Numero totale di elementi nel file JSON
        "Cime mai attivate": total_never_activated,
        "Totale cime Inattive": count_inactive,
        "Totale cime Valide": len(data) - count_inactive  # Calcola le cime con "ValidTo" = 31/12/2099
    }

    # Combina i dati filtrati con il conteggio totale in un unico oggetto
    output_data = {"filtered_data": filtered_data, "total_elements": total_elements}

# Scrive tutto in un unico file JSON
with open('tuscanyzeroactivation.json', 'w') as outfile:
    json.dump(output_data, outfile, indent=4)

# Stampa a console per verifica immediata
print(json.dumps(output_data, indent=4))