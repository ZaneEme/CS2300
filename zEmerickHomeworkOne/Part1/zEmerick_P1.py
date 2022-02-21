# Mat1:
# Number of Rows = Number of Letters in your first name
# Number of Columns = Number of Letters in your last name
#
# Starting at index position (0,0) begin filling Mat1 with
# values starting at 1 and increasing by 1 each time as you
# iterate the indices over the columns first, then over rows second.
def Mat1(firstName, lastName):
    array = [[0] * len(lastName)] * len(firstName)
    count = 0
    with open("zEmerick_Mat1.txt", "w") as file:
        for row in array:
            for _ in row:
                if count < 10:
                    file.write("0" + str(count) + " ")
                else:
                    file.write(str(count) + " ")
                count += 1
            file.write("\n")


# Mat2:
# Number of Rows = Number of Letters in your last name
# Number of Columns = Number of Letters in your first name
#
# Starting at index position (0,0) begin filling Mat2 with
# values starting at 2 and increasing by 3 each time as you
# iterate the indices over the rows first, then over columns second.
def Mat2(firstName, lastName):
    array = [[0 for _ in range(len(firstName))] for _ in range(len(lastName))]
    count = 2
    colIndex = 0
    with open("zEmerick_Mat2.txt", "w") as file:
        while colIndex < len(firstName):
            for row in array:
                row[colIndex] = count
                count += 3
            colIndex += 1
        for row in array:
            for col in row:
                if col < 10:
                    file.write("0" + str(col) + " ")
                else:
                    file.write(str(col) + " ")
            file.write("\n")


# Mat3:
# Number of Rows = Number of Letters in your last name
# Number of Columns = Number of Letters in your first name
#
# Starting at index position (0,0) begin filling Mat3 with
# values starting at 0.6 and increasing by 0.2 each time as you
# iterate the indices over the rows first, then over columns second.
def Mat3(firstName, lastName):
    array = [[0 for _ in range(len(lastName))] for _ in range(len(firstName))]
    count = 0.6
    colIndex = 0
    with open("zEmerick_Mat3.txt", "w") as file:
        while colIndex < len(lastName):
            for row in array:
                row[colIndex] = round(count, 2)
                count += 0.2
            colIndex += 1
        for row in array:
            for col in row:
                file.write(str(col) + " ")
            file.write("\n")


# Mat4:
# Number of Rows = 5, number of Columns = 9
#
# Starting at index position (0,0) begin filling Mat4 with
# values starting at 3 and increasing by 2 each time as you
# iterate the indices over the rows first, then over columns second.
def Mat4():
    array = [[0 for _ in range(9)] for _ in range(5)]
    count = 3
    colIndex = 0
    with open("zEmerick_Mat4.txt", "w") as file:
        while colIndex < 9:
            for row in array:
                row[colIndex] = count
                count += 2
            colIndex += 1
        for row in array:
            for col in row:
                if col < 10:
                    file.write("0" + str(col) + " ")
                else:
                    file.write(str(col) + " ")
            file.write("\n")


# Mat5:
# Numbers of Rows = 5, number of Columns = 9
#
# Starting at index position (0,0) begin filling Mat5 with
# values starting at -7 and increasing by 1 each time as you
# iterate the indices over the columns first, then over rows second.
def Mat5():
    array = [[0] * 9] * 5
    count = -7
    with open("zEmerick_Mat5.txt", "w") as file:
        for row in array:
            for _ in row:
                if count >= 0 and count < 10:
                    file.write("0" + str(count) + " ")
                else:
                    file.write(str(count) + " ")
                count += 1
            file.write("\n")


if __name__ == "__main__":
    Mat1("Zane", "Emerick")
    Mat2("Zane", "Emerick")
    Mat3("Zane", "Emerick")
    Mat4()
    Mat5()
