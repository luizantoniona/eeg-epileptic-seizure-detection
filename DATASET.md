# Dataset
- O dataset é separado em exames de 24 individuos (chb01 ... chb24).
- Cada exame é separado em vários arquivos (chb01_01.edf ... chb24_21.edf).
- Cada exame contém um arquivo com as informações de cada um dos segmentos dos exames.

- Como exemplo:

```
['Data Sampling Rate: 256 Hz\n',
 '*************************\n',
 '\n',
 'Channels in EDF Files:\n',
 '**********************\n',
 'Channel 1: FP1-F7\n',
 'Channel 2: F7-T7\n',
 'Channel 3: T7-P7\n',
 ...
 '\n',
 'File Name: chb01_26.edf\n',
 'File Start Time: 12:34:22\n',
 'File End Time: 13:13:07\n',
 'Number of Seizures in File: 1\n',
 'Seizure Start Time: 1862 seconds\n',
 'Seizure End Time: 1963 seconds\n',
 '\n',
 ...
```
- Após analise das informações contidas nos súmarios, algumas informações importantes foram extraidas e convertidas para o modelo de tabela relacional á seguir:

|record_name| file_name | start_time | end_time | nr_seizures | start_seizure | end_seizure | nr_channels | ds_channels |
|:---------:|:---------:|:----------:|:--------:|:-----------:|:-------------:|:-----------:|:-----------:|:-----------:|
|ch01|chb01_01.edf|12:34:22|13:13:07|2|1862, 2000|1963, 2213| 24 | FP1-F7,F7-T7,...|

- Onde:
    - record_name: É o nome do exame principal do dataset;
    - file_name: É o nome do arquivo do exame;
    - start_time: É o tempo de inicio do exame do arquivo;
    - end_time: É o tempo final do exame do arquivo;
    - nr_seizures: O número de convulsões presentes no arquivo;
    - start_seizure: Uma lista com os tempos de inicio de cada convulsão;
    - end_seizure: Uma lista com os tempos de fim de cada convulsão;
    - nr_channels: O número de canais gravados no arquivo;
    - ds_channels: Uma lista com o nome de cada canal;

- Com o modelo de tabela relacional acima, podemos armazenar essas informações em um banco de dados para facilitar a leitura de informações presentes no dataset.

## Banco de dados
- O banco utilizado foi o MySQL, por ser um banco de fácil utilização e com as bibliotecas já implementadas em python.
- Foi criado uma tabela com as informações acima.
- As informações são inseridas em banco somente quando o arquivo do exame é baixado.

## Download do dataset
- Devido ao tamanho do dataset, optou-se por criar uma maneira dinâmica de realizar o download dos arquivos.
- Foi implementado um algoritmo que realiza a leitura dos sumários e verifica a necessidade de baixar ou não o exame.
    - Verifica se já existe o registro em banco;
    - Verifica se já existe o exame em disco;
    - Baixa o arquivo e faz a inserção no banco de dados de acordo com as verificações;
- Vantagem de utilizar o algoritmo para realizar o download é: poder parar a transfêrencia em qualquer momento, e retoma-la quando necessário.

## Leitura do dataset
- Após o ambiente configurado com o banco de dados e o dataset baixado, foi necessário encontrar formas para realizar a leitura dos arquivos de exame.
- Os arquivos são em formato .edf (European Data Format)(colocar link) que é o formato padrão projetado para troca e armazenamento de séries temporais médicas.
- Para realizar a leitura de cada arquivo, utilizou-se a biblioteca do MNE (https://mne.tools/stable/documentation/cite.html) por ser um pacote em python open source feita exclusivamente para explorar, visualizar e analisar dados neurológicos.
- Foi implementado um método de leitura dos arquivos criando uma Classe com as informações do banco e os dados do sinal utilizando a biblioteca do MNE.
- Com isso, temos um objeto com todas as informações necessárias para analise e utlização dos exames.

# Dataset Preview
- Com os dados devidamente armazenados e com o algoritmo de leitura dos arquivos funcionando, foi implementado em um Jupyter notebook a pré-visualização dessas informações.
- Foi analisado os dados temporais e comportamento dos mesmos, quando há e não há uma convulsão.
- Feito algumas transformações de domínio dessas informações para prévia analise do domínio de frequência.

-- COLOCAR IMAGENS MOSTRANDO AS ANALISES

# Pré-processamento:

-- Copiar trecho já escrito no artigo

-- Mencionar número de exames

-- Mencionar gerenciamento de memória

# Modelo

-- CNN e motivador para utiliza-la

-- Como chegou no modelo atual

-- Hiperparâmetros

## Treinamento

-- Shape de entrada dos dados

-- Número de amostras

-- Gráficos de treino

## Métricas

-- Copiar trecho já escrito no artigo

-- Explorar outras métricas q não seja acurácia

