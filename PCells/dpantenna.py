#
# Import the db 
#
from ui import *
#
# The entry point
#
def dpantenna(cv) :
    lib = cv.lib()
    tech = lib.tech()
    dbu = lib.dbuPerUU()
    #
    # Layer rules
    #
    xygrid = int(0.005 * dbu)
    activ_en_cont = int(0.14 * dbu)
    cont_width = int(0.16 * dbu)
    cont_space = int(0.18 * dbu)
    extblock_en_gatpoly = int(0.18 * dbu)
    metal1_en_cont = int(0.0 * dbu)
    psd_en_activ = int(0.18 * dbu)
    nwell_en_psd_activ = int(0.31 * dbu)
    #
    # Creating the device
    #
    # Create contacts
    layer = tech.getLayerNum("Cont", "drawing")
    xc01 = 0
    yc01 = 0
    xc11 = int(cont_width)
    yc11 = int(cont_width)
    r = Rect(xc01, yc01, xc11, yc11)
    cont = cv.dbCreateRect(r, layer)
    xc02 = int(cont_width + cont_space)
    yc02 = 0
    xc12 = int(xc02 + cont_width)
    yc12 = int(cont_width)
    r = Rect(xc02, yc02, xc12, yc12)
    cont = cv.dbCreateRect(r, layer)
    xc03 = 0
    yc03 = int(cont_width + cont_space)
    xc13 = int(cont_width)
    yc13 = int(yc03 + cont_width)
    r = Rect(xc03, yc03, xc13, yc13)
    cont = cv.dbCreateRect(r, layer)
    xc04 = int(cont_width + cont_space)
    yc04 = int(cont_width + cont_space)
    xc14 = int(xc04 + cont_width)
    yc14 = int(yc04 + cont_width)
    r = Rect(xc04, yc04, xc14, yc14)
    cont = cv.dbCreateRect(r, layer)
    # Create activ
    layer = tech.getLayerNum("Activ", "drawing")
    xa0 = int(-activ_en_cont)
    ya0 = int(-activ_en_cont)
    xa1 = int(xc14 + activ_en_cont)
    ya1 = int(yc14 + activ_en_cont)
    r = Rect(xa0, ya0, xa1, ya1)
    activ = cv.dbCreateRect(r, layer)
    layer = tech.getLayerNum("EXTBlock", "drawing")
    extblock = cv.dbCreateRect(r, layer)
    # Create P+ implant
    layer = tech.getLayerNum("pSD", "drawing")
    xp0 = int(xa0 - psd_en_activ)
    yp0 = int(ya0 - psd_en_activ)
    xp1 = int(xa1 + psd_en_activ)
    yp1 = int(ya1 + psd_en_activ)
    r = Rect(xp0, yp0, xp1, yp1)
    psd = cv.dbCreateRect(r, layer)
    # Create NWell
    layer = tech.getLayerNum("NWell", "drawing")
    xn0 = int(xa0 - nwell_en_psd_activ)
    yn0 = int(ya0 - nwell_en_psd_activ)
    xn1 = int(xa1 + nwell_en_psd_activ)
    yn1 = int(ya1 + nwell_en_psd_activ)
    r = Rect(xn0, yn0, xn1, yn1)
    psd = cv.dbCreateRect(r, layer)
    # Create metalization
    layer = tech.getLayerNum("Metal1", "drawing")
    # xm0 = int(-metal1_en_cont)
    # ym0 = int(-metal1_en_cont)
    # xm1 = int(xc14 + metal1_en_cont)
    # ym1 = int(yc14 + metal1_en_cont)
    xm0 = 0
    ym0 = 0
    xm1 = xc14
    ym1 = yc14
    r = Rect(xm0, ym0, xm1, ym1)
    metal1 = cv.dbCreateRect(r, layer)
    #
    # Add device type
    #
    cv.dbAddProp("type", "dio")
    #
    # Save results
    #
    cv.update()