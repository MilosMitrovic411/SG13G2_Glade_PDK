#
# Import the db wrappers
#
from ui import *
from math import *
#
# The entry point. The function name *must* match the filename.
#
def rppd_ex(cv, ptlist=[[0,0],[1000,0],[1000,1000],[0,1000]]) :
    lib = cv.lib()
    dbu = lib.dbuPerUU()
    npts = len(ptlist)
    #
    # Create the recognition region shape
    #
    xpts = intarray(npts)
    ypts = intarray(npts)
    for i in range (npts) :
        xpts[i] = ptlist[i][0]
        ypts[i] = ptlist[i][1]
    cv.dbCreatePolygon(xpts, ypts, npts, TECH_Y0_LAYER);
    #
    # Create pins
    #
    plus_net = cv.dbCreateNet("A")
    cv.dbCreatePin("A", plus_net, DB_PIN_INPUT)
    minus_net = cv.dbCreateNet("B")
    cv.dbCreatePin("B", minus_net, DB_PIN_INPUT)
    #
    # Set the device modelName property for netlisting
    #
    cv.dbAddProp("modelName", "rppd")
    #
    # Set the netlisting property
    #
    cv.dbAddProp("NLPDeviceFormat", "[@instName] [|A:%] [|B:%] [@modelName] [@w:w=%u] [@l:l=%u]")
    cv.dbAddProp("NLPDeviceFormatCDL", "x[@instName] [|A:%] [|B:%] [@modelName] [@w:w=%u] [@l:l=%u]")
    #
    # Device type
    cv.dbAddProp("type", "res")
    #
    # Commit to db the bounding box
    #
    cv.update()