#
# Initialise boolean package. 
#
from ui import *
ui = cvar.uiptr
cv = ui.getEditCellView()
geomBegin(cv)
lib = cv.lib()
#
# Parasitic capacitance density [F/m2]
#
e0 = 8.854187817e-12
er = 4.1
c0 = e0 * er * 1e6
cmetal1gatpoly      = c0 / 0.460
cmetal1diff         = c0 / 0.620
cmetal2metal1       = c0 / 0.540
cmetal2gatpoly      = c0 / 1.420
cmetal2diff         = c0 / 1.580
cmetal3metal2       = c0 / 0.540
cmetal3metal1       = c0 / 1.570
cmetal3gatpoly      = c0 / 2.450
cmetal3diff         = c0 / 2.610
cmetal4metal3       = c0 / 0.540
cmetal4metal2       = c0 / 1.570
cmetal4metal1       = c0 / 2.600
cmetal4diff         = c0 / 3.640
cmetal4gatpoly      = c0 / 3.480
cmetal5metal4       = c0 / 0.540
cmetal5metal3       = c0 / 1.570
cmetal5metal2       = c0 / 2.600
cmetal5metal1       = c0 / 3.630
cmetal5gatpoly      = c0 / 4.510
cmetal5diff         = c0 / 4.670
ctopmetal1mim       = c0 / 0.660
ctopmetal1metal5    = c0 / 0.850
ctopmetal1metal4    = c0 / 1.880
ctopmetal1metal3    = c0 / 2.910
ctopmetal1metal2    = c0 / 3.940
ctopmetal1metal1    = c0 / 4.970
ctopmetal1gatpoly   = c0 / 5.850
ctopmetal1diff      = c0 / 6.010
ctopmetal2topmetal1 = c0 / 2.800
ctopmetal2mim       = c0 / 5.460
ctopmetal2metal5    = c0 / 5.650
ctopmetal2metal4    = c0 / 6.680
ctopmetal2metal3    = c0 / 7.710
ctopmetal2metal2    = c0 / 8.740
ctopmetal2metal1    = c0 / 9.770
ctopmetal2gatpoly   = c0 / 10.650
ctopmetal2diff      = c0 / 10.810
#
# Loading raw layers
#
nwell            = geomGetShapes("NWell", "drawing")
pwell_block      = geomGetShapes("PWell", "block")
nbulay           = geomGetShapes("nBuLay", "drawing")
nbulay_block     = geomGetShapes("nBuLay", "block")
activ            = geomGetShapes("Activ", "drawing")
thickgateox      = geomGetShapes("ThickGateOx", "drawing")
gatpoly          = geomGetShapes("GatPoly", "drawing")
psd              = geomGetShapes("pSD", "drawing")
nsd              = geomGetShapes("nSD", "drawing")
nsd_block        = geomGetShapes("nSD", "block")
extblock         = geomGetShapes("EXTBlock", "drawing")
salblcok         = geomGetShapes("SalBlock", "drawing")
cont             = geomGetShapes("Cont", "drawing")
metal1           = geomGetShapes("Metal1", "drawing")
metal2           = geomGetShapes("Metal2", "drawing")
metal3           = geomGetShapes("Metal3", "drawing")
metal4           = geomGetShapes("Metal4", "drawing")
metal5           = geomGetShapes("Metal5", "drawing")
topmetal1        = geomGetShapes("TopMetal1", "drawing")
topmetal2        = geomGetShapes("TopMetal2", "drawing")
via1             = geomGetShapes("Via1", "drawing")
via2             = geomGetShapes("Via2", "drawing")
via3             = geomGetShapes("Via3", "drawing")
via4             = geomGetShapes("Via4", "drawing")
topvia1          = geomGetShapes("TopVia1", "drawing")
topvia2          = geomGetShapes("TopVia2", "drawing")
passiv_sbump     = geomGetShapes("Passiv", "sbump")
passiv_pillar    = geomGetShapes("Passiv", "pillar")
passiv           = geomGetShapes("Passiv", "drawing")
dpad             = geomGetShapes("dfpad", "drawing")
pwell            = geomGetShapes("PWell", "drawing")
trans            = geomGetShapes("TRANS", "drawing")
res              = geomGetShapes("RES", "drawing")
edgeseal         = geomGetShapes("EdgeSeal", "drawing")
mim              = geomGetShapes("MIM", "drawing")
#
# Forming derived layers
#
pwell       = geomOr(geomNot(geomOr(nwell, pwell_block)), pwell)
nbl         = geomAndNot(geomOr(geomSize(geomSize(nwell, -1.495), 0.495), nbulay), nbulay_block)
nres        = geomAnd(res, gatpoly)
pres        = geomAnd(geomAnd(gatpoly, salblcok), geomAndNot(psd, nsd))
pnres       = geomAnd(geomAnd(gatpoly, salblcok), geomAnd(psd, nsd))
poly        = geomAndNot(gatpoly, geomOr(nres, geomOr(pres, pnres)))
gate        = geomAnd(activ, poly)
diff        = geomAndNot(activ, poly)
ndiff       = geomAnd(diff, geomOr(nsd, geomNot(geomOr(psd, nsd_block))))
pdiff       = geomAnd(diff, psd)
nactiv      = geomAnd(activ, geomOr(nsd, geomNot(geomOr(psd, nsd_block))))
pactiv      = geomAnd(activ, psd)
thickpdiff  = geomAnd(thickgateox, pdiff)
thickndiff  = geomAnd(thickgateox, ndiff)
ntap        = geomAnd(nwell, ndiff)
ptap        = geomAnd(pwell, pdiff)
thickntap   = geomAnd(thickgateox, ntap)
thickptap   = geomAnd(thickgateox, ptap)
nfet        = geomAndNot(geomAnd(nactiv, gate), thickgateox)
pfet        = geomAndNot(geomAnd(nwell, geomAnd(pactiv, gate)), thickgateox)
hvnfet      = geomAnd(geomAnd(nactiv, gate), thickgateox)
hvpfet      = geomAnd(geomAnd(nwell, geomAnd(pactiv, gate)), thickgateox)
pntap       = geomAnd(pdiff, nwell)
ncon        = geomAnd(nbl, nwell)
infet       = geomContains(geomContains(nbl, pwell), nfet)
hvinfet     = geomContains(geomContains(nbl, pwell), hvnfet)
cntbx       = geomSize(geomSize(cont, -0.08, horizontal), 0.08, horizontal)
cntby       = geomSize(geomSize(cont, -0.08, vertical), 0.08, vertical) 
cnt         = geomAndNot(cont, geomOr(cntbx, cntby))
schottky    = geomAnd(geomAnd(geomAnd(geomAnd(nbl, salblcok), nsd_block), pwell_block), geomOr(cntbx, cntby))
pad         = geomAnd(passiv, geomAnd(passiv_sbump, geomAnd(passiv_pillar, dpad)))
sbumppad    = geomAndNot(geomAnd(passiv_sbump, dpad), geomOr(passiv, passiv_pillar))
cupillarpad = geomAndNot(geomAnd(passiv_pillar, dpad), geomOr(passiv, passiv_sbump))
mimcap      = geomAnd(mim, metal5)
ndio        = geomAnd(ndiff, geomAnd(extblock, pwell))
pdio        = geomAnd(pdiff, geomAnd(extblock, nwell))
#
# Extracting pin and net names before geomConnect
#
geomLabel(activ, "Activ", "pin")
geomLabel(activ, "Activ", "net", False)
geomLabel(poly, "GatPoly", "pin")
geomLabel(poly, "GatPoly", "net", False)
geomLabel(nwell, "NWell", "pin")
geomLabel(nwell, "NWell", "net", False)
geomLabel(nbl, "nBuLay", "pin")
geomLabel(nbl, "nBuLay", "net", False)
geomLabel(metal1, "Metal1", "pin")
geomLabel(metal1, "Metal1", "net", False)
geomLabel(metal2, "Metal2", "pin")
geomLabel(metal2, "Metal2", "net", False)
geomLabel(metal3, "Metal3", "pin")
geomLabel(metal3, "Metal3", "net", False)
geomLabel(metal4, "Metal4", "pin")
geomLabel(metal4, "Metal4", "net", False)
geomLabel(metal5, "Metal5", "pin")
geomLabel(metal5, "Metal5", "net", False)
geomLabel(topmetal1, "TopMetal1", "pin")
geomLabel(topmetal1, "TopMetal1", "net", False)
geomLabel(topmetal2, "TopMetal2", "pin")
geomLabel(topmetal2, "TopMetal2", "net", False)
geomLabel(passiv, "Passiv", "pin")
geomLabel(passiv, "Passiv", "net", False)
#
# Forming connectivity.
#
print("Forming connectivity")
geomConnect([
            [ncon, nbl, nwell],
            [ntap, nwell, ndiff],
            [ptap, pwell, pdiff],
            [cont, ndiff, pdiff, poly, metal1],
            [via1, metal1, metal2],
            [via2, metal2, metal3],
            [via3, metal3, metal4],
            [via4, metal4, metal5],
            [topvia1, metal5, mim, topmetal1],
            [topvia2, topmetal1, topmetal2]])
