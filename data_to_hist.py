#Takes raw data stored in TTree format, and saves as a histogram in a root file as a THist
#Edit year and month loops for whatever specifies to directories of the stored data
#Descriptor assigns the object name of the histogram, change to whatever is indicative of the data
import os
import ROOT
for year in range(2015,2016,1):
    for month in range(1,4,1):
        month=str(month).zfill(2)
        Descriptor=month+"_"+str(year)
        h=ROOT.TH2F(Descriptor, "Histogram Title", XBins,Xmin,Xmax,Ybins,Ymin,Ymax)  #Set Parameters of new histogram
        h.GetXaxis().SetTitle("XAxis Label")
        h.GetYaxis().SetTitle("YAxis Label")
        DIR=str(year)+"/"+month   #Modify here for new directories to be looped over
        for filename in os.listdir(DIR):
            if filename.endswith(".root"):
                print(filename)
                f=ROOT.TFile.Open(DIR+"/"+filename)
                for evt in f.Tree0:
                    h.Fill(evt.xdata, evt.ydata) #Fill histogram with data from the event leaves
                f.Close()
        NewHist=ROOT.TFile(Descriptor+"_title.root", "RECREATE")    #Save the histogram to a new root file, named here
        h.Write()
        NewHist.Close()

#Possible modifications
#Could use same in the .Draw option if filling resets with each file? This allows multple hists to be plotted on one TCanvas.
# Or maybe total_hist.Add(indvidual_hist) ?? then plot total_hist where Total_Hist=ROOT.THStack("objectname", "Title"). This creates a master histogram and saves onto that
