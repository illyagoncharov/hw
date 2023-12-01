class Chessman:
    name = 'figura'
    color = 'white'
    place_on_the_board = (0,0)
    move = True

    def change_color(self): #змінює колір фігури
        self.color = 'blackwhite'.replace(self.color, '')
        return self.color

    def _inside_the_chessboard(self, x:int,y:int):# перевіряє чи клітина в межах дошки
        if not ((0 <= (x) < 8) and (0 <= (x) < 8)):
            print(f'{(x,y)} outside_the_chessboard')
            return False
        else:
            return True

    def change_place(self, x:int, y:int):# змінюємо початкову позицію фігури
        if self._inside_the_chessboard(x, y):
            self.place_on_the_board = (x,y)
            print(f'New place on the board for {self.color}_{self.name}_ is {self.place_on_the_board}')
            return self.place_on_the_board

    def _running_condition(self, x:int, y:int, x0:int, y0:int):# умови здійснення ходу
        return self.move

    def is_the_move_possible(self, x:int, y:int):# перевіряє чи можливо виконати хід н нові координати
        x0 = self.place_on_the_board[0]
        y0 = self.place_on_the_board[1]
        if (x0, y0) == (x, y):
            print(f'{self.color}_{self.name}{(x0,y0)}_ remained in position')
            return True
        if self._inside_the_chessboard(x, y):
            if self._running_condition(x,y,x0,y0):
                print(f'For {self.color}_{self.name}{(x0,y0)}_ move on {(x,y)} is possible')
                return True
        print(f'For {self.color}_{self.name}{(x0,y0)}_ move on {(x,y)} is impossible')
        return False

#--------------------------------------------------------------------------------------------
class King(Chessman):
    name = 'king'

    def _running_condition(self, x:int, y:int, x0:int, y0:int):
        self.move = (abs(x0 - x) <= 1 and abs(y0 - y) <=1)
        return self.move


class Bishop(Chessman):
    name = 'bishop'

    def _running_condition(self, x:int, y:int, x0:int, y0:int):
        self.move = (abs(x0 - x) == abs(y0 - y))
        return self.move


class Rook(Chessman):
    name = 'rook'

    def _running_condition(self, x:int, y:int, x0:int, y0:int):
        self.move = (x == x0 or y == y0)
        return self.move


class Queen(Chessman):
    name = 'queen'

    def _running_condition(self, x:int, y:int, x0:int, y0:int):
        self.move = ((x == x0 or y == y0) or (abs(x0 - x) == abs(y0 - y)))
        return self.move


class Knight(Chessman):
    name = 'knight'

    def _running_condition(self, x:int, y:int, x0:int, y0:int):
        self.move = ((abs(x0 - x), abs(y0 - y)) == (2,1) or (abs(x0 - x), abs(y0 - y)) == (1,2))
        return self.move

class Pawn(Chessman):
    name = 'pawn'

    def _running_condition(self, x:int, y:int, x0:int, y0:int):
        if self.color == 'white':
            self.move = ((x0 == x) and ((y0 - y) == 1))
        if self.color == 'black':
            self.move = ((x0 == x) and ((y0 - y) == -1))
        return self.move


pawn = Pawn()
bishop = Bishop()
knight = Knight()
rook = Rook()
queen = Queen()
king = King()
cheesman_list = [pawn, bishop, king, knight, rook, queen]

def check_place(list_cman:list, x:int, y:int): # перевіряє яка з фігур здатна переміститись на нові координати
    return [ i for i in list_cman if i.is_the_move_possible(x,y)]


#pawn.change_color()
pawn.change_place(4,3)
rook.change_place(4,5)
king.change_place(3,4)
queen.change_place(2,2)
bishop.change_place(5,2)
knight.change_place(3,2)
print('-----------------')
print(check_place(cheesman_list, 4, 4))

