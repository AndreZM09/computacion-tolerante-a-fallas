# Monitor de Estado de Aplicación con Python

Este script Python utiliza módulos `threading` y `queue` para implementar un monitor de estado que muestra el progreso de varias tareas en tiempo real.

## Descripción

El script se compone de varias partes:

- **Cola de Estado**: Una cola que facilita la comunicación entre los diferentes hilos, permitiéndoles enviar y recibir mensajes sobre el estado actual de la aplicación.
- **Monitor de Estado**: Un hilo que supervisa constantemente la cola de estado para obtener y mostrar el estado más reciente de la aplicación.
- **Tareas (1, 2 y 3)**: Tres hilos separados que representan tareas individuales de una aplicación. Cada tarea reporta su progreso al monitor de estado mediante mensajes enviados a través de la cola de estado.

## Funciones

### `monitor_de_estado()`

Un hilo que supervisa la cola de estado, extrayendo y mostrando cualquier nuevo mensaje de estado que se haya agregado a la cola. Si no recibe un nuevo mensaje dentro de un período de tiempo específico (3 segundos en este caso), asume que la aplicación ha terminado y se detiene.

### `tarea_1()`, `tarea_2()`, `tarea_3()`

Estas funciones representan tareas individuales en la aplicación. Cada una ejecuta una serie de "pasos", reportando su progreso al monitor de estado después de cada paso. Una vez que una tarea ha completado todos sus pasos, envía un mensaje final indicando que ha terminado.

## Uso

1. Asegúrate de tener Python instalado en tu sistema.
2. Ejecuta el script con un intérprete Python.
3. Observa la salida en la consola para ver los mensajes de estado en tiempo real de cada tarea y del monitor de estado.

## Notas

- Los hilos de tarea simulan el paso del tiempo utilizando la función `time.sleep()` para crear un retardo entre cada paso.
- La cantidad de pasos y el tiempo de retardo pueden ajustarse según sea necesario para cada tarea.

## Conclusión

Este script demuestra cómo implementar un sistema de monitoreo de estado simple utilizando Python. A través del uso de `threading` y `queue`, permite una comunicación fluida entre varios hilos y un monitoreo continuo del estado de la aplicación.
