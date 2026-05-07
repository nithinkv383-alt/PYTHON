import os.path
import sys

fname = input("Enter the filename to sort: ")

# Check if input file exists
if not os.path.isfile(fname):
    print("File", fname, "does not exist.")
    sys.exit()

# Read the file
infile = open(fname, "r")
lines = infile.readlines()
infile.close()

# Clean and sort the list
lineList = []
for line in lines:
    lineList.append(line.strip()) # strip() removes extra newlines

lineList.sort()

# Write to the new file
outfile = open("sorted.txt", "w")
for line in lineList:
    outfile.write(line + "\n")
outfile.close()

# Final Output
print("Sorted.txt created successfully.")
print("Total lines processed:", len(lineList))