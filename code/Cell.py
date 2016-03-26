class InputCell:
    taken = False
    inputQueue = 0

    def addCar(self):
        self.inputQueue += 1

    def getQueue(self):
       return self.inputQueue

    def actualize(self,nextCell):
        if self.taken==True:
            if nextCell.taken==False:
                if self.inputQueue>0:
                    self.taken=True
                    self.inputQueue -=1
                else:
                    self.taken=False
        else:
            if self.inputQueue>0:
                self.taken = True
                self.inputQueue -= 1

class OutputCell:
    taken = False
    outputQueue = 0

    def getOutput(self):
        return self.outputQueue

    def actualize(self,prevCell):
        if self.taken == True:
            self.outputQueue +=1
        if prevCell.taken==False:
            self.taken=False
        else:
            self.taken=True


class trafficLightCell:
    taken = False
    open = False

    def changeOpen(self,o):
        self.open=o

    def actualize(self,prevCell,nextIntersectionCell):
        if self.open==False:
            if self.taken==True:
                pass
            else:
                if prevCell.taken==True:
                    self.taken=True
        else:
            if self.taken==True:
                if nextIntersectionCell.takenV==False and nextIntersectionCell.takenV==False:
                    self.taken=False
            else:
                if prevCell.taken==True:
                    self.taken=True


class intersectionCell:
    takenH = False
    takenV = False

    def actualize(self,trafficLightCellH,trafficLightCellV,postIntersectionCellH,postIntersectionCellV):
        dirH = True if trafficLightCellH.open else False
        if self.takenH==True or self.takenV==True:
            if self.takenH:
                if postIntersectionCellH.taken==False:
                    self.takenH=False
                    self.takenV=False
            else:
                if postIntersectionCellV.taken==False:
                    self.takenH=False
                    self.takenV=False
        else:
            if dirH:
                if trafficLightCellH.taken==True:
                    self.takenH=True
                    self.takenV=False
            else:
                if trafficLightCellV.taken==True:
                    self.takenV=True
                    self.takenH=False

class postIntersectionCell:
    taken = False

    def actualize(self,intersectionCell,nextCell,H):
        if H:
            if self.taken==False:
                if intersectionCell.takenH==True:
                    self.taken=True
            else:
                if nextCell.taken==False:
                    self.taken=False
        else:
            if self.taken==False:
                if intersectionCell.takenV==True:
                    self.taken=True
            else:
                if nextCell.taken==False:
                    self.taken=False


class normalCell:
    taken = False

    def actualize(self,prevCell,nextCell):
        if self.taken==False:
            if prevCell.taken==True:
                self.taken=True
        else:
            if nextCell.taken==False:
                self.taken=False



def getDefaultConfiguration():
    board = []
    a = intersectionCell()
    b = intersectionCell()
    c = intersectionCell()
    d = intersectionCell()
    board.append([InputCell(),normalCell(),normalCell(),trafficLightCell(),a,
        postIntersectionCell(),normalCell(),normalCell(),trafficLightCell(),
        b,postIntersectionCell(),normalCell(),normalCell(),OutputCell()])
    board.append([InputCell(),normalCell(),normalCell(),trafficLightCell(),c,
        postIntersectionCell(),normalCell(),normalCell(),trafficLightCell(),
        d,postIntersectionCell(),normalCell(),normalCell(),OutputCell()])
    board.append([InputCell(),normalCell(),normalCell(),trafficLightCell(),a,
        postIntersectionCell(),normalCell(),normalCell(),trafficLightCell(),
        c,postIntersectionCell(),normalCell(),normalCell(),OutputCell()])
    board.append([InputCell(),normalCell(),normalCell(),trafficLightCell(),b,
        postIntersectionCell(),normalCell(),normalCell(),trafficLightCell(),
        d,postIntersectionCell(),normalCell(),normalCell(),OutputCell()])
    return board