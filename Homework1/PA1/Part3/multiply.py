import numpy as np

# Given two arrays, attempt to multiply them and write the output to a specified file.
def multiply(arrayOne, arrayTwo, outName):
    file = open(outName, "w")

    try:
        result = np.multiply(arrayOne, arrayTwo)
        np.savetxt(file, result, fmt="%s")
    except:
        file.write("Error: Multiplication cannot be computed")

    file.close()

# If the program is run as a standalone, take two inputs and multiply their corresponding arrays.
if __name__ == "__main__":
    firstArrayNum = input("Enter a number (1-5): ")
    secondArrayNum = input("Enter a second number (1-5): ")
    outName = input("Enter the name of the file to write to: ")

    arrayOne = np.loadtxt(
        (f"../Part1/zEmerick_P1_Mat{0}.txt", firstArrayNum), dtype="str"
    )
    arrayTwo = np.loadtxt(
        (f"../Part1/zEmerick_P1_Mat{0}.txt", secondArrayNum), dtype="str"
    )

    multiply(arrayOne, arrayTwo, outName)
