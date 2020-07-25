# Spiking neural network (SNN)

## Author:
Geraldas Kastauna\
https://www.geraldaskastauna.com

## Project supervisor:
Professor Dr. Chris Huyck\
https://www.cwa.mdx.ac.uk/chris/chrisroot.html

## University:
Middlesex University\
The Burroughs, Hendon\
London, NW4 4BT\
United Kingdom

## Disseration theme:
"Learning with spiking neural networks"

## Requirements (what I used during implementation)
* Linux Ubuntu Distribution 16.04 (xenus) x64
* Python 3.8.3 (https://www.python.org/downloads/)
* Conda 4.8.2 (https://docs.conda.io/projects/conda/en/latest/index.html)
* PyNN 0.9.5 (http://neuralensemble.org/docs/PyNN/)
* Numpy 1.19.1 (https://numpy.org/)
* Iris dataset (https://archive.ics.uci.edu/ml/datasets/iris)

## About the program:
**snn-stdp.py** is the main program, all the info about the program is inside the file commented at the top.\
**get-networks-accuracy.py** is used to get the accuracy of the network, info at the top of the file.\
**read-pkl-spikes.py** is used to check the spikes from pkl files that were generated by **snn-stdp.py** 
during training and testing phases.\

## How to use:
1. Check if there are **iris-train.txt** and **iris-test.txt** files.
2. Make sure everything from the requirements section is installed and up-to-date.
3. Run **snn-stdp.py**. Training and testing results are saved in **results folder**
4. If you wanna check the spikes that were generated during training or testing phases, 
edit the **read-pkl-spikes.py** file (info on what to edit is commented inside the file)
and then run the code and check the console for neuron number and spike time sequence.
5. To get the accuracy on test file (iris-test.txt) run **get-networks-accuracy.py**.
The amount of correct answers will be printed to the console along with accuracy percentage.

## Contact info:
Name: Geraldas Kastauna\
University email: GK468@live.mdx.ac.uk\
Personal: geraldaskastauna@gmail.com
