from boardgame import BoardGame, console_play
from boardgame_g2d import BoardGameGui
from random import randrange
import g2d

class Scacchiera(BoardGame):

    def __init__(self,dim: int):
        self._cols, self._rows = dim, dim
        self._dim=dim
        self._board=[[0 for x in range(0,dim)] for y in range (0,dim)]
        self._mossedisponibili=True
        self._x=0
        self._y=0
        self._count=0
        self._listamosse=[0,0,0,0,0,0,0,0]
        self._fine=False

    def cols(self) -> int:
        return self._cols

    def rows(self) -> int:
        return self._rows

    def finished(self) -> bool:
        if(self._fine==True):
            return True
        else:
            return False
        
    def flag_at(self,x:int,y:int):
        self._mossedisponibili=False
        for j in range (0,len(self._listamosse)):
            if(self._listamosse[j]!=1):
                self._mossedisponibili=True
        if(self._mossedisponibili==True):
            if(self._count!=0):
                try:
                    h=self._listamosse.index([x,y]) #Varibile tmp per gestire l'eccezione
                except ValueError:
                        warnsdorf=self.warnsdorfsrule()
                        if(warnsdorf!=8):
                            x=self._listamosse[warnsdorf][0]
                            y=self._listamosse[warnsdorf][1]
                            self._x=x
                            self._y=y
                            self._count=self._count+1 
                            self._listamosse=self.calmosse(x,y)
                            self._board[x][y]=self._count
            else:
                self._count=self._count+1 
                self._listamosse=self.calmosse(x,y)
                self._board[x][y]=self._count
                self._x=x
                self._y=y
        if(self._count==self._dim*self._dim):
            self._fine=True
        
    def warnsdorfsrule(self):
        tmp=8 #Variabile d'appoggio per determinare la mossa con meno combinazioni possibili
        indice=8 #indice lista mosse
        for i in range(0,len(self._listamosse)):
            count1=0
            listam=self._listamosse[i]
            if(listam!=1):
                x1=listam[0]
                y1=listam[1]
                listam=self.calmosse1(x1,y1)
                for j in range(0,len(listam)):
                    try:
                        h=listam[j][0]#variabile per gestire l'eccezione
                    except:
                        count1=count1+1
                count1=8-count1
                if(self._board[x1][y1]==0):
                    if(count1<=tmp):
                        tmp=count1
                        indice=i
        return indice
            

    def setmatrice(self,val: int):
        for x in range(0,self._dim):
            for y in range (0,self._dim):
                if(self._board[x][y]>val):
                    self._board[x][y]=0

    def get_val(self, x: int, y: int) -> str:
        if (0 <= x < self._cols and 0 <= y < self._rows and
            self._board[y][x]):
            return str(self._board[y][x])
        return "0"

    def get_mossedis(self):
        return self._mossedisponibili

    def calmosse(self,x:int, y:int):
        lista=[]
        if(x-2>=0 and y-1>=0 and x-2<self._dim and y-1<self._dim): #controllo su x e y in modo da non considerare indici negativi
            lista.append([x-2,y-1]) # 0 indica posizione disponibile, quindi inserisco le coordiante
        else:
            lista.append(1) # 1 indica posizione non disponibile
        if(x-2>=0 and y+1>=0 and x-2<self._dim and y+1<self._dim):
            lista.append([x-2,y+1])
        else:
            lista.append(1)
        if(x-1>=0 and y-2>=0 and x-1<self._dim and y-2<self._dim):
            lista.append([x-1,y-2])
        else:
            lista.append(1)
        if(x-1>=0 and y+2>=0 and x-1<self._dim and y+2<self._dim):
            lista.append([x-1,y+2])
        else:
            lista.append(1)
        if(x+1>=0 and y-2>=0 and x+1<self._dim and y-2<self._dim):
            lista.append([x+1,y-2])
        else:
            lista.append(1)
        if(x+1>=0 and y+2>=0 and x+1<self._dim and y+2<self._dim):
            lista.append([x+1,y+2])
        else:
            lista.append(1)
        if(x+2>=0 and y-1>=0 and x+2<self._dim and y-1<self._dim):
            lista.append([x+2,y-1])
        else:
            lista.append(1)
        if(x+2>=0 and y+1>=0 and x+2<self._dim and y+1<self._dim):
            lista.append([x+2,y+1])
        else:
            lista.append(1)
        return lista

    def calmosse1(self,x:int, y:int):
        lista=[]
        if(x-2>=0 and y-1>=0 and x-2<self._dim and y-1<self._dim and self._board[x-2][y-1]==0): #controllo su x e y in modo da non considerare indici negativi
            lista.append([x-2,y-1]) # 0 indica posizione disponibile, quindi inserisco le coordiante
        else:
            lista.append(1) # 1 indica posizione non disponibile
        if(x-2>=0 and y+1>=0 and x-2<self._dim and y+1<self._dim and self._board[x-2][y+1]==0):
            lista.append([x-2,y+1])
        else:
            lista.append(1)
        if(x-1>=0 and y-2>=0 and x-1<self._dim and y-2<self._dim and self._board[x-1][y-2]==0):
            lista.append([x-1,y-2])
        else:
            lista.append(1)
        if(x-1>=0 and y+2>=0 and x-1<self._dim and y+2<self._dim and self._board[x-1][y+2]==0):
            lista.append([x-1,y+2])
        else:
            lista.append(1)
        if(x+1>=0 and y-2>=0 and x+1<self._dim and y-2<self._dim and self._board[x+1][y-2]==0):
            lista.append([x+1,y-2])
        else:
            lista.append(1)
        if(x+1>=0 and y+2>=0 and x+1<self._dim and y+2<self._dim and self._board[x+1][y+2]==0):
            lista.append([x+1,y+2])
        else:
            lista.append(1)
        if(x+2>=0 and y-1>=0 and x+2<self._dim and y-1<self._dim and self._board[x+2][y-1]==0):
            lista.append([x+2,y-1])
        else:
            lista.append(1)
        if(x+2>=0 and y+1>=0 and x+2<self._dim and y+1<self._dim and self._board[x+2][y+1]==0):
            lista.append([x+2,y+1])
        else:
            lista.append(1)
        return lista

def main():
        print("Le coordinate vengono date come una scacchiera, quindi di dimensione da 1 a n")
        n=0
        while (n<5):
            n=int(input("Inserisci la dim della scacchiera (N>=5): "))
        game = Scacchiera(n)
        gui = BoardGameGui(game)
        while(game._fine!=True):
            gui.main_loop()
        

if __name__ == "__main__":
	main()

