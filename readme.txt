This is a tool to shuffle an array of words based on an input secret seed and array length. 
It is written in python3 and deployed on docker on 20210106.
The docker container has the same python and numpy libraries pre-installed used during the inital creation of this tool, but you can run this script without docker as well. Make sure to have the correct numpy version as it might change in the future and impact the randomness of the input seed, thus giving a totally different array if you try to recreate the same array based on a unique input seed.

---

To run in docker: 
1. Make sure to have docker installed and up and running on your computer
2. run: docker build -t shufflearraycontainer /Path/To/This/Folder/With/Dockerfile/And/Python/Script
3. run: docker run -it shufflearraycontainer /bin/sh
4. You should now arrive inside the docker container
5. run: python3 shuffleArray -s 123456789 -l 24
	-s argument 123456789 is your input secret
	-l argument 24 is your array length, in this case 24.
6. The output is a shuffled array from 1-24 based on the given input secret seed.

Use this original array for whatever purpose you opened this tool for in the first place.

---

The original array, created 20210106, before WWIII, has been generated with the following libraries:
numpy version: 1.19.5
argparse version: 1.1	
python version: 3.9.1

