# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 21:14:59 2020

@author: user
"""

#Importamos cada una de las variables del archivo 
from lifestore_file import lifestore_searches, lifestore_sales, lifestore_products

#print(lifestore_products) #Se comprueba que imprime la variable correctamente



usuarios_admin=[["Patricia","123"],["Alejandra","hola"],["Daniel","perro"],["Mai","gato"]]

es_admin=0

while es_admin==0:
    usuario_entrada=input("Ingresa tu nombre de usuario: ")
    usuario_clave=input("Ingresa tu clave de acceso: ")

    for usuario in usuarios_admin:
        if usuario[0]==usuario_entrada and usuario[1]==usuario_clave:
            es_admin=1
        else:
            continue
    
if es_admin==1:
    print("Bienvenido a Lifestore")
    
    print("Elige una opcion del menu: \n 1.Conocer los 50 productos con mayores y menores ventas:  a \n 2.Productos con mejores y peores resenas: b \n 3.Productos mas y menos buscados: c")
    opcion_seleccionada=input("Opcion: ")
    op_correcta=0
    
    while op_correcta==0:
        if opcion_seleccionada=="a":
            print("Seleccionaste a")
            opcion=1
            op_correcta=1
            
            contador=0
            total_ventas=[] #[[id,contador],[id2, contador2]]
            
            for producto in lifestore_products:
                for venta in lifestore_sales:
                    if producto[0]==venta[1]:
                        contador+=1
                
                formato=[producto[0], producto[1], contador]
                #formato=[producto[0],contador]
                total_ventas.append(formato)
                contador=0
           
           
            ventas_ordenada=[]
              
            while total_ventas:
                minimo=total_ventas[0][2]
                lista_actual=total_ventas[0]
                for venta in total_ventas:
                    if venta[2]<minimo:
                        minimo=venta[2]
                        lista_actual=venta
                ventas_ordenada.append(lista_actual)
                total_ventas.remove(lista_actual)
            
            tam=len(ventas_ordenada)
            print("\n \nPRODUCTOS MAS VENDIDOS")
            for idx in list((reversed(range(tam-50,tam)))):
                print("\nNombre: \n", ventas_ordenada[idx][0],ventas_ordenada[idx][1],ventas_ordenada[idx][2],"\n")   
               
            #print(ventas_ordenada)
            print("PRODUCTOS MENOS VENDIDOS")
            for idx in range(0,50):    
                print("\nNombre: \n", ventas_ordenada[idx][1],ventas_ordenada[idx][2])  
            

            
        elif opcion_seleccionada=="b":
            print("Seleccionaste b'")
            op_correcta=1
            
            promedio=0
            suma=0
            numero=0
            index=0
            formato=[]
            total_resenas=[]
            #total_resenas1=[]
            
            for objeto in lifestore_products:
                while lifestore_sales:
                    if index<len(lifestore_sales):
                        primero=lifestore_sales[index][1]
                        for producto in lifestore_sales:
                            if producto[1]==primero:                
                                numero+=1
                                suma=suma+producto[2]                  
                                promedio=suma/numero                          
                                index+=1
                    else:
                        break
                                
                    formato=[objeto[1],primero,promedio]
                    total_resenas.append(formato)
                    promedio=0
                    suma=0
                    numero=0        
            
            
            #print(total_resenas)     
            
            
            
            ###############################################################################
            
            resenas_ordenada=[]
              
            while total_resenas:
                minimo=total_resenas[0][1]
                lista_actual=total_resenas[0]
                for resena in total_resenas:
                    if resena[1]<minimo:
                        minimo=resena[1]
                        lista_actual=resena
                resenas_ordenada.append(lista_actual)
                total_resenas.remove(lista_actual)
                

            
            tam=len(resenas_ordenada)
            print("\n \nPRODUCTOS MEJORES RESENAS")
            for idx in list((reversed(range(tam-20,tam)))):
                print("\nNombre: \n", resenas_ordenada[idx][0],resenas_ordenada[idx][1],"\n") 
                
            print("\n \nPRODUCTOS PEORES RESENAS")
            for idx in range(0,20):    
                print("\nNombre: \n", resenas_ordenada[idx][0],resenas_ordenada[idx][1],"\n")   
                        
            
        elif opcion_seleccionada=="c":
            print("Seleccionaste c'")
            op_correcta=1   
            
            
            contador=0
            total_busquedas=[] #[[id,contador],[id2, contador2]]
            
            for producto in lifestore_products:
                for busqueda in lifestore_searches:
                    if producto[0]==busqueda[1]:
                        contador+=1
                
                formato=[producto[0], producto[1], contador]
                #formato=[producto[0],contador]
                total_busquedas.append(formato)
                contador=0
            print(total_busquedas)
             

            
            busquedas_ordenada=[]
              
            while total_busquedas:
                minimo=total_busquedas[0][2]
                lista_actual=total_busquedas[0]
                for busqueda in total_busquedas:
                    if busqueda[2]<minimo:
                        minimo=busqueda[2]
                        lista_actual=busqueda
                busquedas_ordenada.append(lista_actual)
                total_busquedas.remove(lista_actual)
            
            tam=len(busquedas_ordenada)
            print("PRODUCTOS MAS BUSCADOS")
            for idx in list((reversed(range(tam-10,tam)))):
                print("\nNombre: \n", busquedas_ordenada[idx][0],busquedas_ordenada[idx][2])   
                
            #print(ventas_ordenada)
            print("PRODUCTOS MENOS BUSCADOS")
            for idx in range(0,10):    
                print("\nNombre: \n", busquedas_ordenada[idx][0],busquedas_ordenada[idx][2])   
                        
                        
            
            
            
        else:
            print("Opcion incorrecta.")
            opcion_seleccionada=input("Intenta otra vez: ")
    
else:
    print("No existe")

# if opcion==1:
#     print("Hola mundo")