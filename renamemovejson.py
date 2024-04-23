"""
.\venv\Scripts\activate
"""
import os
from datetime import datetime

def rename_and_move_files():
    # Ottiene la data odierna in formato stringa
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Elenco dei file da rinominare e spostare
    files_to_process = ["tuscanydashboard.json", "firstactivator-v2.json", "tuscanysummit.json"]
    directory = "backup"

    # Crea la directory di backup se non esiste
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Processa ciascun file
    for file_name in files_to_process:
        if os.path.exists(file_name):
            # Costruisce il nuovo nome del file con la data
            new_file_name = f"{today}-{file_name}"
            # Rinomina e sposta il file
            os.rename(file_name, os.path.join(directory, new_file_name))
            print(f"File '{file_name}' rinominato e spostato con successo.")
        else:
            # Stampa un messaggio se il file non esiste
            print(f"Il file '{file_name}' non esiste e non può essere processato.")

# Esegui la funzione
if __name__ == "__main__":
    rename_and_move_files()
