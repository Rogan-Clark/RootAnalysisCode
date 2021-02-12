#Takes a THist stored in a ROOT file and prints the resutl as a png for display purposes

import ROOT
import os

#GetKeyNames allows looping over all objects in a ROOT file, printing the names as a list. GodTier ROOT function.

def GetKeyNames(self):
    return [name.GetName() for name in self.GetListOfKeys()]

ROOT.TFile.GetKeyNames = GetKeyNames                 #Slight renaming here - important
ROOT.gStyle.SetOptStat(1000000001)                   #Sets style of statistics box
DIR="."                             #Directory containing THist files
for file in os.listdir(DIR):
    if file.endswith(".root"):
        FileName=ROOT.TFile.Open(DIR+"/"+file)
        HistName=FileName.GetKeyNames()
        print(FileName)
        print(HistName[0])                           #If the file contains multiple THists, loop over here incrementing HistName[i]
        h=FileName.Get(HistName[0])
        canv=ROOT.TCanvas()
        h.Draw("COLZ")
        canv.SaveAs(HistName[0]+".png")
        FileName.Close()

