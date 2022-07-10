#!/usr/bin/python3

#Credits to StormPug/RTTGOD (Creator)

#Assigns grades to a given dataset of marks


#declare variables

ID=""; mark=0; totalStudents=0;

IDarray=[]
markarray=[]

def CalcLetterGrade(mark):
    if mark >=80 and mark<=100:
        grade='A'
    elif mark >=65 and mark<=79:
        grade='B'
    elif mark>=50 and mark<=64:
        grade='C'
    elif mark>=35 and mark<=49:
        grade='D'
    else:
        grade='E'
    return grade

def StringGen(mark):
    bar='#'*int(mark/2)
    return bar
try:
    #GET name of file
    fileNameIn=input("Enter file name: ")

    #get output file name
    fileNameOut=input("enter file output name: ")

    #reader to open file entered
    reader=open(fileNameIn,'r')

    #writer to write to file
    writer=open(fileNameOut, 'w')
    #make header
    print("{:10s} {:5s} {:5s}".format("ID Number","Mark","Grade"),file=writer)

    #make a nice header
    #print("{:10s}  {:5s}".format("ID Number","Mark"))

    for line in reader:
        line=line.rstrip('\n')

        #sort into array
        data=line.split(',')

        #sort data read from array
        ID=data[0]
        mark=int(data[1])

        #store into arrays seperately
        IDarray.append(ID)
        markarray.append(mark)

        #add student total
        totalStudents+=1

    
        

        #print nicely
        #print("ID Number: {:10s} Mark: {:5d}".format(ID,mark))

    #end for loop
    #call function to calculate letter grades using loop

    
    for markPS in markarray:
        gradeActual=CalcLetterGrade(markPS)
        #print(gradeActual)

        #call the function to draw #
        barDraw=StringGen(markPS)
        

        print("ID Number: {:10s} Mark: {:3d} Grade: {:3s} String: {:}".format(ID,mark,gradeActual,barDraw))
    #print(markarray)

        #print it to the output file
        print("ID Number: {:10s} Mark: {:3d} Grade: {:3s}".format(ID,mark,gradeActual),file=writer)
    #print(gradeActual)

    #print nicely
    #print("ID Number: {:10s} Mark: {:5d} Grade: {:3s}".format(ID,mark,gradeActual))

    print("Total students: {:}".format(totalStudents),file=writer)
    reader.close()
    writer.close()
    
except:
    print("error with", line)
