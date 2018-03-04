#Movie Vault
##Table of contents
1. Requirements. 
2. Installation  
2.1. How to use this code  
2.2. How does it works? 

  
###1. Requirements
To use this code you must have Python 2.7 installed and running in your computer.  
If you don't have Python follow these instructions to dowload and install.  
**Installing Python 2 on Mac OS X.**  
[http://docs.python-guide.org/en/latest/starting/install/osx/]() 

**Installing Python 2 on Linux.**  
[http://docs.python-guide.org/en/latest/starting/install/linux/]() 


**Installing Python 2 on Windows.**  
[http://docs.python-guide.org/en/latest/starting/install/win/]()

###2. Installation 
####2.1 How to use this code?
Just copy the contents to the folder of your preference and run the file **collection_listing.py** with Python.  

Running from command line:  
**Linux and Mac**  

``` 
/path/to/interpreter/python collection_listing.py 
```  
  or  
  
```  
python collection_listing.py 
``` 
**Windows**  
 
```
C:\Python27\python.exe C:\your\folder\collection_listing.py
``` 
or. 
 
```
python.exe collection_listing.py 
```
####2.2. How does it works?    
When you run the file **collection_listing.py**, Python compiles the code, reads the contents of **video_collection.py** (the file used to store all the movies and) and converts to html so in that way you can view it in your browser as a website.

When the page displays (**collection_listing.html**), put the mouse pointer over the title to show the storyline and relese year. Click on the image to view its trailer.

####2.2.1 Top 15 movies
On the right side of the screen there is a list with the top 15 movies rated by IMDb Users (actually the list has 250 titles but I selected only 15). This list is extracted from [IMDB](http://www.imdb.com/) via an API from [MyApiFilms](http://api.myapifilms.com/). Click on a title and you will be redirected to the IMDB movie page containing more information.