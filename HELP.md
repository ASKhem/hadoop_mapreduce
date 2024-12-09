# 🚀 Laboratorio Hadoop
## 🛠️ Preparación
- Configura a conexión ao CESGA
- Conéctate ao CESGA
- Comproba que tes acceso a Hadoop:
  - `hadoop`
  - `yarn`

## 🔐 Configuración de Conexión SSH
Edita o ficheiro `config` dentro do directorio `~/.ssh/`, onde tes as chaves RSA:

Por exemplo:
```
Host hadoop
Hostname hadoop.cesga.es
User o_teu_userXX
IdentityFile ~/.ssh/chave_privada
```

## 📋 Tarefa 1
Nesta tarefa créase un ficheiro `.txt` con elementos de varias listas da compra, todos nun único ficheiro. O ficheiro envíase a un clúster de almacenamento HDFS. A continuación, lánzase un traballo MapReduce sobre o ficheiro para utilizar a potencia de supercomputación do CESGA para contar o número de veces que aparece cada palabra no ficheiro. Finalmente, copiamos os ficheiros obtidos á nosa conta local e verificamos o resultado.

1. Entrar en Hadoop (CESGA):
   ```
   ssh hadoop
   ```

2. Comprobar que funciona:   
   ```
   hadoop
   ```

3. Comandos para traballar con HDFS:
   ```
   hdfs dfs -ls             # listar contido en HDFS
   hdfs dfs -mkdir carpeta  # crear carpeta en HDFS
   hdfs dfs -rm -r carpeta  # eliminar carpeta en HDFS
   ```

4. Crear o ficheiro `lista_compra.txt`:
   ```
   nano lista_compra.txt
   ```

5. Copiar o ficheiro a HDFS:
   ```
   hdfs dfs -put lista_compra.txt
   hdfs dfs -ls
   ```

6. Mostrar bloques e localización do ficheiro nos diferentes nodos do clúster:
   ```
   hdfs fsck lista_compra.txt -files -blocks -locations
   ```

7. Lanzar un traballo WordCount:
   ```
   yarn jar /opt/cloudera/parcels/CDH-6.1.1-1.cdh6.1.1.p0.875250/jars/hadoop-mapreduce-examples-3.0.0-cdh6.1.1.jar wordcount lista_compra.txt contalista
   ```

8. O resultado gárdase en HDFS. Traemos o resultado ao noso sistema de ficheiros:
   ```
   hdfs dfs -get contalista
   ```

9. Comprobar o resultado:
   ```
   cat contalista/*
   ```

## 📋 Tarefa 2
En esta tarefa, cada persoa creará unha lista da compra persoal con un mínimo de 20 elementos. Copiaránse todas as listas á carpeta local temporal `/tmp/listas`. Enviaránse as listas ao clúster de almacenamento HDFS e executarase un traballo que conte todos os elementos. A diferenza da tarefa 1, nesta ocasión realízase o traballo paralelo sobre unha carpeta con 20 ficheiros diferentes.

Pasos a seguir:

1. Cada un escribe na súa conta a súa lista da compra: `lista_iniciais_nome_apelidos.txt` (20 elementos).

2. Copiar a lista da compra a `/mnt/listas/`:
   ```
   cp lista_iniciais_nome_apelidos.txt /mnt/listas
   ```

3. Enviar carpeta con listas ao clúster HDFS:
   ```
   hdfs dfs -put /mnt/listas
   ```

4. Verificar que hai unha nova carpeta con listas en HDFS:
   ```
   hdfs dfs -ls
   hdfs dfs -ls listas
   ```

5. Lanzar traballo WordCount para que conte todos os elementos das listas:
   ```
   yarn jar /opt/cloudera/parcels/CDH-6.1.1-1.cdh6.1.1.p0.875250/jars/hadoop-mapreduce-examples-3.0.0-cdh6.1.1.jar wordcount listas resumolistas
   ```

6. Copiar resultado desde clúster HDFS a conta local:
   ```
   hdfs dfs -get resumolistas
   ```

7. Revisar resultado:
   ```
   cd resumolistas  # hai un ficheiro SUCCEEDED??
   ```

## 🆘 AXUDA
Para enviar ficheiros entre unha máquina e outra, pode ser útil o comando `scp`. SCP é un CP sobre SSH, é dicir, realiza copias de un ficheiro desde un host orixe a un host destino.
   ```
   scp ficheiro.txt usuario@host_destino: # copia ficheiro.txt a /home/usuario/ da máquina: host_destino
   ```
Para descomprimir un ficheiro `.zip`, podes utilizar o comando `unzip`, por exemplo:
    ```
    unzip fichero.zip
    ```
Para crear un ficheiro con los resultados de hacer cat:
    ```
    cat contalista/ > resultado.txt
    ```
