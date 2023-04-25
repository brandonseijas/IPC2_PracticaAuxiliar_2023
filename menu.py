from tkinter import *
from tkinter import filedialog
from xml.dom import minidom
import csv
from xml.etree.ElementTree import (
    Element, SubElement, Comment, tostring,
)
import datetime
import xml.etree.ElementTree as ET
from nodoempresa import nodoempresa
from Lista import Lista
Lista = Lista()

def menu():
    opc = 0
    pru=0
    po=0
    while opc != "10":
        print("     ---------------------------------------------------------------------------------------------")
        print("     |     Menú para el primer proyecto de ipc2 en el 2023                                        |")
        print("     |     1. Cargar información                                                                  |")
        print("     |     2. Calcular Margenes y Valor del inventario                                            |")
        print("     |     3. Mostrar el Top 10 dependiendo el valor a evaluar                                    |")
        print("     |     4. Acerca del creador                                                                  |")
        print("     |     5.Salida                                                                              |")
        print("     ---------------------------------------------------------------------------------------------")
        opc = input('Ingres opción: ')
        if opc == "5":
            print("Gracias por ingresar a la aplicación hasta la proxima")
        else:
            if opc == "1":
                print("Realizaremos la carga del archivo xml")
                raiz = Tk ()
                archivo = filedialog.askopenfilename(title = "abrir")
                #print(archivo)
                #Button(raiz,text="Abrir Archivo", command=abrirAchivo).pack()
                #raiz.mainloop()
                print(archivo)
                try:
                    xml_file = open(archivo)
                    if xml_file.readable():
                        xml_data = ET.fromstring(xml_file.read())
                        lst_ItemList = xml_data.findall('Item')
                        for ItemList in lst_ItemList:
                            nodomuestranuevo = nodoempresa()
                            nodomuestranuevo.ItemCode = ItemList.find('ItemCode').text
                            nodomuestranuevo.QuantityOnHand = ItemList.find('QuantityOnHand').text
                            nodomuestranuevo.PriceLevel1 = ItemList.find('PriceLevel1').text
                            nodomuestranuevo.PriceLevel2 = ItemList.find('PriceLevel2').text
                            nodomuestranuevo.PriceLevel3 = ItemList.find('PriceLevel3').text
                            nodomuestranuevo.LastTotalUnitCost = ItemList.find('LastTotalUnitCost').text
                            Lista.agregarNodo(nodomuestranuevo)
                        print("=====================================================")
                        Lista.mostrardato()
                        print("=====================================================")
                        pru = 1
                    else:
                        print(False)
                except Exception as err:
                    print("Error:", err)
                #finally:
                    #xml_file.close()
            if opc == "2":
                if pru == 1:
                    print("Se realizara los calculos necesarios")
                    Lista.realizarCal()
                    po = 1
            if opc == "3":
                if po == 1:
                    print("Dado las siguientes opciones:")
                    print("    ->MarginLevel1: ")
                    print("    ->MarginLevel2: ")
                    print("    ->MarginLevel3: ")
                    print("    ->ValorInventario: ")
                    print("-------------------------------")
                    respuestaf = input("Ingrese que valor se utilizara como parametro para que se ordene la lista\n y muestre el Top 10")
                    Lista.ordenar(respuestaf)
            if opc == "4":
                print("-----------------------------------------------------------")
                print("| Nombre: Brandon Orlando Seijas Morales                   |")
                print("| Carnet: 202010035                                        |")
                print("| Curso: Introducción a la programación y computación 2    |")
                print("-----------------------------------------------------------")