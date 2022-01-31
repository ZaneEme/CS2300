-import numpy as np


for fileNumber in range(1, 6):
    with open(f"pa3_input_C_{fileNumber}.txt") as file:
        xCoords = file.readline().split()
        yCoords = file.readline().split()
        
  
        xCoords = list(map(float, xCoords))
        yCoords = list(map(float, yCoords))
        area = 0.5 * ( (xCoords[0] * (yCoords[1] - yCoords[2])) + (xCoords[1] * (yCoords[2] - yCoords[0])) + (xCoords[2] * (yCoords[0] - yCoords[1])) ) 
        

        point1 = np.array([xCoords[0], yCoords[0]])
        point2 = np.array([xCoords[1], yCoords[1]])
        point3 = np.array([xCoords[2], yCoords[2]])

        distance = np.cross((point2 - point1), (point3 - point1)) / np.linalg.norm(point2 - point1)
        area = abs(area)
        print(area)

        outFile = open(f"zemerick_output_C_{fileNumber}.txt", "w")

        outFile.write(str(round(abs(area), 4)))
        outFile.write("\n")
        outFile.write(str(round(abs(distance), 4)))
