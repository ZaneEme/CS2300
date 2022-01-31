import numpy as np


for fileNum in range(1, 6):

    with open(f"pa3_input_A_{fileNum}.txt") as file:
        firstLine = np.array(file.readline().split(), dtype='d')
        secondLine = np.array(file.readline().split(), dtype='d')
        
        outFile = open(f"zemerick_output_A_{fileNum}.txt", "w")
        
        #solve for Ax = b

        bigArray = np.row_stack((firstLine, secondLine))

        A, b = np.split(bigArray, [2], 1)
        solved = np.zeros(5)

        try:
            solved = np.linalg.solve(A, b)
            solved = np.round(solved, 4)
            np.savetxt(outFile, solved) 
        except:
            solved = ("equation is unsolveable.")
            outFile.write(solved)

