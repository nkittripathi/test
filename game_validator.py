import numpy as np
import operator

class cell():

    def __init__(self, number=0, constraintType='', constraintRow=0,constraintCol=0):
        self.number = number
        self.constraintType = constraintType
        self.constraintRow = constraintRow
        self.constraintCol = constraintCol
    
    def get_number(self):
        return self.number;

    def set_number(self, number):
        self.number = number

    def get_constraintType(self):
        return self.constraintType;

    def set_constraintType(self, constraintType):
        self.constraintType = constraintType

    def get_constraintRow(self):
        return self.constraintRow;

    def set_constraintRow(self, constraintRow):
        self.constraintRow = constraintRow

    def get_constraintCol(self):
        return self.constraintCol;

    def set_constraintCol(self, constraintCol):
        self.constraintCol = constraintCol

def solution_Validator(board, numElement):
    return validator(board, numElement);

def validator(board, numRows):
    rowcolSet=set()
    # Check the uniqueness of elements in rows
    for i in range(numRows):
        for j in range(numRows):
            if (board[i][j].get_constraintType()!=''):
                if (cellValidator(board,board[i][j])==False):
                    return False;

            rowcolSet.add(board[i][j].get_number())

        if ((len(rowcolSet) != numRows) ):
            return False;       
        rowcolSet=set()
    
    # Check the uniqueness in of elements in column    
    colrowSet=set()
    for i in range(numRows):
        for j in range(numRows):
            colrowSet.add(board[j][i].get_number())
        if (len(colrowSet) != numRows):
            return False;
        colrowSet=set()

    return True

def cellValidator(board, cellInfo):
    if(cellInfo.get_constraintType()==''):
        return True
    else:
        return get_truth(cellInfo.get_number(),cellInfo.get_constraintType(),board[cellInfo.get_constraintRow()][cellInfo.get_constraintCol()].get_number())

def get_truth(inp1, inOperator, inp2):
    ops = {'>': operator.gt,
           '<': operator.lt,
           '>=': operator.ge,
           '<=': operator.le,
           '=': operator.eq}
    return ops[inOperator](inp1, inp2)


if __name__ == "__main__":

    board = [
            [cell(21,'>',0,1),cell(2,'<',0,0),cell(3,'',0,0),cell(4,'',0,0)],
            [cell(5,'',0,0),cell(6,'',0,0),cell(17,'>',2,2),cell(8,'',0,0)],
            [cell(9,'',0,0),cell(10,'<',3,1),cell(11,'<',1,2),cell(12,'',0,0)],
            [cell(23,'>',3,1),cell(14,'>',2,1),cell(15,'',0,0),cell(16,'',0,0)]
        ]

    numElement = len(board)
    
    if solution_Validator(board, numElement):
        print("Board is Valid")
    else:
        print("Board is Invalid")
