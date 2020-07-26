"""
FILES IN PACKAGE:
snn-stdp.py
get-networks-accuracy.py
read-pkl-spikes.py
iris-train.txt
iris-test.txt
README.md

Files generated after training:
results/input.pkl
results/output.pkl

Files generated after testing:
results/inputTest.pkl
results/outputTest.pkl

Author: Geraldas Kastauna
Supervisor: Professor Dr. Chris Huyck (https://www.cwa.mdx.ac.uk/chris/chrisroot.html)
Email: GK468@live.mdx.ac.uk OR geraldaskastauna@gmail.com

Middlesex University, London Campus
Undergradute Student of Computer Science BSc

Thesis: 'Learing with Spiking Neural Network'

About this program:
This program lets user see the spike trains that were generated by snn-stdp.py
program during training and testing. It prints the neuron number and
all its spike timings.
"""

# === Dependencies ===
import _pickle as pickle

# === Traininig files ===
TRAINING_INPUT_SPIKES_FILE = 'results/input.pkl'
TRAINING_OUTPUT_SPIKES_FILE = 'results/output.pkl'

# === Testing files ===
TESTING_INPUT_SPIKES_FILE = 'results/inputTest.pkl'
TESTING_OUTPUT_SPIKES_FILE = 'results/outputTest.pkl'

"""
Functions that prints neuron number and its spike sequence
from .pkl file to console
Parameters: file name (string)
"""
def print_pkl_spikes(fileName):
        fileHandler = open(fileName, 'rb') # Opens a file for reading only in binary format
        neoObject = pickle.load(fileHandler, encoding = 'utf8') 
        segments = neoObject.segments
        segment = segments[0]
        spikeSequence = segment.spiketrains
        neurons = len(spikeSequence)

        # Loop through active neurons
        for neuronNum in range (0,neurons):
            if (len(spikeSequence[neuronNum])>0):
                spikes = spikeSequence[neuronNum]
                for spike in range (0,len(spikes)):
                    print (neuronNum, spikes[spike])
        fileHandler.close()

# === Main ===
# Delete or add # (hastag) infront of the line to print neuron and spike times to console

# === Training files ===
#print_pkl_spikes(TRAINING_INPUT_SPIKES_FILE)
#print_pkl_spikes(TRAINING_OUTPUT_SPIKES_FILE)
    
# === Testing files ===
#print_pkl_spikes(TESTING_INPUT_SPIKES_FILE)
print_pkl_spikes(TESTING_OUTPUT_SPIKES_FILE)

# === End of program ===