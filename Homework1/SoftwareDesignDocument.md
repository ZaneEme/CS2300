<h1 align = "center">Programming Linear Algebra Software Design Document </h1>
 
 <h3 align="left"> 
 CS2300 Section 1 Spring 2022
 <p> Zane Emerick
 </h3>

# Project Description
Create multiple two-dimensional arrays the size of your first name and last name, and fill them with various numbers. Then write programs that can add and multiply these arrays to produce outputs in the form of text files. This should all be saved into a Github repository and shared with the professors.

# Approach

I solved this problem by first creating block comments for every section describing the requirements, and then writing code to fill those requirements. I had prior knowledge about the Numpy library, and decided that taking advantage of it's many methods would be very helpful for this assignment. 

 
# Detailed Design
## Programming Language

For this assignment I decided to use Python 3.10 with the Numpy library for all array arithmetic. I was hesitant to write the project in Java or C first, but once I started modeling out the problems, I realized many of the loops could be solved a much quicker way using Python and Numpy.


## Modules

### Part 1:
* **Mat (1-5):**
	* The functions named Mat1- Mat5 each create an array size Lastname x Firstname or a translation of that. Each containing an ascending list of various integers and decimal numbers. These are are each then output to a seperate text file following the naming scheme zEmerick_Mat(1-5).txt
		
###  Part 2: 
* **Main Loop** 
	* This program uses two for-loops to iterate over every combination of arrays, and add them together. Duplicates have been excluded as well (1,3 vs 3,1 yield the same sum)
		
### Part 3:
* **Multiply**
	* This program takes two inputs in the form of two dimensional arrays, and uses Numpy to multiply them together and write to a specified output file. This program also includes a main method in the case it is run by itself, where the input arrays are taken in the form of an integer representing a Mat array.
* **Runner**
	* This program, similar to the last, implements two for-loops that iterate through every combination of Mat arrays, and multiplies them together. All of the code to write to the files themselves is implemented into the Multiply program.


## Key Data Structures

The key data structure used in this array was the Numpy Array. The Numpy library provides functionality to make array-arithmetic very easy and straightforward. I decided to use this, as it was much less code on my part to have a library do the majority of the heavy lifting.

