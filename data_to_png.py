#Takes raw root data stored in leaves, prints it to a histogram, which is then saved as an image
#Doesn't work if aren't able to display images on the machine - consider storing the histograms as root files for later?
import os
import ROOT
ROOT.gStyle.SetOptStat(1000000001)                         #Hides the statistics box, change the value if you want to know mean, std, etc
for year in range(2015,2016,1):                       #Loop over whatever directories contain the data
    for month in range(1,3,1):
        month=str(month).zfill(2)
        Descriptor=month+"_"+str(year)
        canv=ROOT.TCanvas()
        h=ROOT.TH2F(Descriptor, "Successful HistogDram Plot", XBins,XMin,XMax,YBins,YMin,YMax)
        h.GetXaxis().SetTitle("XTitle")
        h.GetYaxis().SetTitle("YTitle")
        DIR=str(year)+"/"+month                       #MODIFY FOR NEW DIRECTORIES
        for filename in os.listdir(DIR):              #Loop over necessary directories here
            if filename.endswith(".root"):
                print(filename)
                f=ROOT.TFile.Open(DIR+"/"+filename)
                for evt in f.Tree0:
                    h.Fill(evt.xaxis, evt.yaxis)      #Change xaxis and yaxis for whatever variables you want to plot
                f.Close()
        h.Draw("COLZ")                                #COLZ gives a colour density plot, feel free to change to what is most appropriate
        canv.SaveAs(Descriptor+".png")                 

