# Usa un'immagine base Python ufficiale.
FROM python:3.12

# Imposta una directory di lavoro nel container
WORKDIR /app

# Copia il file delle dipendenze e installale.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia il resto del tuo codice dell'applicazione nel container.
COPY . .

# Espone la porta su cui l'applicazione sarà accessibile.
EXPOSE 5000

# Definisce il comando per avviare l'applicazione.
CMD ["flask", "run", "--host=0.0.0.0"]
