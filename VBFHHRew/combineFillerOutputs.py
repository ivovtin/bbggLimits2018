import OutputManager as omng
import argparse
import fnmatch
import os
import sys
#import ROOT
from ROOT import *
import os,json
gROOT.SetBatch()
import itertools


# VBF HH Reweighting
# reads from the config the 6 input samples and the target couplings

target_cv  = [1]
target_c2v = [1]
#target_kl  = [-6]
#target_kl  = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_kl  = [-6.0, -5.8, -5.6, -5.4, -5.2, -5.0, -4.8, -4.6, -4.4, -4.2, -4.0, -3.8, -3.6, -3.4, -3.2, -3.0, -2.8, -2.6, -2.4, -2.2, -2.0, -1.8, -1.6, -1.4, -1.2, -1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0, 2.2, 2.4, 2.6, 2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0, 5.2, 5.4, 5.6, 5.8, 6.0, 6.2, 6.4, 6.6, 6.8, 7.0, 7.2, 7.4, 7.6, 7.8, 8.0, 8.2, 8.4, 8.6, 8.8, 9.0, 9.2, 9.4, 9.6, 9.8, 10.0]
target_bf  = 0.0026

#output_VBFHHTo2B2G_CV_0_5_C2V_1_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8.root
#output_VBFHHTo2B2G_CV_1_5_C2V_1_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8.root
#output_VBFHHTo2B2G_CV_1_C2V_1_C3_0_TuneCP5_PSWeights_13TeV-madgraph-pythia8.root
#output_VBFHHTo2B2G_CV_1_C2V_1_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8.root
#output_VBFHHTo2B2G_CV_1_C2V_1_C3_2_TuneCP5_PSWeights_13TeV-madgraph-pythia8.root
#output_VBFHHTo2B2G_CV_1_C2V_2_C3_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8.root

inputSigList = ['VBFHHTo2B2G_CV_1_C2V_1_C3_1', 'VBFHHTo2B2G_CV_1_C2V_1_C3_0', 'VBFHHTo2B2G_CV_1_C2V_1_C3_2', 'VBFHHTo2B2G_CV_1_C2V_2_C3_1', 'VBFHHTo2B2G_CV_1_5_C2V_1_C3_1', 'VBFHHTo2B2G_CV_0_5_C2V_1_C3_1']

omngr = omng.OutputManager()

print "ikL is an integer, a labelling convention used by Lata: ikl = (6+kl)/0.2+1. In the tree the branch with ikl weight shall be named \"KL\",ikl is KL1, KL2, KL80. You can scan kL by steps of 0.2 starting from -6"

omngr.makeVBFrew(inputSigList, target_kl, target_cv, target_c2v, target_bf)

