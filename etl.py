import requests 
import pandas as pd


# dictionary in python
def extract() -> pd.DataFrame:
    """ Estrae i dati dal file CSV esposto tramite URL """
    API_URL = "https://dati-ustat.mur.gov.it/dataset/8caba27a-8e5f-431f-a926-daaa0a70fcf9/resource/1817f123-deb8-4687-b0a0-36e89f230d3d/download/2001-2009_laureatixclassexcorso.csv"
    
    try:
        df = pd.read_csv(API_URL ,encoding ='latin1', sep=';')
        print(f"Numero di righe nel CSV: {len(df)}")
        return df
    
    except requests.exceptions.RequestException as e:
        print(f"Errore nella richiesta API: {e}")
        return pd.DataFrame()  



def transform(df: pd.DataFrame) -> pd.DataFrame:
    print(f"Numero totale di record nel DataFrame: {len(df)}")
    
    # stampa le colonne disponibili
    print("Colonne disponibili:", df.columns.tolist())
    
    df = df[df["CLASSE"].str.contains("Ingegneria", case=False, na=False)]
    print(f"Numero di università che offrono corsi di Ingegneria: {len(df)}")
    
    df = df.reset_index(drop=True)
    
    # Seleziona le colonne di interesse
    return df[['Anno solare','CLASSE','LAUREATI_FEMMINE']]  

def load(df: pd.DataFrame, filename: str):
    """ Carica il DataFrame in un file CSV """
    try:
        df.to_csv(filename, index=False)
        print(f"Dati salvati in '{filename}'")
    except Exception as e:
        print(f"Errore durante il salvataggio: {e}")


# Esecuzione del processo ETL
df = extract()
if not df.empty:
    df_transformed = transform(df)
    load(df_transformed,'dati_laureati.csv')  # Salva in un file CSV
else:
    print("Estrazione fallita. Nessun dato disponibile.")