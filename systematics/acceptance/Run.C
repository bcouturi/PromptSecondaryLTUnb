#include <iostream>

#include "TFile.h"
#include "TTree.h"

void Run() {

  //std::string filename = "/data/Phys/data/mcd02kpi_tracks9_merged.root";
  std::string filename = "/data/Phys/data/mcd02kpi_tracks10_merged.root";
  bool fileNotFound = gSystem->AccessPathName(filename.c_str());
  // if local file is not found use the EOS version
  if (fileNotFound) {
    //filename = "root://eoslhcb.cern.ch//eos/lhcb/user/m/malexand/d2hh/secondariesTagging/mcd02kpi_tracks9_merged.root";
    filename = "root://eoslhcb.cern.ch//eos/lhcb/user/l/lben/27163003tag/mcd02kpi_tracks10_merged.root";
   }
  
  TFile * f = TFile::Open(filename.c_str());
  TTree *tree = (TTree *)f->Get("TrackFilter/DecayTree");
  if (tree == nullptr) {
    tree = (TTree *)f->Get("DecayTree");
  }
  std::cout << "Nb Entries in tree:" << tree->GetEntries() << std::endl;
  tree->Process("RadialSelector.C", "");
  f->Close();

}
