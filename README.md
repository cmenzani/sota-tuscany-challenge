# sota-tuscany-challenge


Bozza **MANIFESTO** 

**Obbiettivi:**

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

Legge il numero di elementi/referenze presenti nel file tuscanysummit.json cha hanno il campo ActivationCount==0 chesignifica che quella cime non è mai stata attivata.
            In questo modo potremo sempre tenere giornalmente aggiornata la dashboard: 
             
                SITUAZIONE AGGIORNATA al gg/mm/aaaa
                
                CIME ATTIVABILI: 227
                
                CIME ATTIVATE:    XX
                
                CIME DA ATTIVARE: YY