#
# Saving interconnections
#
print("Saving interconnections")
saveInterconnect([[nbl, "nBuLay"],
                  nwell,
                  [pwell, "PWell"],
                  [ndiff, "Activ"],
                  [pdiff, "Activ"],
                  [ntap, "Activ"],
                  [ptap, "Activ"],
                  [poly, "GatPoly"],
                  cont,
                  metal1,
                  via1,
                  metal2,
                  via2,
                  metal3,
                  via3,
                  metal4,
                  via4,
                  metal5,
                  mim,
                  topvia1,
                  topmetal1,
                  topvia2,
                  topmetal2])
#
print("Extracting MOSFETs")
if geomNumShapes(nfet) > 0 :
    extractMOS("nmos_ex", nfet, poly, ndiff, pwell)
if geomNumShapes(pfet) > 0 :
    extractMOS("pmos_ex", pfet, poly, pdiff, nwell)
if geomNumShapes(hvnfet) > 0 :
    extractMOS("nmosHV_ex", hvnfet, poly, ndiff, pwell)
if geomNumShapes(hvpfet) > 0 :
    extractMOS("pmosHV_ex", hvpfet, poly, pdiff, nwell)
#
print("Extracting Resistors")
if geomNumShapes(nres) > 0 :
    extractRes("rsil_ex", nres, poly)
