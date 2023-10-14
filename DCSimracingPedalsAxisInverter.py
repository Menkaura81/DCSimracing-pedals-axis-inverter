######################################################################################
# Script para invertir los ejes en los pedales DCSimracing.
#
# Los pedales disponen de un software de configuracion bastante completo, pero
# carece de la opcion de invertir los pedales. Es por esto que he creado este 
# script. Su principal utilidad es en juegos retro o emuladores que no permitan
# invertir los ejes ingame.
#
# Modo de uso:
# Copiar el ejecutable en la misma carpeta que el software de DCSimracing guarda las 
# distintas configuraciones, por defecto es la carpeta Documentos. Ejecutarlo, 
# seleccionar cual es el archivo de configuracion que quier modificar y elegir que ejes
# quiere invertir. El programa crea automaticamente una copia de seguridad del archivo
# de configuracion original. Una vez ejecutado, cargar el archivo de configuracion
# con el software oficial y enviar dicha configuracion a los pedales 
# 
# © 2023 Menkaura Soft
 ######################################################################################


import os
import sys


###########
# PRESETS
###########

ACELERADOR_NORMAL = "[THROTTLE]\ndz_0=4\ndz_1=95\nband_0=0\nband_10=10\nband_20=20\nband_30=30\nband_40=40\nband_50=50\nband_60=60\nband_70=70\nband_80=80\nband_90=90\nband_100=100\naxis_cnf=1\naxis_mode=0\n"
FRENO_NORMAL = "[BRAKE]dz_0=10\ndz_1=100\nband_0=0\nband_10=10\nband_20=20\nband_30=30\nband_40=40\nband_50=50\nband_60=60\nband_70=70\nband_80=80\nband_90=90\nband_100=100\naxis_cnf=1\naxis_mode=0\n"
EMBRAGUE_NORMAL = "[CLUTCH]\ndz_0=4\ndz_1=95\nband_0=0\nband_10=10\nband_20=20\nband_30=30\nband_40=40\nband_50=50\nband_60=60\nband_70=70\nband_80=80\nband_90=90\nband_100=100\naxis_cnf=1\naxis_mode=0\n"

ACELERADOR_INVERTIDO = "[THROTTLE]\ndz_0=4\ndz_1=95\nband_0=100\nband_10=90\nband_20=80\nband_30=70\nband_40=60\nband_50=50\nband_60=40\nband_70=30\nband_80=20\nband_90=10\nband_100=0\naxis_cnf=1\naxis_mode=0\n"
FRENO_INVERTIDO = "[BRAKE]dz_0=10\ndz_1=100\nband_0=100\nband_10=90\nband_20=80\nband_30=70\nband_40=60\nband_50=50\nband_60=40\nband_70=30\nband_80=20\nband_90=10\nband_100=0\naxis_cnf=1\naxis_mode=0\n"
EMBRAGUE_INVERTIDO = "[CLUTCH]\ndz_0=4\ndz_1=95\nband_0=100\nband_10=90\nband_20=80\nband_30=70\nband_40=60\nband_50=50\nband_60=40\nband_70=30\nband_80=20\nband_90=10\nband_100=0\naxis_cnf=1\naxis_mode=0\n"

configuracion= ""


#######################
# ENTRADA DE OPCIONES
#######################

archivoCorrecto = False
while (archivoCorrecto == False):
    archivo = input ("Introduce el nombre del archivo de configuracion: ")
    if (os.path.exists(archivo)):
        archivoCorrecto = True
    else:
        print("Nombre de archivo incorrecto.")


acelerador = ""
while (acelerador != "s" and acelerador != "n" and acelerador != "si" and acelerador != "no"):
    acelerador = input ("¿Desea invertir el eje del acelerador?(s/n): ")

freno = ""
while (freno != "s" and freno != "n" and freno != "si" and freno != "no"):    
    freno = input ("¿Desea invertir el eje del freno?(s/n): ")

embrague = ""
while (embrague != "s" and embrague != "n" and embrague != "si" and embrague != "no"): 
    embrague = input ("¿Desea invertir el eje del embrague?(s/n): ")


###############################
# CREACION COPIA DE SEGURIDAD
###############################

file = open(archivo, "r")
backup = file.read()
file.close

try:
    file = open("inverter_backup.txt", "x")
    file.write(backup)
    file.close
except: 
    print("Ya existe un archivo copia de seguridad en el directorio")
    exit = ""
    while exit != "s" and exit != "n" and exit != "si" and exit != "no":
        exit = input("¿Desea continuar sin realizar copia de seguridad?(s/n): ")
    if exit != "s" and exit != "si":
        sys.exit()
            

#############################
# CONFIGURACION DEL STRING
#############################

if acelerador == "s" or acelerador == "si":
    configuracion += ACELERADOR_INVERTIDO
else:
    configuracion += ACELERADOR_NORMAL

if freno == "s" or freno == "si":
    configuracion += FRENO_INVERTIDO
else:
    configuracion += FRENO_NORMAL

if embrague == "s" or freno == "si":
    configuracion += EMBRAGUE_INVERTIDO
else:
    configuracion += EMBRAGUE_NORMAL


#################################
# ESCRIBIR EN EL ARCHIVO ELEGIDO
#################################
file = open(archivo, mode="w")
file.write(configuracion)
file.close