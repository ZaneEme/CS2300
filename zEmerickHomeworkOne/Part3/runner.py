import numpy as np
from multiply import multiply

# load each array from previous question
Mat1 = np.loadtxt("../Part1/zEmerick_Mat1.txt", dtype="str")
Mat2 = np.loadtxt("../Part1/zEmerick_Mat2.txt", dtype="str")
Mat3 = np.loadtxt("../Part1/zEmerick_Mat3.txt", dtype="str")
Mat4 = np.loadtxt("../Part1/zEmerick_Mat4.txt", dtype="str")
Mat5 = np.loadtxt("../Part1/zEmerick_Mat5.txt", dtype="str")

listOfLists = [Mat1, Mat2, Mat3, Mat4, Mat5]

# Loop arrays and multiply
for firstNum in range(0, 5):
    for secNum in range(firstNum + 1, 5):

        path = "zEmerick_p2_out" + str(firstNum + 1) + str(secNum + 1) + ".txt"

        multiply(listOfLists[firstNum], listOfLists[secNum], path)
