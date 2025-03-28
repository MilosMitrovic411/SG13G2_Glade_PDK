#
# Import the db wrappers
#
from ui import *
#
# The entry point. The function name *must* match the filename.
#
def nmos_ex(cv, ptlist=[[0,0],[1000,0],[1000,1000],[0,1000]]) :
    lib = cv.lib()
    dbu = lib.dbuPerUU()
    #
    # Create the recognition region shape
    #
    npts = len(ptlist)
    xpts = intarray(npts)
    ypts = intarray(npts)
    for i in range (npts) :
        xpts[i] = ptlist[i][0]
        ypts[i] = ptlist[i][1]
    cv.dbCreatePolygon(xpts, ypts, npts, TECH_Y0_LAYER);
    #
    # Create pins
    #
    gate_net = cv.dbCreateNet("G")
    cv.dbCreatePin("G", gate_net, DB_PIN_INPUT)
    source_net = cv.dbCreateNet("S")
    cv.dbCreatePin("S", source_net, DB_PIN_INOUT)
    drain_net = cv.dbCreateNet("D")
    cv.dbCreatePin("D", drain_net, DB_PIN_INOUT)
    bulk_net = cv.dbCreateNet("B")
    cv.dbCreatePin("B", bulk_net, DB_PIN_INPUT)
    #
    # Set the device modelName property for netlisting
    #
    cv.dbAddProp("modelName", "sg13_lv_nmos")
    #
    # Set the netlisting property
    #
    cv.dbAddProp("NLPDeviceFormat", "[@instName] [|D:%] [|G:%] [|S:%] [|B:%] [@modelName] [@w:w=%] [@l:l=%] [@as:as=%] [@ps:ps=%] [@ad:ad=%] [@pd:pd=%] [@m:m=%]")
    cv.dbAddProp("NLPDeviceFormatCDL", "x[@instName] [|D:%] [|G:%] [|S:%] [|B:%] [@modelName] [@w:w=%] [@l:l=%] [@as:as=%] [@ps:ps=%] [@ad:ad=%] [@pd:pd=%] [@m:m=%]")
    #
    # Device type
    #
    cv.dbAddProp("type", "mos")
    #
    # Update the bounding box
    #
    cv.update()