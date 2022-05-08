# Listas por comprensión 

### **¿Qué son?**

Las listas por comprensión son una construcción sintáctica disponible en Python con la que se pueden crear listas a partir de otros elementos iterables. Siendo una de las contracciones más elegantes del lenguaje. Su funcionalidad es crear listas avanzadas en una misma línea de código.

La forma general de la definición de una lista por comprensión es:\

[**expresion** for **item** in **iterable**]

Opcionalmente, se puede incluir un condicional en la expresión:\

[**expresion** for **item** in **iterable** if **condicion**]

expresion puede ser cualquier expresión computable en Python, generalmente involucrando un item del iterable llamado iterable puede ser cualquier objeto iterable, como una secuencia (lista o cadena de caracteres), la función la función range(), etc. La salida siempre es un tipo de lista Python.
En el caso de que se desee realizar una operación diferente cuando no se cumple la condición se puede hacer con un else. Aunque es necesario cambiar modificar el orden. Si se utiliza un else la condición se tiene que situar justamente después de la expresión y antes del for.


### **¿Cuáles son los beneficios?**

Uno de los principales beneficios de usar listas por comprensión en Python es que se puede usar en muchas situaciones diferentes. Además de la creación de listas estándar, las listas por comprensión también se pueden utilizar para mapeo y filtrado. No es necesario utilizar diferentes métodos para cada situación.

Las listas por comprensión también son más declarativas que los bucles, lo que significa que son más fáciles de leer y comprender. Los ciclos requieren concentración en la creación de listas. Debe crear manualmente una lista vacía, repetir y agregar a los elementos.

Las listas por comprensión son más rápidas en la mayoría de los casos y puede reemplazar bucles en casi el 80% de los casos. Pero no siempre podemos reemplazar los bucles, hay algunos casos en los que tenemos un buen número de condiciones y las clases están anidadas en un bucle. En estos casos, usar listas por compresión podría ser bastante engorroso y puede hacer que nuestro código se ejecute más lento o consuma más memoria. Es mejor ir a bucles en tales situaciones. 
Las comprensiones de listas son fáciles de entender y hacen que el código sea elegante, ya que podemos escribir el programa con expresiones simples.


### **¿Cuáles son las diferencias con NumPy? ¿Y por qué se ejecutan más rápido?**

Las matrices NumPy se ejecutan mucho más rápido que las listas en Python. Existe una gran diferencia entre el tiempo de ejecución de matrices y listas.
Las matrices NumPy son más rápidas que las listas de Python por las siguientes razones: 
 
- Una matriz es una colección de tipos de datos homogéneos que se almacenan en ubicaciones de memoria contiguas. Por otro lado, una lista en Python es una colección de tipos de datos heterogéneos almacenados en ubicaciones de memoria no contiguas.
- El paquete NumPy divide una tarea en varios fragmentos y luego procesa todos los fragmentos en paralelo.
- El paquete NumPy integra códigos C, C ++ y Fortran en Python. Estos lenguajes de programación tienen muy poco tiempo de ejecución en comparación con Python.
