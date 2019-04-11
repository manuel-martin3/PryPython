import mysql.connector
import datetime
#from tkinter import *


##############################################################################################################
###########################################  CONEXIÓN A BD  ##################################################
##############################################################################################################

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  db="midemo",
  port=3305
)

fecha = datetime.datetime.now()

##############################################################################################################
#############################################   CONSULTAS   ##################################################
##############################################################################################################

# consulta simple
def consultar():
    cursor=db.cursor()
    sql='SELECT * FROM usuario'
    cursor.execute(sql)
    resultado=cursor.fetchall()
    conta=1
    print(" ")
    print("############## LISTADO DE REGISTROS ###################")
    print("=======================================================")
    for reg in resultado:
	       print(reg[0], '|' ,reg[1] ,'|' ,reg[2] , '|' ,reg[3])
	       conta+=1
    print("registro afectados: " +str(conta))
    print("=====================================================")

# busqueda con parametros
def buscar(n):
    cursor=db.cursor()
    sql='SELECT * FROM usuario WHERE id ='+str(n)
    cursor.execute(sql)
    resultado=cursor.fetchall()
    conta = 1
    for reg in resultado:
	       print(reg[0], '|' ,reg[1] ,'|' ,reg[2] , '|' ,reg[3])
	       conta+=1
    print("registro afectados: " +str(conta))
    print("=====================================================")

def busca_r(n):
    cursor=db.cursor()
    sql='SELECT * FROM usuario WHERE ciudad like \'%'+n+'%\''
    cursor.execute(sql)
    resultado=cursor.fetchall()
    conta = 1
    for reg in resultado:
    	print(reg[0], '|' ,reg[1] ,'|' ,reg[2] , '|' ,reg[3])
    	conta+=1
    print("registro afectados: " +str(conta))
    print("=====================================================")

# busqueda auditoria
def auditar():
    cursor=db.cursor()

    sql='SELECT id, nombre, ciudad, pais,(CASE WHEN status = 0 THEN "Eliminado" WHEN status = 1 THEN "Modificado" ELSE "Creado" END)status,fcrea, fmod, fcontrol FROM usuario'
    cursor.execute(sql)
    resultado=cursor.fetchall()

    sql0="UPDATE usuario SET fcontrol = '"+str(fecha)+"' WHERE id != 0"
    cursor.execute(sql0)
    db.commit()
    
    sql1='SELECT id FROM usuario WHERE status = 0'
    cursor.execute(sql1)
    resultado1=cursor.fetchall()

    sql2='SELECT id FROM usuario WHERE status = 1'
    cursor.execute(sql2)
    resultado2=cursor.fetchall()

    sql3='SELECT id FROM usuario WHERE status is null'
    cursor.execute(sql3)
    resultado3=cursor.fetchall()
    
    conta = 0
    conta1 = 0
    conta2 = 0
    conta3 = 0
    
    print("############## REGISTROS AUDITADOS  ###################")
    print("=======================================================")
    for reg in resultado:
	       print(reg[0], '|' ,reg[1] ,'|' ,reg[2] , '|' ,reg[3], '|' ,reg[4] ,'|' ,reg[5] , '|' ,reg[6])
	       conta+=1

    for reg1 in resultado1:
        conta1+=1
        
    for reg2 in resultado2:
        conta2+=1

    for reg3 in resultado3:
        conta3+=1
	    
    print(" ")
    print(f"registros eliminados:... {conta1}")	       
    print(f"registros modificados:... {conta2}")
    print(f"registros creados:.... {conta3}")        
    print("registros leídos:... " +str(conta))
    print("=====================================================")


def busca_e(n):
    cursor=db.cursor()
    sql='SELECT * FROM usuario WHERE status = '+ str(n) 
    cursor.execute(sql)
    resultado=cursor.fetchall()
    conta = 1
    for reg in resultado:
    	print(reg[0], '|' ,reg[1] ,'|' ,reg[2] , '|' ,reg[3], '|' ,reg[4] ,'|' ,reg[5] , '|' ,reg[6])
    	conta+=1
    print("registro afectados: " +str(conta))
    print("=====================================================")

##############################################################################################################
###########################################   MANTENIMIENTO   ################################################
##############################################################################################################
    
def eliminar(n):
        cursor=db.cursor()
        
        sql='UPDATE FROM usuario SET status = 0, fmod = "'+ fecha +'", fcontrol = "'+ fecha +'"   WHERE id = ' + str(n)
        cursor.execute(sql)
        db.commit()
        print("registro alterados: " +str(1))

def agregar(pk, nom, ciu, pai):
        cursor=db.cursor()
        sql="INSERT INTO usuario (nombre,ciudad,pais,status,fcrea,fmod,fcontrol) VALUES("'+nom+'","'+ciu+'","'+pai+'", null, '"+str(fecha)+"', null, null)"
        cursor.execute(sql)
        db.commit()
        print("registro agregados: " +str(1))

def actualizar(pk, nom, ciu, pai):
        cursor=db.cursor()
        sql="UPDATE usuario SET nombre = '"+nom+"',ciudad = '"+ciu+"',pais =  '"+pai+"', status = 1, fmod = '"+str(fecha)+"'  WHERE id = " + str(pk)
        cursor.execute(sql)
        db.commit()
        print("registro actualizados: " +str(1))

def vaciar(n):
        cursor=db.cursor()
        sql='DELETE FROM usuario WHERE status = 0  and  id = ' + str(n)
        cursor.execute(sql)
        db.commit()
        print("registro eliminados: " +str(1))

def vaciar_t(n):
        cursor=db.cursor()
        sql='DELETE FROM usuario WHERE status = ' + str(n)
        cursor.execute(sql)
        db.commit()
        print("registro eliminados: " +str(1))

