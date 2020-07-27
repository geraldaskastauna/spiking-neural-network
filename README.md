# Spiking neural network (SNN)

## Author:
Geraldas Kastauna\
http://www.geraldaskastauna.com

## Project supervisor:
Professor Dr. Chris Huyck\
https://www.cwa.mdx.ac.uk/chris/chrisroot.html

## University:
Middlesex University\
The Burroughs, Hendon\
London, NW4 4BT\
United Kingdom

## Disseration theme:
**Learning with spiking neural networks**

A spiking neural network that uses spike-timing-dependent plasticity (STDP) synapses for training on half of UCI iris data set
and then runs tests on the other half of the data.

## Requirements (what I used during implementation)
* Linux Ubuntu Distribution 16.04 (xenus) x64
* Python 3.8.3 (https://www.python.org/downloads/)
* Conda 4.8.2 (https://docs.conda.io/projects/conda/en/latest/index.html)
* PyNN 0.9.5 (http://neuralensemble.org/docs/PyNN/)
* Nest-Simulator 2.20.0 (https://nest-simulator.org/)
* Numpy 1.19.1 (https://numpy.org/)
* UCI iris dataset (https://archive.ics.uci.edu/ml/datasets/iris)

## About the program:
**snn-stdp.py** is the main program, all the info about the program is inside the file commented at the top.\
**get-networks-accuracy.py** is used to get the accuracy of the network, info at the top of the file.\
**read-pkl-spikes.py** is used to check the spikes from pkl files that were generated by **snn-stdp.py** 
during training and testing phases.

## About the SNN:
This spiking neural network is trained on UCI iris dataset that contains total of 150 irises, 50 for each class (iris-setosa, iris-versicolour, iris-virginica). Iris data is split into half (75 for training, 75 for testing).\
This SNN uses only two layers of neurons:\
* Presynaptic layer which contains 104 neurons (26 neurons for each iris data feature(4)).
* Postsynaptic layer which contains 3 neurons (each neuron represents one of three iris class).

## Accuracy and speed:
**Accuracy**\
Best accuracy I managed to get:
* Training on **iris-train.txt** data and testing on **iris-test.txt**
Correct system answers: 66 / 75\
Accuracy percentage: **88.0 %**
* Training on **iris-test.txt** data and testing on **iris-train.txt**
Correct system answers: 62 / 75\
Accuracy percentage: **82.66666666666667 %**

**Speed**\
Tested speed using Linux terminal command - **time python snn-stdp.py**\
Results were the same for both cases:
real    0m **3.234s**\
user    0m **3.137s**\
sys     0m **0.096s**\

## How to use:
1. Check if there are **iris-train.txt** and **iris-test.txt** files.
2. Make sure everything from the requirements section is installed and up-to-date.
3. Run **snn-stdp.py**. Training and testing results are saved in **results** folder.
4. If you wanna check the spikes that were generated during training or testing phases, 
edit the **read-pkl-spikes.py** file (info on what to edit is commented inside the file)
and then run the code and check the console for neuron number and spike time sequence.
5. To get the accuracy on test file (iris-test.txt) run **get-networks-accuracy.py**.
The amount of correct answers will be printed to the console along with accuracy percentage.

## Contact info:
**University email:** GK468@live.mdx.ac.uk\
**Personal:** geraldaskastauna@gmail.com
