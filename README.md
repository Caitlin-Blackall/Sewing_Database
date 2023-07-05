# Sewing Database

*Completed July 2023*

## Idea
This project stemmed from my hobby of sewing. I have a lot of 
sewing patterns and wanted an easy way to store and search 
these patterns to find an appropriate pattern.

## Process
I already had a clear picture of how I wanted this database 
to look - I needed easy-to-use functions, ability to add pictures 
to pattern files and ability to update the files as I sewed 
patterns. To make sure I didn't lose my progress and to put into 
practice skills I had recently learnt doing the CodeAcademy 
git and GitHub course, I created a repository on GitHub for this 
project and made sure I was making regular commits.

I then started with writing code to open, read and write 
to a CSV file. From here, I created functions in order to be 
able to add, search and update patterns within the database.

I used tkinter to make the interface more user-friendly. I also 
used pandas within the 'Updating' section as this made it easier 
to select and edit the information contained within the 
database.

I also put comments in my code to explain each function and also 
within the code, usually when I implemented something I hadn't 
used before (ie. within the pandas section). This helped me keep 
track of what I was up to, what each function did and what each 
section of the code was doing.

## Learning
### Challenges

**1. Keeping track of all the code!**
+ Code can get big and confusing very easily! As discussed in  
the future work section, it would be very useful to have different 
sections / functions of the code kept in separate files. This 
would make it more readable and more organised.


+ Using comments within the code - in some sections I used  
comments to help me think through the code I needed to write but 
it would be useful to do this more routinely to demonstrate my 
thought process (as well as help myself keep track of what I 
was doing!)


**2. Error handling with tkinter**
+ It was initially challenging to get the interface to do what 
I wanted it to do. Using the command= option within the 
checkbox tool and setting this to a different function ended up 
being key in this process.

+ It was also a bit of a learning curve discovering how to pull 
relevant information from the interface and timing when to do 
this so that I could access the information after destroying 
the interface.

**3. Using Pandas**
+ The main challenge I faced with pandas was accessing the 
right index of the database. This was mainly challenging 
because my knowledge of the syntax was lacking and I was using 
variables.


### New Skills
+ The biggest skill that I learnt throughout this process was using 
tkinter to develop user interfaces. I've previously done 
something similar using macros on Microsoft Excel but using 
python has been much easier in many ways. It was easier to code,
easier to layout in a nice way and easier to handle errors. I 
used labels, entry boxes, buttons and checkboxes to develop my user 
interfaces and implemented IntVar() to pull the variables from 
the interface into useable data within the code.


+ Using pandas to update CSV files! It would be useful to explore 
how this program works in more detail so that I can manipulate 
CSV files more easily in future.

## Future Work
It would be great to revisit this database in future when I have 
more skills in python. Ideally, this would be an online 
interface that wouldn't need to be opened in python to run. This 
would allow further flexibility in the application of the project 
as well as allow me to work on the design elements of the 
presentation more.

It would also be great to add an option to sort by category 
as well as by availability of patterns. This would make the 
database more user-friendly and better for the application that 
I want. Furthermore, making an option of ensuring categories 
are exact matches as well (ie. searching by Dresses and Tops will 
only result in matches that are BOTH Dresses and Tops, rather than 
either Dresses or Tops).

I find it useful when searching or trying to choose which pattern 
I want to sew to see images of how it looks. This is definitely 
a feature to add in future, potentially one that would be easier 
if the database was a web application. Making this a web 
application would also help with other design aspects as well as 
overall useability.

Linking the documents to the search feature so that the appropriate 
pattern can be opened following the search would be great. This 
may also link to a feature of just being able to open a particular 
file.

## Conclusion
Overall, I think this was a great project. It's something that 
is useful in my life so it was easy to come up with the outline of 
the database. It was a challenging project but did allow me to 
use my existing knowledge to logically think through solutions 
to more complex coding problems. I learnt a lot of new things 
throughout this process, including tkinter and pandas. But I 
also learnt a lot about coding in general (structuring complex 
code, organising large blocks of code, etc). I'm really glad 
I managed to complete this database and I'm keen to continue to 
work on my coding skills and complete more complex projects 
soon!