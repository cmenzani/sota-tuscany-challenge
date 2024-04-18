# sota-tuscany-challenge


Bozza **MANIFESTO** 

**Obiettivi:**

Incentivare l'attività SOTA nella regione.
Incentivare i NEW ONE
Raggiungere entro la fine del 2025 l'attivazione di tutte le 227(*) cime della Toscana.

(*) ad esclusione di quelle non attivabili perchè zone private o aree protette (vedi Isola di Montecristo)

**Riconoscimenti/Award:**

Ogni 5 attivazioni NEW ONE l'attivatore riceverà dal team del SOTA Tuscany Challenge una T-shirt ed un Buono AMAZON da €30





**Note ai sorgenti**

*sotatc.py*  

Legge il file "https://storage.sota.org.uk/summitslist.csv" che giornalmente viene aggiornato da SOTA.UK estrae le sole referenze della Toscana creando il file *tuscanysummit.json*

*sotazeroactivation.py*

Legge il numero di elementi/referenze presenti nel file *tuscanysummit.json* cha hanno il campo ActivationCount==0 chesignifica che quella cime non è mai stata attivata.
            In questo modo potremo sempre tenere giornalmente aggiornata la dashboard: 
             
            ======================================
            Data elaborazione: 2024-04-16 11:31:27
            ======================================
            Totale cime SOTA in Toscana: 238
            Totale cime Non Valide/Inactive: 11
            Totale cime Valide: 227
            Cime mai attivate Valide: 115


*sotafirstactivator.py*

Legge *tuscanysummit.json*  e per ogni cima che è stata attivata almeno una volta (quindi esclude tutte le referenze che hanno il campo ActivationCount = 0) va a leggere mediante API un set di dati fra i quali ci sono quelli relativi alla **prima attivazione**


**Note OPERATIVE**

Al momento per aggiornare le statistiche con le ultime "prime attivazioni" è necessario far girare in sequenza i 3 script:

*sotatc.py* 
  
*sotazeroactivation.py*

*sotafirstactivator.py*




**Note API**

recupera l'Honor Roll degli Attivatori italiani


https://api-db.sota.org.uk/admin/activator_roll?associationID=54

presenta l'elenco delle referenze e cliccando su ognuna si ottiene l'elenco degli attivatori

  https://sotl.as/summits/I/TO
 

