# Analisi dei requisiti

## Contesto

Il Museo Diocesano di Monopoli propone visite guidate in italiano e in inglese, laboratori per ragazzi ed eventi speciali. Oggi le prenotazioni avvengono per telefono, solo durante l'orario di apertura e con almeno due giorni di anticipo. Le informazioni su orari e attività sono distribuite su siti diversi e non sempre coincidenti. Il museo non dispone di dati strutturati su partecipazione e gradimento.

La piattaforma digitalizza questo processo: prenotazione online con disponibilità in tempo reale, raccolta dei feedback e monitoraggio delle attività.

## Attori

| Attore | Descrizione |
|---|---|
| Visitatore | Consulta il calendario e il catalogo, prenota senza registrarsi, gestisce la prenotazione tramite un codice |
| Operatore | Personale del museo: gestisce le attività e registra le presenze |
| Amministratore | Ha le funzioni dell'operatore, consulta la dashboard e gestisce gli account del personale |

## Requisiti funzionali

| Requisito | Attore |
|---|---|
| Consultare il calendario delle attività future con tipo, lingua, data e posti disponibili, filtrandolo per tipo, lingua e disponibilità | Visitatore |
| Consultare il dettaglio di un'attività, comprese le opere che vi vengono illustrate | Visitatore |
| Prenotare un'attività indicando nome, email, telefono facoltativo, numero di biglietti interi e ridotti e consenso al trattamento dei dati; ricevere un codice di prenotazione e l'importo | Visitatore |
| Consultare e annullare una prenotazione tramite il codice | Visitatore |
| Lasciare un feedback (voto da 1 a 5 e commento facoltativo) dopo l'attività | Visitatore |
| Consultare il catalogo delle opere, con autore, datazione, tecnica e sala | Visitatore |
| Accedere all'area riservata con email e password | Operatore, Amministratore |
| Creare, modificare e annullare le attività | Operatore, Amministratore |
| Consultare l'elenco dei partecipanti di un'attività e registrarne la presenza o l'assenza | Operatore, Amministratore |
| Consultare la dashboard: attività svolte, prenotazioni, partecipanti, incasso, tasso di riempimento, tasso di assenze, voto medio, suddivisione per tipo e lingua, andamento settimanale, ultimi commenti | Amministratore |
| Consultare l'elenco del personale e creare nuovi account assegnando il ruolo | Amministratore |

## Regole del museo

1. I posti prenotati non possono mai superare la capienza dell'attività, anche con richieste simultanee.
2. Le prenotazioni si chiudono 2 giorni prima dell'inizio dell'attività.
3. Sono previste tre tariffe: intero, ridotto (ragazzi dai 14 ai 18 anni) e tariffa di gruppo per le prenotazioni oltre le 20 persone.
4. Una singola prenotazione comprende al massimo 40 biglietti.
5. Una prenotazione si può annullare solo prima dell'inizio dell'attività; l'annullamento libera i posti.
6. Il feedback si può inviare una sola volta per prenotazione, solo dopo la conclusione dell'attività e non in caso di assenza registrata.
7. La capienza di un'attività non può scendere sotto il numero di posti già prenotati.
8. Le attività annullate non sono prenotabili.

## Requisiti non funzionali

1. **Architettura a livelli**: interfaccia web, backend con API REST, database relazionale.
2. **Sicurezza**: password conservate solo come hash, accesso con token a scadenza, permessi verificati dal backend in base al ruolo, chiavi segrete fuori dal codice.
3. **Integrità dei dati**: vincoli definiti anche nel database, non solo nel codice.
4. **Portabilità**: SQLite in locale e PostgreSQL in produzione senza modifiche al codice.
5. **Usabilità**: interfaccia utilizzabile da computer e smartphone, con attenzione all'accessibilità.
6. **Riproducibilità**: dipendenze dichiarate, istruzioni di esecuzione, dati simulati rigenerabili.
7. **Verificabilità**: ogni regola del museo è coperta da almeno un test automatico.
8. **Riservatezza**: raccolta dei soli dati necessari, nessun dato personale dei visitatori esposto nelle pagine pubbliche.

## Funzionalità non incluse nel prototipo

Il prototipo si concentra sul processo di prenotazione e sul monitoraggio delle attività. Le seguenti funzionalità sono state escluse deliberatamente e sono indicate come possibili sviluppi futuri:

- **Registrazione dei visitatori**: il visitatore prenota senza creare un account, perché il pubblico è in gran parte occasionale (ad esempio turisti) e per raccogliere solo i dati strettamente necessari. Un account facoltativo per i visitatori abituali consentirebbe di consultare lo storico delle prenotazioni.
- **Invio automatico di email** di conferma e promemoria, che permetterebbe anche di recuperare il codice di prenotazione smarrito.
- **Pagamento online** dei biglietti, ad esempio tramite Stripe.
- **Biglietteria per l'ingresso libero**, senza visita guidata.
- **Applicazione mobile nativa**.

## Fonti

- Ministero della Cultura, scheda del Museo Diocesano di Monopoli (cultura.gov.it)
- Città di Monopoli, pagine dedicate al museo e agli eventi (comune.monopoli.ba.it)
- Monopoli City Tourism, pagina "I musei" (monopolitourism.com)