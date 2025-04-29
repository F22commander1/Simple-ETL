# ETL Laureati Ingegneria

Questo semplice progetto esegue un processo ETL (Extract,Transform,Load) sui dati del MIUR relativi ai laureati italiani tra il 2001 e il 2009, filtrando in particolare i corsi di **Ingegneria**.

## 📁 Descrizione

Il flusso del processo è il seguente:

1. **Estrazione**: scarica i dati da una fonte ufficiale MIUR (formato CSV).
2. **Trasformazione**: filtra solo i corsi con "Ingegneria" nel nome e seleziona le colonne più significative.
3. **Salvataggio**: esporta i dati trasformati in un file `dati_laureati.csv`.

## 🔧 Requisiti

- Python 3.7 o superiore
- Pandas
- Requests

## 📚 Fonte dei dati
I dati sono forniti dal portale open data del MIUR e sono accessibili pubblicamente. Dataset utilizzato:
Titolo: Laureati per classe di corso

## 🔒 Licenza
Questo progetto è distribuito sotto licenza MIT. Puoi copiarlo, modificarlo e riutilizzarlo liberamente.
