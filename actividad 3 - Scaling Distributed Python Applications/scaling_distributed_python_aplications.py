import concurrent.futures
from multiprocessing import Process
import threading
import time
import matplotlib.pyplot as plt
import numpy as np

def daemon_thread_function():
    while True:
        print("Daemon Thread: La hora actual es:", time.ctime())
        time.sleep(2)

def normal_thread_function():
    print("Normal Thread: Generando gráfico de una función sinusoidal...")
    x = [i * 0.1 for i in range(100)]
    y = [np.sin(i) for i in x]
    plt.plot(x, y)
    plt.title('Función Sinusoidal')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.show()

def separate_process_function():
    print("Process: Creando un archivo y escribiendo datos en él...")
    with open('proceso_archivo.txt', 'w') as f:
        for i in range(5):
            f.write(f"Línea {i}\n")
    print("Process: Archivo creado y datos escritos exitosamente.")

def concurrent_function():
    print("Concurrent: Ejecutando varias tareas de forma concurrente...")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(task, i) for i in range(5)]
        for future in concurrent.futures.as_completed(futures):
            print(f"Concurrent: Tarea {future.result()} completada.")

def task(n):
    time.sleep(n)
    return n

def main():
    while True:
        print("""
        Por favor elige una opción:
        1. Daemon Thread
        2. Normal Thread
        3. Separate Process
        4. Concurrent Execution
        5. Salir
        """)
        
        choice = input("Tu elección: ")
        
        if choice == "1":
            daemon_thread = threading.Thread(target=daemon_thread_function, daemon=True)
            daemon_thread.start()
            time.sleep(10)  # Dejamos que el daemon thread se ejecute por un tiempo antes de volver al menú
            break
        elif choice == "2":
            normal_thread = threading.Thread(target=normal_thread_function)
            normal_thread.start()
            normal_thread.join()  # Esperamos a que el hilo normal termine antes de volver al menú
        elif choice == "3":
            separate_process = Process(target=separate_process_function)
            separate_process.start()
            separate_process.join()  # Esperamos a que el proceso separado termine antes de volver al menú
        elif choice == "4":
            concurrent_function()  # Ejecutamos la función concurrente y esperamos a que termine antes de volver al menú
        elif choice == "5":
            break  # Salimos del loop y terminamos el programa
        else:
            print("Opción no válida. Por favor intenta de nuevo.")

if __name__ == '__main__':
    main()
