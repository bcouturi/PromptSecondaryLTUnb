#
# Exctraction script for MC d02Kpi
#

script   = 'mcfindtracksFinal.py'

def make_template(script, name = "MCFT07", gridOutput = True) :
    t = JobTemplate( application = Bender( version = "v25r3", module = script ))
    t.name = name
    bkquery = BKQuery('/MC/2011/Beam3500GeV-2011-MagDown-Nu2-EmNoCuts/Sim05/Trig0x40760037Flagged/Reco12a/Stripping17NoPrescalingFlagged/27163003/ALLSTREAMS.DST')
    datafiles = bkquery.getDataset()
    t.inputdata = datafiles

    t.splitter=SplitByFiles(filesPerJob=10, ignoremissing=False, maxFiles=None)
    NTUPLE_NAME = "mcd02kpi_tracks_ntuple.root"
    if gridOutput :
        ntuple = DiracFile(NTUPLE_NAME)
        histo = DiracFile("mcd02kpi_tracks_histo.root")
    else :
        ntuple = LocalFile(NTUPLE_NAME)
        histo = LocalFile("mcd02kpi_tracks_histo.root")
        
    t.outputfiles = [ntuple, histo] 

    return t

def make_job(script, name = "MCFT07", gridOutput = True) :
    if not gridOutput :
        name += 'Local'
    try :
        t = templates[name]
    except :
        t = make_template(script, name, gridOutput)

    j = Job( t, backend = Dirac() )
    #j = Job( t, backend = Local() )


    return j
