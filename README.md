Dasher Assistant
================

The goal of this application is to provide statistical information to dashers.
It will try to help figure out what regions, times, and restaurants are better paying.
It also features a plugin structure so anyone can create their own analysis tool.

How To Run
----------

To run from the command line, navigate to the root of the project and run:

    python3 -m assistant
    
Adding Plugins
--------------

To create a statistical plugin, create a folder in the stats folder.
Then add your code, putting the main running code in an \_\_init\_\_.py file.

There are 2 methods you need to implement:
 * getName()- simply returns a text definition of what the plugin does
 * runStat(dashes)- gives you a Dashes object to analyze.
 This is your main running function.
 It does nothing with the return, so you will need to print any output you want