if geomNumShapes(pres) > 0 :
    extractRes("rppd_ex", pres, poly)
if geomNumShapes(pnres) > 0 :
    extractRes("rhigh_ex", pnres, poly)
#
print("Extracting Capacitors")
if geomNumShapes(mimcap) > 0 :
    extractDevice("cmim_ex", mimcap, [[mim, "T"], [metal5, "B"]])
#
print("Extracting Diodes")
if geomNumShapes(ndio) > 0 :
    extractDio("dantenna_ex", ndio, pwell, ndiff)
if geomNumShapes(pdio) > 0 :
    extractDio("dpantenna_ex", pdio, pdiff, nwell)
#
# Extracting parasitics
#
print("Extracting Metal1 parasitic caps")
extractParasitic2(poly, metal1, cmetal1gatpoly, 0.0)
extractParasitic2(ndiff, metal1, cmetal1diff, 0.0)
extractParasitic2(pdiff, metal1, cmetal1diff, 0.0)
extractParasitic3(nwell, metal1, cmetal1diff, 0.0, [poly, ndiff, pdiff])
extractParasitic3(pwell, metal1, cmetal1diff, 0.0, [poly, ndiff, pdiff])
#
print("Extracting Metal2 parasitic caps")
extractParasitic2(metal1, metal2, cmetal2metal1, 0.0)
extractParasitic3(poly, metal2, cmetal2gatpoly, 0.0, [metal1])
extractParasitic3(ndiff, metal2, cmetal2diff, 0.0, [metal1])
extractParasitic3(pdiff, metal2, cmetal2diff, 0.0, [metal1])
extractParasitic3(nwell, metal2, cmetal2diff, 0.0, [metal1, poly, ndiff, pdiff])
extractParasitic3(pwell, metal2, cmetal2diff, 0.0, [metal1, poly, ndiff, pdiff])
#
print("Extracting Metal3 parasitic caps")
extractParasitic2(metal2, metal3, cmetal3metal2, 0.0)
extractParasitic3(metal1, metal3, cmetal3metal1, 0.0, [metal2])
extractParasitic3(poly, metal3, cmetal3gatpoly, 0.0, [metal2, metal1])
extractParasitic3(ndiff, metal3, cmetal3diff, 0.0, [metal2, metal1])
extractParasitic3(pdiff, metal3, cmetal3diff, 0.0, [metal2, metal1])
extractParasitic3(nwell, metal3, cmetal3diff, 0.0, [metal2, metal1, poly, ndiff, pdiff])
extractParasitic3(pwell, metal3, cmetal3diff, 0.0, [metal2, metal1, poly, ndiff, pdiff])
#
print("Extracting Metal4 parasitic caps")
extractParasitic2(metal3, metal4, cmetal4metal3, 0.0)
extractParasitic3(metal2, metal4, cmetal4metal2, 0.0, [metal3])
extractParasitic3(metal1, metal4, cmetal4metal1, 0.0, [metal3, metal2])
extractParasitic3(poly, metal4, cmetal4gatpoly, 0.0, [metal3, metal2, metal1])
extractParasitic3(ndiff, metal4, cmetal4diff, 0.0, [metal3, metal2, metal1])
extractParasitic3(pdiff, metal4, cmetal4diff, 0.0, [metal3, metal2, metal1])
extractParasitic3(nwell, metal4, cmetal4diff, 0.0, [metal3, metal2, metal1, poly, ndiff, pdiff])
extractParasitic3(pwell, metal4, cmetal4diff, 0.0, [metal3, metal2, metal1, poly, ndiff, pdiff])
#
print("Extracting Metal5 parasitic caps")
extractParasitic2(metal4, metal5, cmetal5metal4, 0.0)
extractParasitic3(metal3, metal5, cmetal5metal3, 0.0, [metal4])
extractParasitic3(metal2, metal5, cmetal5metal2, 0.0, [metal4, metal3])
extractParasitic3(metal1, metal5, cmetal5metal1, 0.0, [metal4, metal3, metal2])
extractParasitic3(poly, metal5, cmetal5gatpoly, 0.0, [metal4, metal3, metal2, metal1])
extractParasitic3(ndiff, metal5, cmetal5diff, 0.0, [metal4, metal3, metal2, metal1])
extractParasitic3(pdiff, metal5, cmetal5diff, 0.0, [metal4, metal3, metal2, metal1])
extractParasitic3(nwell, metal5, cmetal5diff, 0.0, [metal4, metal3, metal2, metal1, poly, ndiff, pdiff])
extractParasitic3(pwell, metal5, cmetal5diff, 0.0, [metal4, metal3, metal2, metal1, poly, ndiff, pdiff])
#
print("Extracting TopMetal1 parasitic caps")
extractParasitic2(mim, topmetal1, ctopmetal1mim, 0.0)
extractParasitic3(metal5, topmetal1, ctopmetal1metal5, 0.0, [mim])
extractParasitic3(metal4, topmetal1, ctopmetal1metal4, 0.0, [mim, metal5])
extractParasitic3(metal3, topmetal1, ctopmetal1metal3, 0.0, [mim, metal5, metal4])
extractParasitic3(metal2, topmetal1, ctopmetal1metal2, 0.0, [mim, metal5, metal4, metal3])
extractParasitic3(metal1, topmetal1, ctopmetal1metal1, 0.0, [mim, metal5, metal4, metal3, metal2])
extractParasitic3(poly, topmetal1, ctopmetal1gatpoly, 0.0, [mim, metal5, metal4, metal3, metal2, metal1])
extractParasitic3(ndiff, topmetal1, ctopmetal1diff, 0.0, [mim, metal5, metal4, metal3, metal2, metal1])
extractParasitic3(pdiff, topmetal1, ctopmetal1diff, 0.0, [mim, metal5, metal4, metal3, metal2, metal1])
extractParasitic3(nwell, topmetal1, ctopmetal1diff, 0.0, [mim, metal5, metal4, metal3, metal2, metal1, poly, ndiff, pdiff])
extractParasitic3(pwell, topmetal1, ctopmetal1diff, 0.0, [mim, metal5, metal4, metal3, metal2, metal1, poly, ndiff, pdiff])
#
print("Extracting TopMetal2 parasitic caps")
extractParasitic2(topmetal1, topmetal2, ctopmetal2topmetal1, 0.0)
extractParasitic3(mim, topmetal2, ctopmetal2mim, 0.0, [topmetal1])
extractParasitic3(metal5, topmetal2, ctopmetal2metal5, 0.0, [topmetal1, mim])
extractParasitic3(metal4, topmetal2, ctopmetal2metal4, 0.0, [topmetal1, mim, metal5])
extractParasitic3(metal3, topmetal2, ctopmetal2metal3, 0.0, [topmetal1, mim, metal5, metal4])
extractParasitic3(metal2, topmetal2, ctopmetal2metal2, 0.0, [topmetal1, mim, metal5, metal4, metal3])
extractParasitic3(metal1, topmetal2, ctopmetal2metal1, 0.0, [topmetal1, mim, metal5, metal4, metal3, metal2])
extractParasitic3(poly, topmetal2, ctopmetal2gatpoly, 0.0, [topmetal1, mim, metal5, metal4, metal3, metal2, metal1])
extractParasitic3(ndiff, topmetal2, ctopmetal2diff, 0.0, [topmetal1, mim, metal5, metal4, metal3, metal2, metal1])
extractParasitic3(pdiff, topmetal2, ctopmetal2diff, 0.0, [topmetal1, mim, metal5, metal4, metal3, metal2, metal1])
extractParasitic3(nwell, topmetal2, ctopmetal2diff, 0.0, [topmetal1, mim, metal5, metal4, metal3, metal2, metal1, poly, ndiff, ndiff])
extractParasitic3(pwell, topmetal2, ctopmetal2diff, 0.0, [topmetal1, mim, metal5, metal4, metal3, metal2, metal1, poly, ndiff, ndiff])
#
#
#
print("End of circuit extraction")
geomEnd()
#
# Reporting results
#
ui.openCellView(lib.libName(), cv.cellName(), "extracted")