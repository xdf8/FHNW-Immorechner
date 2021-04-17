# Immobilienpreisrechner

## Webservice

Auf FastAPI basierter Webserver, der eine Preisschätzung abgibt.

Die Dependencies können mit ```pip3 install -r requirements.txt``` installiert werden.
Der Server kann mit ```uvicorn main:app --reload``` gestartet werden.

Unter [http://127.0.0.1:8000/docs]() ist ersichtlich, dass ```/price_predict``` ein JSON als Body-Request erwartet.
In [test_prediction.json](test_prediction.json) ist solch ein exemplarisches JSON hinterlegt.
Im konkreten Fall antworter der Server mit:

```
[
  808524.5625
]
```

Das entspricht dem geschätzen Hauspreis auf Basis der eingegebenen Daten.