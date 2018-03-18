# BookInfoWebScraper
This repository holds the WebScraping of this web: 
https://www.packtpub.com/packt/offers/free-learning/

The purpose of this client is to obtain the title and 
the summary of the book that is offered at the previously 
mentioned URL.

#Core Aspects: 
   - O.S. used: `Ubuntu 16.04`
   - Python version: Python 2 (Version: 2.7)

#Requirements 
To install the dependencies I have added the file
**requirements.txt**.

To install the dependencies just execute 
the following command into the CommandLine.

_`pip install -r requirements.txt`_

#How to use it
First of all, **download** it.

After that, open a **CommandLine**.

To continue, _`cd /put/the/path/`_ 
and when you are at the right path, 
execute it using the following command:

_`python <file_name>.py`_

#Libraries
The libraries we used on this project, are specified on 
the requirements.txt (Check Requirements Section).

#Development
We divided our client into two functions, one that will 
download the web page that we specify and the that will 
parse and print the info that we specified.

To find the information that we want (html in which we are interested),
on the previously downloaded web (method used to obtain it:get_web), 
we used this BeautifulSoup method:
 
**`find_all("<html_tag>", "<html_class>")`**  
**[html_class] --> Optional parameter.**

The previously mentioned method is used too reduce the html
on we will be searching for a specific tag using BeautifulSoup
method: 

**`find("<html_tag>")`**

At the end, when you have found the information you 
were searching for, the last thing left is to print it.


