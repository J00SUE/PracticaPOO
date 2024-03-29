class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 

class Canino: #canino y felino heredan de Mascota
    def __init__(self,canino): #agregamos la clase canino 
        self._canino = canino

class Felino:
    def __init__(self,felino): #agregamos la clase felino
        self._felino = felino 
        
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso= 0 #cambiamos a numero porque sera un int
        self.__lista_medicamentos=[]
        
    #getters
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
    
    #setters
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
class sistemaV: #sistemaV hereda la informacion de la mascota
    def __init__(self):
        self.__lista_mascotas = [] #corregimos bibliotecas para que se guarden en sistemaV
        self.__biblio_F = {}  #añadimos las bibliotecas 
        self.__biblio_C = {}

    #setters
        
    def asignarcanino(self, n, historia):
        self.__biblio_C[historia] = n 

    def asignarfelino(self, n, historia):
        self.__biblio_F[historia] = n 

    
    def verificarExiste(self,historia):
        for m in self.__lista_mascotas:
            if historia == m.verHistoria():
                return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False
        
    def verNumeroMascotas(self):
        return len(self.__lista_mascotas) 
    
    def ingresarMascota(self,mascota):
        self.__lista_mascotas.append(mascota) 
   
   #getter

    def verFechaIngreso(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verFecha() 
        return None

    def verMedicamento(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verLista_Medicamentos() 
        return None
    
    #delete
    
    def eliminarMascota(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                self.__lista_mascotas.remove(masc)  #opcion con el pop
                return True  #eliminado con exito
        return False      


def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Salir 
                       \nUsted ingresó la opción: ''' ))
        if menu==1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            historia=int(input("Ingrese la historia clínica de la mascota: "))
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre=input("Ingrese el nombre de la mascota: ")
                tipo=input("Ingrese el tipo de mascota (felino o canino): ")         
                peso=int(input("Ingrese el peso de la mascota: "))
                import datetime #importamos datetime para usar su funcion

                fecha = datetime.datetime.now() #la fecha se agregara automaticamente con datetime
                #fecha=input("Ingrese la fecha de ingreso (dia/mes/año): ")
                nm=int(input("Ingrese cantidad de medicamentos: "))
                lista_med=[]

                LM = [] #agregamos una lista para verificar medicamentos en una sola mascota
                for i in range(0,nm):
                    nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                    medicamento = Medicamento()
                    A = True #variable bandera
                    for m in LM: #buscamos en la lista
                        if m == nombre_medicamentos:
                            nm = nm + 1
                            print("Ya esta registrado")
                            A = False
                            break

                    if A == True:
                        dosis =int(input("Ingrese la dosis: "))
                        medicamento.asignarNombre(nombre_medicamentos)
                        medicamento.asignarDosis(dosis)
                        lista_med.append(medicamento)
                        LM.append(nombre_medicamentos) #agregamos a nuestra lista el medicamento
                        A = True
                        continue
                    elif A == False:
                        continue

                mas= Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)
                if tipo == "felino":
                    mas = Mascota()
                    felino = {}
                    felino[historia] = mas
                    servicio_hospitalario.asignarfelino(mas,historia) #agregamos a la biblioteca felino
                    
                
                elif tipo == "canino":
                    mas = Mascota()
                    canino = {}
                    canino[historia] = mas
                    servicio_hospitalario.asignarcanino(mas, historia)    #biblioteca canino

            else:
                print("Ya existe la mascota con el numero de histoira clinica")

        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha_1 = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha_1 != None:
                print(fecha_1)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")
            
        elif menu==6:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()





            

                

