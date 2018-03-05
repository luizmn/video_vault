#Movie Vault
##Table of contents
1. Requirements. 
2. Installation  
2.1. How to use this code  
2.2. How does it works? 

  
###1. Requirements
To use this code you must have:  
* An active internet connection (to retrieve movie information);  
* Python 2.7 installed and running in your computer.  
* Json module;  
* Requests module;   

If you don't have Python follow these instructions to download and install.  

**Installing Python 2 on Mac OS X.**  
[http://docs.python-guide.org/en/latest/starting/install/osx/]() 

**Installing Python 2 on Linux.**  
[http://docs.python-guide.org/en/latest/starting/install/linux/]() 


**Installing Python 2 on Windows.**  
[http://docs.python-guide.org/en/latest/starting/install/win/]()

In some cases the Requests and Json modules can already be installed but just to make sure, open the terminal of your preference (e.g. terminal, MS-DOS prompt or xterm) and just type in (as an administrator):  
Example:  
```
foo@bar:~$ sudo easy_install requests
```  

After the execution of the first command, type:  
```
foo@bar:~$ sudo easy_install json  
```  

If the above command does not works try this:
```
foo@bar:~$ sudo easy_install simplejson
```  

In Windows:  
```
C:\Windows> easy_install requests
```  

After the execution of the first command, type:  
```
C:\Windows> easy_install json  
```  

If the above command does not works try this:
```
C:\Windows> easy_install simplejson
```  

**Note:** pip can also be used instead of easy_install.  
Just type this:  
```
pip install
```  

Example:  
```
pip install requests
```  
###2. Installation 
####2.1 How to use this code?
Just copy the contents to the folder of your preference and run the file **video_collection.py** with Python.  

**Note about opening .py files directly:** It is not recommend opening python files ending with .py by double clicking them. Instead, open the scripts from within your IDLE session, using **File → Open**. This is because the behaviour you get can be unexpected, although it won't do any harm. 
#####2.1.1 Running from command line:  
**Linux and Mac**  

``` 
/path/to/interpreter/python video_collection.py 
```  
  or if you are already in the video_collection.py folder: 
  
```  
python video_collection.py 
``` 
**Windows**  
 
```
C:\Python27\python.exe C:\your\folder\video_collection.py
``` 
or if you are already in the video_collection.py folder: 
 
```
python.exe video_collection.py 
```
#####2.1.2 Running from IDLE:
The IDLE GUI (graphical user interface) is automatically installed with the Python interpreter.   
IDLE stands for integrated development environment (IDE) for editing and running Python 2.x or Python 3 programs. 
IDLE was designed specifically for use with Python and has a number of features to help you develop your Python programs including powerful syntax highlighting.  
Basically you have two ways to open the IDLE GUI: 
Via your OS programs list or through terminal/MS-DOS prompt.

#####2.1.2.1 Open IDLE via OS programs list
**Mac**  
If you are running Mac, from the Applications folder, open IDLE as follows:
**Applications → Python 2.7 → IDLE** will open a "Python Shell".  
Alternatively you can search for "IDLE" in **spotlight** and click in the icon.

**Windows**  
If you are running Windows, you will be starting IDLE from the Python XY package. From **Start Menu**, open IDLE as follows:
**Start → All Programs → Python 2.7 → IDLE (Python GUI).**  
The typical result will be a window labeled "Python Shell".  
Example:  
![Python Shell](https://pythonfun.files.wordpress.com/2011/08/screenshot-python-shell.png)
**Linux**  
Enter 'idle' in the Application Launcher.

**After opening the IDLE program**  
Using **File → Open** in Windows or Mac, go to the folder where the files are located. Open the file called `video_collection.py`, which might show up as `video_collection` or as `video_collection.py` in the directory listing.
In the menu, select **Run → Run Module**. (The shortcut for this is F5.) This should compile the code, access the internet and display the movie web site in the browser.

#####2.1.2.2 Open IDLE via terminal/MS-DOS prompt
The command below works for Windows, Linux and Mac.  
When you open up a new terminal window (e.g. terminal, MS-DOS prompt or xterm), just type in `idle`  
Example:  
```
foo@bar:~$ idle
```  
or  
```
C:\Windows> idle
```

More information on IDLE can be found in its [documentation] (https://docs.python.org/2/library/idle.html).
#####2.1.3 Opening and running the file inside your OS
To open your Python file, locate the file in the folder, click once on the file name it to highlight it, then right-click on the mouse to see the file options and select "Edit with IDLE" 
to open the editor window.   
 
Once the editor opens, select **Run Module** from the **Run menu** located in the toolbar.
Then you will see your program running in a Python Shell window and after a few seconds, the browser will open displaying the generated web site.



####2.2. How does it works?    
When you run the file **video_collection.py**, Python compiles the code, reads the contents of **video_collection.py** (the file used to store all the movies and) and converts to html so in that way you can view it in your browser as a website.

When the page displays (**collection_listing.html**), put the mouse pointer over the movie title to show the storyline and release year. Click on the image to view its trailer in Youtube.

####2.2.1 Top 15 movies list
On the right side of the screen there is a list with the top 15 movies rated by IMDb Users (actually the [list](http://www.imdb.com/chart/top) has 250 titles but for this site, only the first 15 are displayed). This list is extracted from [IMDB](http://www.imdb.com/) via an API from [MyApiFilms](http://api.myapifilms.com/imdb.do).   
Click on a title and you will be redirected to the IMDB page from that movie, containing more information.