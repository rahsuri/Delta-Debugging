<h1>Delta-Debugging</h1>

<h3>Summary</h3>
This was a cool project I made in my Software Engineering class that used the method of Delta Debugging to obtain the smallest subset of input files (in this case images) that still had the optimal line coverage in the libpng program. This meant scraping all the useless files that do not actually provide coverage. 

<h3>Tutorial</h3>
To run this program, first extract the files and move both the large-png-suite file as well as the delta-libpng.py file into the libpng-1.6.34 file. Next, switch the directory to libpng-1.6.34.

Next, we need to download the latest version of a compression library. To do this, run:
<pre>$ sudo apt-get install libz-dev </pre>
Please also make sure you have python3 (version 3.5.2+) installed

Next, lets prepare our libpng program for running. To do this, we can run both of these commands:
<pre>$ sh ./configure CFLAGS="--coverage -static"</pre>
<pre>$ make clean ; make </pre>

Now, we can proceed with running our Delta Debugging program. To do this, we can run the following command:
<pre>$ python3 delta-libpng.py x</pre>
Where x is any value from 0-1638. This x value represents how many files we want to input into our program.

Warning: This could take multiple hours to run depending on your computing environment!
