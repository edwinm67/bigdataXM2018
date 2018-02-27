# Universidad EAFIT
# Curso Big Data - XM, 2018
# Profesor: Edwin Montoya M. – emontoya@eafit.edu.co

## ->CONECTARSE AL CLUSTER CLOUDERA:

### Conectarse a la VPN

### Desde la estación Cliente Windows desde Internet:

* Descargar putty.exe y colocarlo en el Escritorio.
* Ejecutar putty.exe

      Host Name (or IP address):
      192.168.10.115

      Port: 22 (dejarlo asi):

      Click en "Open"

      login as: xm##      (usuario asignado)
      password: ********        (password asignado)

### Desde una estación Linux o Mac desde Internet:

* Abrir una terminal

      user@hostname$ ssh xm##@192.168.10.115
      Passoword: ***** (password asignado a cada usuario)

### Por Web:

* Desde un browser: http://192.168.10.115:8888 (por la Intranet via VPN)
* Desde un browser: http://<hostname>.dis.eafit.edu.co (por la Internet)


## ->DATASETS

* [datasets](datasets)

## 1. SISTEMA DE ARCHIVOS HDFS

* [HDFS](01-hdfs)

## 2. PROCESAMIENTO - MAP/REDUCE

* [MapReduce](02-mapreduce)

## 3. Lenguaje PIG

* [Pig](03-pig)

## 4. Bases de datos SQL - Hive y Sqoop

* [Hive-Sqoop](04-hive-sqoop)

## 5. Bases de datos No SQL - Columnares - Hbase

* [Hbase](05-hbase)

## 6. Spark

* [Spark](06-spark)