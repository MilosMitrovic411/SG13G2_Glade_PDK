#
# Initialise boolean package. 
#
from ui import *
ui = cvar.uiptr
cv = ui.getEditCellView()
geomBegin(cv)
lib = cv.lib()
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
#extractDevice("isolbox", recLayer, [[termLayer1, term1Name, ...] [termLayer2, term2Name, ...]] 
#
print("End of circuit extraction")
geomEnd()
#
# Reporting results
#
cv_ex = lib.dbFindCellViewByName(cv.cellName(), "extracted")
box = cv_ex.bBox()
objs = cv_ex.dbGetOverlaps(box, 0, True, True, True)
obj = objs.first()
num_dev = 0
while obj :
    if obj.isInst() :
        num_dev = num_dev + 1
    obj = objs.next()
print("Total device count = ", num_dev)
ui.openCellView(lib.libName(), cv.cellName(), "extracted")