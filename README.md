This file contains notes and instructions about the replication of the language scoring experiment.
We have prepared a docker that runs the code, but our computers weren't efficient enough to run it till the end.

I- Investigate the experiments' results directly:
We have included the Results.txt file that has all the output from running IdeaPOC.py (the main scripts). This file
contains all the experiments results and you can look at it without running any of the scripts, this is the easier way.


II- IT MIGHT BE EASIER TO RUN THE SCRIPT MANUALLY THAN IN A DOCKER CONTAINER, AND IT WILL BE LESS TIME CONSUMING, WE ADVISE YOU DO IT THIS WAY:
1- We have prepared all the data for you, parsed and features extracted.
2- You need to install python
3- You need to install numpy, scipy, sklearn, xgboost
4- You may encouter an error while trying to install xgboost in windows, if that's the case, install pipwin with "pip install pipwin" then install xgboost with "pipwin install xgboost"
5- Go to the root folder "Reproduced", open a terminal and run : python -Wignore IdeaPOC.py


Here are the steps if you want to run it inside a docker container:
1- Remove all the Meta files in the Datasets folder
2- Remove all the files in the Datasets/LANG and Datasets/LANG-Parsed for LANG in [CZ, IT, DE]
3- Remove all the files from the features folder
4- Go to the bulkparselang.sh, comment the line that has "../udp/udpipe.exe" (used for windows) and decomment the line with "../udp/udpipe-1.2.0-bin/bin-linux64/udpipe"
5- Go to root folder "Reproduced"
6- Open a terminal and run: docker-compose up --build

7- The docker has been made in a windows environment, which usually uses CRLF instead of LF, this might cause some problems while running
the docker container, if that was the case with you, make sure to go to your IDE, and change the break line to LF
