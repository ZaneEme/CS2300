class Board:
    # Build the board with a given size
    def __init__(self, size):
        self.gameBoard = []
        self.size = size

        for _ in range(self.size):
            self.gameBoard.append(["." for _ in range(self.size)])

    # Print the board to console
    def printToConsole(self):
        # First row numbers for decoration
        print("  ", end="")
        for xCounter in range(1, self.size + 1):
            print(str(xCounter) + "  ", end="")
        print()

        # Print board itself
        yCounter = 1
        for row in self.gameBoard:
            print(str(yCounter) + " ", end="")
            for col in row:
                print(str(col) + "  ", end="")
            print("\n")
            yCounter += 1

        print()

    # Print the board to a specified file
    def printToFile(self, file):
        file = open(file, "w")

        # First row numbers for decoration
        file.write("  ")
        for xCounter in range(1, self.size + 1):
            file.write(str(xCounter) + "  ")
        file.write("\n")

        # Print the board itself
        yCounter = 1
        for row in self.gameBoard:
            file.write(str(yCounter) + " ")
            for col in row:
                file.write(str(col) + "  ")
            file.write("\n")
            yCounter += 1

        file.write("\n")
