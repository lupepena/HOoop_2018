import random as r


class Fila(object):
    """Clase base de fila"""

    def __init__(self):
        """constructor de la clase Fila """
        self.enfila= 0
        self.fila = []#la fila es una lista
##################
class FilaPreferencial(Fila):
    """Clase de la fila de los clientes preferenciales"""        

    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila preferencial"""
        self.fila.append(cliente)#a fila le agrego los clientes, los clientes son los elementos de la fila
        self.enfila+=1 #cada vez que inserta le suma uno y cuento los clientes en una fila

    def atender(self):
        """Atiende al proximo cliente preferencial"""
        if (self.enfila > 0):#Si no entra nadie que no cuente
            self.enfila-=1
            self.fila.pop(0)
        
    def abrircajanueva(self,filanueva,maxenfila=20):
        """Si maxenfila es menor que la cantidad de clientes actualmente en espera, abro nueva caja"""
        if maxenfila < self.enfila:
            #filanueva=FilaPreferencial()
            self.enfila-=1

            #filanueva.insertar(self.fila.pop(0))
            filanueva.fila.append(self.fila.pop(0))#Inserto el cliente que saque a la filanueva
            filanueva.enfila+=1   
    
#######################   
class FilaGeneral(Fila):
    """Clase que mantiene una fila de clientes no preferenciales"""

    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila no preferencial"""
        self.fila.append(cliente)#a fila le agrego los clientes, los clientes son los elementos de la fila
        self.enfila+=1 #cada vez que inserta le suma uno y cuento los clientes en una fila

    def atender(self):
        """Atiende al proximo cliente general"""
        if (self.enfila > 0):#Si no entra nadie que no cuente
            self.enfila-=1#al atender un cliente lo resta a la cantidad de clientes
            self.fila.pop(0)#saca el objeto cliente de la fila(lista)   
    
#######################
class cliente(object):
    """clase cliente """
    def __init__(self,dni):
        """ constructor de la clase cliente """
        self.dni=dni
        self.categoria=None
    def modificarcategoria(self, categoria):
        """modifica el atributo categoria del cliente """
        self.categoria=categoria
  
#############################MAIN#########################################
    
if __name__ == "__main__":
    """ simular una fila en una entidad bancaria"""
    

    #Filas que voy a necesitar 3

    fp1=FilaPreferencial()
    fp2=FilaPreferencial()
    fg=FilaGeneral()


    #Creo Clientes
    #Se los adjudico a las filas segun su categoria
    #Atender personas cada un rango de tiempo
    cantidadpersonas=0

    for t in range(1,300):

        personanueva=r.randint(0,3)#gente que llega al banco
        cantidadpersonas= cantidadpersonas + personanueva

        for i in range(0,personanueva):

            
            dni=r.randint(1000,9000)
            persona=cliente(dni)

            #Quiero adjudicarle una categoria (general o preferencial)
            n=r.randint(0,2)#Me elige aleatoriamente un numero entre 0 y 1
            
            if (n==0):
                persona.modificarcategoria('General')
                fg.insertar(persona)
            else:
                persona.modificarcategoria('Preferencial')
                fp1.insertar(persona) 
                fp1.abrircajanueva(fp2)        


        #Le digo que atienda gente cada 2 o 3 pasos
        if (t%2==0):
        
            fp1.atender()
            fp2.atender()

        if (t%3==0):

            fg.atender()

    print('total', 'General','preferencial1','preferencial2')         
    print(cantidadpersonas,fg.enfila,fp1.enfila,fp2.enfila)
        #print(fg.fila,fp1.fila)   


        

            

        

















