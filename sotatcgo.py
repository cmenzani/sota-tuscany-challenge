"""
.\venv\Scripts\activate
"""
import subprocess

import subprocess

def run_scripts_in_sequence():
    # Elenco degli script Python da eseguire in ordine
    scripts = [
        "sotatc.py",
        "sotafirstactivator-v2.py",
        "sotatuscanynewone.py",
        "tuscanydashboard.py"
    ]

    # Esegue ogni script e attende il suo completamento prima di procedere
    for script in scripts:
        print(f"Tentativo di esecuzione dello script: {script}")
        try:
            # Esegue lo script e cattura l'output
            result = subprocess.run(['python', script], check=True, text=True, capture_output=True)
            # Stampa l'output dello script e un messaggio di successo
            print(result.stdout)
            print(f"Script '{script}' completato con successo.")
        except subprocess.CalledProcessError as e:
            # Stampa l'output di errore e il messaggio di errore
            print(e.stdout)
            print(e.stderr)
            print(f"Errore durante l'esecuzione dello script '{script}': {e}")
            break

# Esegui la funzione
if __name__ == "__main__":
    run_scripts_in_sequence()
