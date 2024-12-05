# 🚀 Ejercicio 2: Trabajando con MapReduce

## 🎯 Objetivo
- 🧠 Comprender el funcionamiento del trabajo distribuido basado en técnicas MapReduce
- 🔧 Modificar mappers y reducers para obtener diferentes resultados a partir de los datos

## 📚 Guía de Uso

### 🔍 Pruebas Locales
Antes de ejecutar en Hadoop, puedes probar tu código localmente:

1. **Crear datos de prueba** 📝
```bash
head -n100 purchases.txt > mini_purchases.txt
```

2. **Visualizar datos** 👀
```bash
cat mini_purchases.txt
```

3. **Probar el mapper** 🗺️
```bash
cat mini_purchases.txt | python mapper.py
```

4. **Ordenar resultados** 📊
```bash
cat mini_purchases.txt | python mapper.py | sort
```

5. **Ejecutar pipeline completo** ⚡
```bash
cat mini_purchases.txt | python mapper.py | sort | python reducer.py
```

### 💡 Tip Pro
Para hacer los scripts ejecutables:
```bash
chmod +x mapper.py reducer.py
# Ahora puedes usar:
cat mini_purchases.txt | ./mapper.py | sort | ./reducer.py
```

## 🌟 Ejecución en Hadoop

### 1️⃣ Subir datos a HDFS
```bash
hdfs dfs -put PURCHASES
```

### 2️⃣ Ejecutar MapReduce
```bash
mapred streaming -files mapper.py,reducer.py -input PURCHASES/purchases.txt -output COMPRASXTENDA -mapper mapper.py -reducer reducer.py
```

### 📋 Sintaxis Completa
```bash
$ mapred streaming
-files mapper.py,reducer.py
-input myInputDirs \
-output myOutputDir \
-mapper script_mapper
-reducer script_reducer
```

## 🌟 Ventajas de Hadoop
- 📦 Procesamiento de archivos grandes
- 🌐 Sistema de archivos distribuido
- 💪 Procesamiento paralelo en múltiples computadoras
- 🔄 Escalabilidad horizontal

## 📚 Recursos
- 📖 [Documentación de Hadoop Streaming](https://hadoop.apache.org/docs/stable/hadoop-streaming/HadoopStreaming.html)

## ⚠️ Notas Importantes
- Asegúrate de que todos los archivos estén en el directorio correcto
- Verifica las rutas antes de ejecutar los comandos
- Realiza pruebas locales antes de ejecutar en el clúster

---
💡 *Este ejercicio es parte del aprendizaje de procesamiento distribuido con Hadoop MapReduce*
