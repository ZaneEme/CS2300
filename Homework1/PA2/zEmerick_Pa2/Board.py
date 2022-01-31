class Board:
    def __init__(self, size):
        self.gameBoard = []
        self.size = size

        for i in range(self.size):
            self.gameBoard.append(["." for j in range(self.size)])



    def printBoard(self):
        # First row numbers
        print("  ", end="")
        for x in range(1, self.size + 1):
            print(str(x) + "  ", end = "")
        print()

        y = 1
        for a in self.gameBoard:
            print(str(y) + " ", end = "")
            for b in a:
                print(str(b) + "  ", end = "")
            print("\n")
            y += 1
        
        print()

    def printToFile(self, file):
        f = open(file, "w")


        # First row numbers
        f.write("  ")
        for x in range(1, self.size + 1):
            f.write(str(x) + "  ")
        f.write("\n")

        y = 1
        for a in self.gameBoard:
            f.write(str(y) + " ")
            for b in a:
                f.write(str(b) + "  ")
            f.write("\n")
            y += 1
        
        f.write("\n")


    
