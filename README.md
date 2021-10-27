# ambev assd 


<img src="/icon.png" alt="drawing" width="120"/>  

## O que é o ASSD?

O ambev **ASSD** é um algoritmo de distribuição de estoques que busca equilibrar os SKUs dos depósitos da Ambev sejam eles dos centros de distribuição **(CDD)** ou das fábricas. O ASSD é consciente da natureza não linear das vendas dos produtos Ambev, que pode variar de acordo com cenarios, como por exemplo: um maior calor em determinada região, feriados regionais, ou simplesmente um desequilibrio em um CDD causado por grandes demandas de grandes supermercados ou revendedores.

O algoritmo implementa um mecanismo de otimização baseado em prioridades, no qual prioriza os depósitos com menor nível de estoque desejado, que pode variar com a demanda prevista esperada.

#### Objetivos / Métricas de interesse

- Garantir a disponibilidade dos SKUS em todos os estoques
- Evitar vencimento de produtos
- Reduzir custos de transporte durante a escolha dos fornecedores 
- Rebalancear os estoques de acordo com as demandas locais repentinas


#### Otimização

A otimização é feita em dois níveis:

1) A nível de distribuição, onde as produções das fábricas são distribuidas entre os CDDs buscando otimizar as métricas de interesse
2) A nível de depósito, onde se busca equilibrar os depósitos de acordo com a necessidade, quando um depósito fica desequilibrado, seja por:  
   - uma alta demanda, por exemplo, devido a grandes carradas feita por uma grande rede de supermercados;

   - ou quando um CDD não vende um SKU como esperava e fica com estoque excedente.

##### [Link da Apresentação do Projeto](https://docs.google.com/presentation/d/1vmMnY2uUdm0bWoeyEkHTZT8bn_Ae7MmfZ-AjhboeY1g/edit?usp=sharing)

## Arquitetura

<p align="center">
  <img src="/arquitetura.png" alt="drawing"/>
</p>

- **Distance Calculator**: módulo responsável por consultar a API do googlemaps e calcular as distâncias entre as fábricas e os CDDs listados no arquivo de entrada `data.csv`. O resultado é uma tabela com informações contendo o código de origem/destino bem como suas latitudes e longitudes e a distrancia saindo da origem para o destino. Note de d(CDD1, CDD3)  não necessáriamente é igual a d(CDD3, CDD1), ja que a API do googlemaps calcula a distancia real, considerando estradas e possíveis problemas no caminho.
- **CSV Handler**: é o responsável por ler o dataset da pasta [`input`](https://github.com/viniciusbds/ambev-assd/tree/main/input) e por salvar o resultado final em [`results`](https://github.com/viniciusbds/ambev-assd/tree/main/results)
- **Distributor**: distribui a produção `Available to Deploy` para os CDDs, usando o algoritmo de distribuição de estoques baseado em prioridades ASSD
- **Rebalancer**: rebalanceia os estoques, considerando o seu nível de estoque atual e o nível de estoque desejado. Caso tenha excedente, distribui os SKUs para CDDs que mais precisam e que possua um custo de transporte menor, a fim de otimizálo.

## Pré requisitos

- ubuntu os
- python3
- openpyxl
- pandas
- [googlemaps](https://github.com/googlemaps/google-maps-services-python)

para instalar basta executar:
```bash 
pip install [deendency]
```

## Como executar?

### 1° Insira o dataset no diretório [`input`](https://github.com/viniciusbds/ambev-assd/tree/main/input)

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

### 2° Execute o código principal

```bash
python3 main.py 
```

### 3° Os resultados estarão em [`results`](https://github.com/viniciusbds/ambev-assd/tree/main/results)

Serão dois arquivos: **distribution-result.csv** e **rebalance-result.csv**, que contém as seguintes colunas:


| Supply Site Code | SKU | Location Code | Average daily demand (Hl)| Location Type | MinDOC (Hl) | Reorder Point (Hl) | MaxDOC  (Hl) | Old Closing Stock | New Closing Stock | Available to Deploy
| ---------------- | --- | ------------- | ------------------------ | ------------- | ----------- | ------------------ | ------------ | -- | ------------- | ----------------- |

`Old Closing Stock` : quantidade do **SKU** no depósito **Location Code** antes da execução do algoritmo

`New Closing Stock` : quantidade do **SKU** no depósito **Location Code** depois da execução do algoritmo


###### Logo [Icon](./icon.png) made by [Freepik](https://www.flaticon.com/br/autores/freepik) from [www.flaticon.com](https://www.flaticon.com/br/)