##############################################################################################################
##############################################   PANEL DE CONTROL   ##########################################
##############################################################################################################

def panelPrincipal(p):    
        if p == 2:
            v = input(" Ingrese [Id] para consultar... ")
            buscar(v)
        elif p == 3:
            v = input(" Ingrese [Ciudad] a consultar... ")            
            busca_r(str(v))
        elif p == 4:
            consultar()
            print("..:: Para eliminar debe ingresar ::... ")
            v = input(" [Id] ... ")            
            eliminar(v);
        elif p == 5:
            p1=0            
            p2 = input(" Ingrese [Nombre]... ")
            p3 = input(" Ingrese [Ciudad]... ")
            p4 = input(" Ingrese [País]... ")
            agregar(p1, p2.upper(), p3.upper(), p4.upper())
        elif p == 6:
            consultar()
            print("..:: Para modificar debe ingresar ::..")
            p1 = input(" [Id]... ")            
            p2 = input(" [Nombre]... ")            
            p3 = input(" [Ciudad]... ")            
            p4 = input(" [País]... ")
            actualizar(p1, p2.upper(), p3.upper(), p4.upper())
        elif p == 7:
            print(" ")            
            print(" .....:::::::::::::::::::::::::::::::... ")            
            auditar()            
        elif p == 8:
            busca_e(0)
            print("..:: Para vaciar debe ingresar ::... ")
            v = input(" [Id] ... ")            
            vaciar(v);
        elif p == 9:
            busca_e(0)
            print("..:: Vaciar todos los registros ::... ")
            v = input(" ¿Desea vaciar todo? S/N... ")
            if v.upper()=="S":
                vaciar(0)
            else:
                cPanel()
        else:
                consultar()

def cPanel():    
    opc={1:"1. Listar todo...",
         2:"2. Buscar por Id...",
         3:"3. Bucsar por Ciudad... ",
         4:"4. Eliminar un Registro...",
         5:"5. Agregar un Registro...",
         6:"6. Modificar un Registro...",
         7:"7. Auditar lista de Registro...",
         8:"8. Vaciar un Registro eliminado...",
         9:"9. Vaciar todos los Registro eliminados..."
         }

    print("¿Qúe desea hacer hoy?")
    
    i=1; x=9
    while i<=x:
        print(opc[i])
        i+=1  
    print(" ")
    p = input("<< Elija una opción [de 1 al "+str(x)+"] >>... " )    
    op = opc[int(p)]
    
    if int(p) != 1:
        print(f'Eligio: <<{op}>>')
        r = input('¿Desea confirmarlo?, S(Si)/N(No)... ')
        
        if ((r.upper()=='S') or (r.upper()is None)):
            panelPrincipal(int(p))
        else:
            cPanel()
    else:
        panelPrincipal(int(p))

    entradas()


def entradas():
    r = input('¿Desea ir a "cPanel()", presione: S(Si)/N(No)... ')    
    if r.upper()=='S':
       cPanel()
    else:
       principal()
       

def principal():
    print("#########################################################################")
    print("#####################       PANTALLA PRINCIPAL     ######################")
    print("#########################################################################")
    print("                                            ##")
    print("                            #             ######")
    print("           ####           ####       ### ##****##")
    print("        ###***##         ######     ######******##")
    print("       ##******##       #######     ######*******##")
    print("      ##********#      #####            ###******##")
    print("     #**********#      ###              ###*###***#")
    print("    #*****###***#     ##    #            #**# ##**#")
    print("   ##****## ##**#    ### ### #############*####***#")
    print("   #****#    #**# ###########  ####*#### #####**###")
    print("   #****#    #**###****## ###    #**# ##  ##*####")
    print("   #****#### #**#******#  ###    #*#####   #**###")
    print("   #********##********##  ##     #*# ###   ##***##")
    print("   ####*##************#          #*#  #    ##****##")
    print("     ######************#         #*#       ##****##")
    print("         ##************#         #*#       #******#")
    print("        ##*************##       #####     ##*****#")
    print("        #***************##     ##*#####   ##****##")
    print("        #****************#######***#XXX####****##")
    print("       #*******************###******#XXXXX######")
    print("       #****************************#XXXXXXXXX###")
    print("       #*****************************#XXXXXXXXXXX###")
    print("       ##**************#*******##****##XX############")
    print("        ##**************###*####*****######XXXXXXXX###           ####")
    print("         ###**************####******####XXXXXXXXXXX## #      ####")
    print("           ####*************##*****##   #XXXXXXXXXX#  ##  ####")
    print("             ####************#****#      ##XXXXXXX##   ####")
    print("                #####********##**#        ##XXXXX##    ##")
    print("                  #####*******#*##          #XXX##      #############")
    print("  #######################*****###  #         ####      ###  #")
    print("                       ##########  #   #     ###     ## #")
    print("                         #*****####          #         ##")
    print("                         ##***#              #         ########")
    print("                        #############       ##     #   #       ####")
    print("                 #######  ##**#      #      #         #            ##")
    print("          #######         ########          #        ##   ")
    print("      #####             ####**##           #        ##")
    print(" ####                ###   #***##         ###      ##")
    print("#                 ###      #***#####     ## ########")
    print("               ###         #***#  ########    ##")
    print("             ##          # #***##             #")
    print("           ##          #####****#            ##")
    print("          #           ##***##****#          ##")
    print("        ##           #******#****##        ##")
    print("       #               ***********##     ###   ")
    print("      #                         ** #######")
    print("                                       #")
    print("#########################################################################")
    print("######################  GRACIAS GRACIAS GRACIAS #########################")
    print("#########################################################################")
    entradas()



    

























    
    
