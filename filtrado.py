import os

# Nombre de la carpeta con los archivos .txt (en el mismo directorio que el script)
carpeta_txt = "data"
# Nombre del archivo de salida (en el mismo directorio que el script)
archivo_salida = "uno.txt"

def contar_registros_y_guardar(palabra_clave):
    total_registros = 0
    lineas_encontradas = []

    # Verificar si la carpeta existepu
    if not os.path.exists(carpeta_txt):
        print(f"Error: La carpeta '{carpeta_txt}' no existe en el directorio actual.")
        return 0

    for archivo in os.listdir(carpeta_txt):
        if archivo.endswith('.txt'):
            ruta_archivo = os.path.join(carpeta_txt, archivo)

            try:
                with open(ruta_archivo, 'r', encoding='utf-8') as f:
                    for linea in f:
                        if palabra_clave in linea:
                            linea_limpia = linea.strip()
                            print(linea_limpia)  # Mostrar en consola
                            lineas_encontradas.append(linea_limpia)
                            total_registros += 1
            except UnicodeDecodeError:
                try:
                    with open(ruta_archivo, 'r', encoding='ISO-8859-1') as f:
                        for linea in f:
                            if palabra_clave in linea:
                                linea_limpia = linea.strip()
                                print(linea_limpia)  # Mostrar en consola
                                lineas_encontradas.append(linea_limpia)
                                total_registros += 1
                except Exception as e:
                    print(f"Error al leer {ruta_archivo}: {e}")

    # Guardar resultados
    with open(archivo_salida, 'w', encoding='utf-8') as f_salida:
        for linea in lineas_encontradas:
            f_salida.write(linea + '\n')

    return total_registros

# Entrada del usuario
palabra_clave = input("Introduce la palabra clave a buscar: ")
registros_encontrados = contar_registros_y_guardar(palabra_clave)

print(f"\nSe encontraron {registros_encontrados} registros con la palabra clave '{palabra_clave}'.")
print(f"Las líneas encontradas se han guardado en '{archivo_salida}' en el directorio actual.")
