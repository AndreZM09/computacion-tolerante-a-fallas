import threading
import time
import queue

# Crear una cola para compartir el estado entre los hilos
cola_de_estado = queue.Queue()

def monitor_de_estado():
    """Monitorea y muestra el estado de la aplicación."""
    while True:
        try:
            # Obtén el estado más reciente de la cola (espera hasta que haya un elemento disponible)
            estado = cola_de_estado.get(timeout=3)
        except queue.Empty:
            # Si no hay ningún mensaje en 3 segundos, asume que la aplicación ha terminado
            print("Estado: La aplicación ha terminado.")
            break

        print(f"Estado: {estado}")

def tarea_1():
    for i in range(5):
        cola_de_estado.put(f"Tarea 1 está trabajando, paso {i+1} de 5")
        time.sleep(1)
    cola_de_estado.put("Tarea 1 completada")

def tarea_2():
    for i in range(3):
        cola_de_estado.put(f"Tarea 2 está trabajando, paso {i+1} de 3")
        time.sleep(2)
    cola_de_estado.put("Tarea 2 completada")

def tarea_3():
    for i in range(4):
        cola_de_estado.put(f"Tarea 3 está trabajando, paso {i+1} de 4")
        time.sleep(1.5)
    cola_de_estado.put("Tarea 3 completada")

# Crear e iniciar un hilo para el monitor de estado
monitor = threading.Thread(target=monitor_de_estado, daemon=True)
monitor.start()

# Crear e iniciar hilos para cada tarea
t1 = threading.Thread(target=tarea_1)
t2 = threading.Thread(target=tarea_2)
t3 = threading.Thread(target=tarea_3)

t1.start()
t2.start()
t3.start()

# Espera a que todas las tareas terminen
t1.join()
t2.join()
t3.join()

# Espera unos segundos adicionales para asegurar que el monitor de estado pueda procesar cualquier mensaje restante
time.sleep(4)
