import numpy as np
import time
def crearPieza(x,y,pieza,num_rows,num_cols,i):
    num_rowsP, num_colsP = pieza.shape
    print(num_cols,num_rows)
    p = np.zeros((num_cols,num_rows))
    p[x:x+num_rowsP,y:y+num_colsP]= pieza*(i+1)
    return p
    
    

def encajar(matA,matB):
    return matA + matB
    

def la_pieza_Encaja(sumaplantilla,i):
    for x in sumaplantilla:
        for y in x:
            if y > i+1:
                return False
    return True

iteracion = 0
def probarPiezarec(x,y,piezas,plantilla,i):
    #
    time.sleep(1)
    global iteracion 
    iteracion +=1
    
    num_rows, num_cols = plantilla.shape
    num_rowsP, num_colsP = piezas[i].shape
    
    piezaM = crearPieza(x,y,piezas[i],num_cols,num_rows,i)
    
    sumaplantilla = piezaM+plantilla    

    print(sumaplantilla)
   
    if la_pieza_Encaja(sumaplantilla,i):
        #print(sumaplantilla)
        if i < len(piezas)-1:
            if probarPiezarec(0,0,piezas,sumaplantilla,i+1):            
            #return probarPiezarec(0,0,piezas,sumaplantilla,i+1)
        #else:
                return True
            else:
                #print('x=',num_rows , num_rowsP,i)
                if y<num_cols-num_colsP:
                    return probarPiezarec(x,y+1,piezas,plantilla,i)
                #print('y=',num_cols,num_colsP,i)
                if x<num_rows-num_rowsP:        
                    return probarPiezarec(x+1,0,piezas,plantilla,i)
        else:
            return True   
    else:
        #print('x=',num_rows , num_rowsP,i)
        if y<num_cols-num_colsP:
            return probarPiezarec(x,y+1,piezas,plantilla,i)
        #print('y=',num_cols,num_colsP,i)
        if x<num_rows-num_rowsP:        
            return probarPiezarec(x+1,0,piezas,plantilla,i)
        
    return False

plantilla = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0]])

pieza = np.array([[0,1],[1,1]])
pieza2 = np.array([[1],[1]])
pieza3 = np.array([[1,1,1]])
pieza4 = np.array([[1]])
pieza5 = np.array([[1,0],[1,0]])  
#piezax = np.array([[1],[1]])
#piezay = np.array([[1,1],[1,0]])
#piezaz = np.array([[0,0,1],[1,1,1]])                 
piezax=np.array([[1,1],[1,0]])
piezay=np.array([[0,1],[1,1]])
piezaz=np.array([[1],[1],[1]])


#piezas = np.array([pieza,pieza3])
#piezas = [pieza,pieza2,pieza3,pieza4]
#piezas = [piezax,piezay,piezaz]
piezas = [piezaz,piezax,piezay,pieza3]
#probarPieza(0,0,pieza,plantilla)
probarPiezarec(0,0,piezas,plantilla,0)
#piezas.shape[0]
print("Cantidad de iteraciones: ", iteracion)