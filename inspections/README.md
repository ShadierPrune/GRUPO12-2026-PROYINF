En este documento se explica que se añadió para ejecutar el sonar. Primero que nada se añadio el archivo *sonar-project.properties*, el cual muestra los datos necesarios para realizar la evaluación, en este caso se ejecutó el de "JS/TS & Web" pues fue aquello con lo que trabajamos.

Para probar el sonar lo que se hace es tener corriendo StartSonar en la carpeta en la que se haya descargado, en nuestro caso se utilizó el SonarQubeCommunity (la versión gratis y que no necesita iniciar sesión), se tiene que ir a la carpeta en la que se tiene descargado, ir a "bin", luego ir avanzando con cd hasta que se ingrese a la versión correspondiente a nuestro sistema opertaivo y despues ejecutar en la terminal cmd:

    StartSonar.bat

Luego esperar que esto se ejecute hasta que quede tintilando la barra donde se escribe. Despues de esto dejar la terminal abierta y no escribir nada.

Finalmente, se va la carpeta donde se tiene el proyecto y se ejecuta:

    sonar

Así solito porque en sonar-project.properties están los datos necesarios para su ejecución. Despues en la terminal tendrá un link de localhost:9000 donde se podrán ver los resultados de la evaluación.

## Análisis

En la carpeta de este readme se añadieron los estados generales despues de la primera evaluación y despues de haber realizado esos cambios. Se vió como disminuyeron los errores o issues de seguridad pero como aumentaron todos los demás, esto probablemente se deba a que se detectaron nuevos errores y que los de la "primera pasada" eran los más relevantes. Pues muchos errores son bajos de mantenibilidad y los altos son del tipo cambiar "var" por "let" o "const".

Entonces dice Quality Gate Failed porque no se solucionaron todos los errores antes de ejecutar la evaluación otra vez, pues para poder aprobarla se necesitaria solucionar todos los errores que tenemos y no solo algunos, pero para este hito se solucionarlon los de mayor importancia primero.

Se adjuntarán imágenes en esta carpeta para ayudar a entender el estado actual precambio y postcambio.