from math import *
import pandas as pd
import numpy as np
import glob
import control
from matplotlib import pyplot as plt
from AutoGenMR.feature_extraction.spectral_math_tools import *
from AutoGenMR.feature_extraction.multitaper import Multitaper
from AutoGenMR.feature_extraction.PowerSpectrumFeatures import PowerSpectrumFeatures
from AutoGenMR.feature_extraction.SpectrogramFeatures import SpectrogramFeatures
from AutoGenMR.feature_extraction.BispectrogramFeatures import BispectrogramFeatures
#from spectrum import pmtm
#import numpy

#*******************************************************************************
# Função para carregar arquivo
def load_ts_txt(file_name):
    lines = []

    with open(file_name, "r") as text_file:
        lines = text_file.readlines()
        lines = list(map(int, lines))

    return lines


#*******************************************************************************
# Função converter array para lista de strings
def array_2_str_list(arranjo):
    l = []

    for i in range(0, len(arranjo)):
        l.append(str(arranjo[i]))

    return l


#*******************************************************************************
path_dataset = ""

#normal olhos abertos
n1_path = path_dataset + "Z/Z040.txt"

#normal olhos fechados
n2_path = path_dataset + "O/O040.txt"

#interictal
in_path = path_dataset + "F/F075.txt"

#ictal
ic_path = path_dataset + "S/S027.txt"

# Spectral parameters
time = 23.6
seg_size = 4097
Fs = 173.61 #frequency sample

#time = 11.5 #time length of each EEG segment
lowFreq = 0 #lowest frequency
highFreq = 80.0 #highest frequency
nw = 10 #
w = 512 # window size
#seg_size = 2000 # EEG segment length

normal1 = np.asarray(load_ts_txt(n1_path))
normal2 = np.asarray(load_ts_txt(n2_path))
interictal = np.asarray(load_ts_txt(in_path))
ictal = np.asarray(load_ts_txt(ic_path))

mtN1 = Multitaper(normal1, frequency_sample = Fs, nw = nw)
mtN2 = Multitaper(normal2, frequency_sample = Fs, nw = nw)
mtIn = Multitaper(interictal, frequency_sample = Fs, nw = nw)
mtIc = Multitaper(ictal, frequency_sample = Fs, nw = nw)

sgN1 = mtN1.get_spectrogram()
sgN2 = mtN2.get_spectrogram()
sgIn = mtIn.get_spectrogram()
sgIc = mtIc.get_spectrogram()

df = (Fs)/len(sgN2)
sfreqs = np.arange(0, Fs, df)
sfreqs = sfreqs[sfreqs <= 80]

sgN1 = 10 * np.log10(sgN1[0 : len(sfreqs)])
sgN2 = 10 * np.log10(sgN2[0 : len(sfreqs)])
sgIn = 10 * np.log10(sgIn[0 : len(sfreqs)])
sgIc = 10 * np.log10(sgIc[0 : len(sfreqs)])

#sgN1 = sgN1[0 : len(sfreqs)]
#sgN2 = sgN2[0 : len(sfreqs)]
#sgIn = sgIn[0 : len(sfreqs)]
#sgIc = sgIc[0 : len(sfreqs)]

z_min = min([sgN1.min(), sgN2.min(), sgIn.min(), sgIc.min()])
z_max = max([sgN1.max(), sgN2.max(), sgIn.max(), sgIc.max()])

t2 = (len(sgN2[0]) * time) / seg_size


fig, (ax1, ax2) = plt.subplots(ncols=2)

pcm1 = ax1.pcolormesh(np.arange(0, t2, t2 / len(sgN1[0])), sfreqs, sgIn, vmin = z_min, vmax = z_max)
ax1.legend(title = "Interictal", loc = 1, fontsize=12)
ax1.set_ylabel("Frequency (Hz)", fontsize=14, fontweight='bold', labelpad=10)
ax1.set_xlabel("Time (s)", fontsize=14, fontweight='bold', labelpad=14)

barra2 = fig.colorbar(pcm1, ax = ax1)

pcm2 = ax2.pcolormesh(np.arange(0, t2, t2 / len(sgN1[0])), sfreqs, sgIc, vmin = z_min, vmax = z_max)
ax2.legend(title = "Ictal", loc = 1, fontsize=12)

barra2 = fig.colorbar(pcm2, ax = ax2)
barra2.set_label("Power (dB)", fontsize=14, fontweight='bold', labelpad=10)
fig.set_size_inches((12, 7), forward=False)
plt.savefig("/home/jefferson/Dropbox/Papers/Artigos Doutorado/Em Andamento - [Doutorado]/BSPC/abnormal_spectrograms.png", dpi=300, bbox_inches='tight')
plt.close(fig)


fig, (ax1, ax2) = plt.subplots(ncols=2)

pcm1 = ax1.pcolormesh(np.arange(0, t2, t2 / len(sgN1[0])), sfreqs, sgN1, vmin = z_min, vmax = z_max)
ax1.legend(title = "Normal (open eyes)", loc = 1, fontsize=12)
ax1.set_ylabel("Frequency (Hz)", fontsize=14, fontweight='bold', labelpad=10)
ax1.set_xlabel("Time (s)", fontsize=14, fontweight='bold', labelpad=14)

barra2 = fig.colorbar(pcm1, ax = ax1)

pcm2 = ax2.pcolormesh(np.arange(0, t2, t2 / len(sgN1[0])), sfreqs, sgN2, vmin = z_min, vmax = z_max)
ax2.legend(title = "Normal (closed eyes)", loc = 1, fontsize=12)

barra2 = fig.colorbar(pcm2, ax = ax2)
barra2.set_label("Power (dB)", fontsize=14, fontweight='bold', labelpad=10)
fig.set_size_inches((12, 7), forward=False)
plt.savefig("/home/jefferson/Dropbox/Papers/Artigos Doutorado/Em Andamento - [Doutorado]/BSPC/normal_spectrograms.png", dpi=300, bbox_inches='tight')
plt.close(fig)
