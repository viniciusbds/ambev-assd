# Input

Essa base de dados inclui dois arquivos principais:

#### data.csv

| Supply Site Code | SKU | Location Code | Average daily demand (Hl)| Location Type | MinDOC (Hl) | Reorder Point (Hl) | MaxDOC  (Hl) | Closing Stock | Available to Deploy
| ---------------- | --- | ------------- | ------------------------ | ------------- | ----------- | ------------------ | ------------ | ------------- | ----------------- |


#### localization.csv

| Instalation Code | Latitude | Longitude |
| ---------------- | -------- | --------- |

#### distances.csv

| originCode | originLatitude | originLongitude | destinyCode | destinyLatitude | destinyLongitude | distance |
| ---------------- | -------- | --------- | -- | ---------------- | -------- | --------- |

Essa tabela pode ser inserida diretamente no diretório ou gerada execurando o script [distancecalculator.py](https://github.com/viniciusbds/ambev-assd/blob/main/distancecalculator.py)