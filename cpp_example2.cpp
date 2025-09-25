// This code may be compiled to make a stand alone exe
// or it can be run from the ROOT command line as:

// root [0] .L cpp_example.cpp  or .L cpp_example.cpp+
// root [1] cpp_example

#include "TApplication.h"
#include "TROOT.h"
#include "TH1F.h"
#include "TF1.h"
#include "TCanvas.h"
#include "TStyle.h"
#include "TRandom3.h"
#include <TH2D.h>
#include <TStyle.h> 
#include <iostream> 
//#include <cstdlib>
//#include <cmath>
//#include <iostream>

using namespace std;
using namespace ROOT::Math;


// examples of various plots in C++ program
void cpp_example(int samples=10000){
  // gStyle->SetOptStat(0);  // turn off default stats box in histograms

  TRandom3 rand; 

  auto c = new TCanvas("c", "canv", 1600, 800); 
  c->Divide(2,2); 

  gStyle->SetOptStat(0); 

  const double min{50.}, max{150.}, sigma{6.}, mean{100.}; 

  //random, gaussian dist
  auto hist2d = new TH2D("h1", "random gauss;x;y", 100, min,max, 100, min,max); 
  for (int i=0; i<samples; i++) {
    hist2d->Fill(rand.Gaus()*sigma + mean, rand.Gaus()*sigma + mean); 
  }
  c->cd(1); 
  hist2d->Draw("col"); 

  //hist2d with offset 
  auto hist2d_offset = (TH2D*)hist2d->Clone("h2"); 
  for (int i=0; i<samples; i++) {
    hist2d_offset->Fill(min + (max-min)*rand.Rndm(), min + (max-min)*rand.Rndm()); 
  }
  hist2d_offset->SetTitle("gauss + offset;x;y"); 
  c->cd(2); 
  hist2d_offset->Draw("col"); 

  //hist2d with 1/xx background 
  auto hist2d_1xx = (TH2D*)hist2d->Clone("h3"); 
  for (int i=0; i<samples*4; i++) {
    hist2d_1xx->Fill( 
      pow( (1./min) - ((1./min) - (1./max))*rand.Rndm(), -1 ),
      pow( (1./min) - ((1./min) - (1./max))*rand.Rndm(), -1 )
    ); 
  }
  hist2d_1xx->SetTitle("gauss + 1/x^{2} background;x;y"); 
  c->cd(3); 
  hist2d_1xx->Draw("col"); 

  //hist2d with 'dilute' hist background 
  auto hist2d_double = (TH2D*)hist2d->Clone("h4"); 
  for (int i=0; i<samples; i++) {
    hist2d_double->Fill( 
      rand.Gaus() * sigma * 4 + mean,
      rand.Gaus() * sigma * 4 + mean
    ); 
  }
  hist2d_double->SetTitle("gauss + 4*#sigma background;x;y"); 
  c->cd(4); 
  hist2d_double->Draw("col"); 

  c->SaveAs("canvas2d_2.png"); 

  auto c2 = new TCanvas("c2"); 
  hist2d->Draw("col"); 
  c2->SaveAs("canvas2d_1.png"); 

  return; 
}

int main(int argc, char **argv) {
  int nsamples=10000;  // set sample sizes

  if (argc>1) nsamples=atoi(argv[1]);
  
  cout << "making plots..." << flush; 
  cpp_example(nsamples);
  cout << "done." << endl; 

  return 0;
}
  
