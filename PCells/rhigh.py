#
# Import the db 
#
from ui import *
#
# The entry point
#
def rhigh(cv, r=1.36e3, w=0.5e-6, l=0.5e-6, calculate=["L", "R"]) :
    lib = cv.lib()
    tech = lib.tech()
    dbu = lib.dbuPerUU()
    res = int(r * dbu)
    width = max(int(w * 1e6 * dbu), int(w * 1e9))
    length = max(int(l * 1e6 * dbu), int(l * 1e9))
    if (calculate == "L") :
        res = int(r * dbu)
        length = int(res * width / (1360 * dbu))
        cv.dbReplaceProp("l", 1e-6 * (length / dbu))
    if (calculate == "R") :
        length = int(l * 1.0e6 * dbu)
        res = float(1360 * length / width)
        cv.dbReplaceProp("r", res)
    #
    # Layer rules
    #
    xygrid = int(0.005 * dbu)
    gatpoly_width = int(0.5 * dbu)
    psd_en_gatpoly = int(0.18 * dbu)
    cont_width = int(0.16 * dbu)
    cont_space = int(0.18 * dbu)
    gatpoly_en_cont = int(0.07 * dbu)
    salblock_lenght = int(0.5 * dbu)
    salblock_to_cont = int(0.2 * dbu)
    salblock_ov_gatpoly = int(0.2 * dbu)
    extblock_en_gatpoly = int(0.18 * dbu)
    metal1_en_cont = int(0.065 * dbu)
    #
    # Device rules
    #
    min_width = gatpoly_width
    min_length = salblock_lenght
    #
    # Checking parameters
    #
    if width%xygrid!=0 :
        width = int(xygrid * int(width / xygrid))
        cv.dbReplaceProp("w", 1e-6 * (width / dbu))
        cv.update()
    if length%xygrid!=0 :
        length = int(xygrid * int(length / xygrid))
        cv.dbReplaceProp("l", 1e-6 * (length / dbu))
        cv.update()
    if width < min_width :
        width = min_width
        cv.dbReplaceProp("w", 1e-6 * (width / dbu))
        cv.update()
    if length < length :
        length = min_length
        cv.dbReplaceProp("l", 1e-6 * (length / dbu))
        cv.update()
    #
    # Creating the device
    #
    # Create gatpoly
    layer = tech.getLayerNum("GatPoly", "drawing")
    r = Rect(int(-(salblock_to_cont + cont_width + gatpoly_en_cont)), 0, int(length + salblock_to_cont + cont_width + gatpoly_en_cont), int(width))
    gatpoly = cv.dbCreateRect(r, layer)
    # Create res recognition layer (in this case thats salblock)
    layer = tech.getLayerNum("SalBlock", "drawing")
    r = Rect(0, int(-salblock_ov_gatpoly), int(length), int(width + salblock_ov_gatpoly))
    salblock = cv.dbCreateRect(r, layer)
    # Create pSD implant
    layer = tech.getLayerNum("pSD", "drawing")
    r = Rect(int(-(extblock_en_gatpoly + salblock_to_cont + cont_width + gatpoly_en_cont)), int(-(extblock_en_gatpoly)), int(extblock_en_gatpoly + length + salblock_to_cont + cont_width + gatpoly_en_cont), int(extblock_en_gatpoly + width))
    psd = cv.dbCreateRect(r, layer)
    # Create nSD implant
    layer = tech.getLayerNum("nSD", "drawing")
    r = Rect(int(-(extblock_en_gatpoly + salblock_to_cont + cont_width + gatpoly_en_cont)), int(-(extblock_en_gatpoly)), int(extblock_en_gatpoly + length + salblock_to_cont + cont_width + gatpoly_en_cont), int(extblock_en_gatpoly + width))
    nsd = cv.dbCreateRect(r, layer)
    # Create extblock layer
    layer = tech.getLayerNum("EXTBlock", "drawing")
    r = Rect(int(-(extblock_en_gatpoly + salblock_to_cont + cont_width + gatpoly_en_cont)), int(-(extblock_en_gatpoly)), int(extblock_en_gatpoly + length + salblock_to_cont + cont_width + gatpoly_en_cont), int(extblock_en_gatpoly + width))
    extblock = cv.dbCreateRect(r, layer)
    # Create contacts
    layer = tech.getLayerNum("Cont", "drawing")
    n_cont = int((width - 2 * gatpoly_en_cont + cont_space) / (cont_width + cont_space))
    s_cont = 0
    if (n_cont > 1) :
        s_cont = cont_space
    offset = abs(int((width - (2 * gatpoly_en_cont + n_cont * (cont_width + s_cont) - s_cont)) / 2))
    if offset%xygrid!=0 :
        offset = int(xygrid * int(offset / xygrid))
    for n in range(n_cont) :
        r = Rect(int(-(salblock_to_cont + cont_width)), int(gatpoly_en_cont + offset + n * (cont_width + s_cont)), int(-salblock_to_cont), int(gatpoly_en_cont + offset + cont_width + n * (cont_width + s_cont)))
        cont = cv.dbCreateRect(r, layer)
        r = Rect(int(length + salblock_to_cont), int(gatpoly_en_cont + n * (cont_width + s_cont) + offset), int(length + salblock_to_cont + cont_width), int(gatpoly_en_cont + offset + cont_width + n * (cont_width + s_cont)))
        cont = cv.dbCreateRect(r, layer)
    # Create metalization over contacts
    layer = tech.getLayerNum("Metal1", "drawing")
    r = Rect(int(-(metal1_en_cont + salblock_to_cont + cont_width)), int(gatpoly_en_cont - metal1_en_cont + offset), int(-salblock_to_cont + metal1_en_cont), int(gatpoly_en_cont + offset + n_cont * (cont_width + s_cont) - s_cont + metal1_en_cont))
    metal1 = cv.dbCreateRect(r, layer)
    net = cv.dbCreateNet("A")
    pin = cv.dbCreatePin("A", net, DB_PIN_INOUT)
    cv.dbCreatePort(pin, metal1)
    r = Rect(int(length + salblock_to_cont - metal1_en_cont), int(gatpoly_en_cont - metal1_en_cont + offset), int(length + salblock_to_cont + cont_width + metal1_en_cont), int(gatpoly_en_cont + offset + n_cont * (cont_width + s_cont) - s_cont + metal1_en_cont))
    metal1 = cv.dbCreateRect(r, layer)
    net = cv.dbCreateNet("B")
    pin = cv.dbCreatePin("B", net, DB_PIN_INOUT)
    cv.dbCreatePort(pin, metal1)
    #
    # Add device type
    #
    cv.dbAddProp("type", "res")
    #
    # Save results
    #
    cv.update()