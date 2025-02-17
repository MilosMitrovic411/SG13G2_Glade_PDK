#
# Import the db 
#
from ui import *
#
# The entry point
#
def isolbox(cv, w=4e-6, l=4e-6) :
    lib = cv.lib()
    tech = lib.tech()
    dbu = lib.dbuPerUU()
    width = max(int(w * 1e6 * dbu), int(w * 1e9))
    length = max(int(l * 1e6 * dbu), int(l * 1e9))
    #
    # Layer rules
    #
    xygrid = int(0.005 * dbu)
    nwell_width = int(0.62 * dbu)
    pwellblock_width = int(0.62 * dbu)
    nbulay_en_activ = int(1.24 * dbu)
    nwell_en_nsd_activ = int(0.24 * dbu)
    activ_width = int(0.15 * dbu)
    activ_ex_ds = int(0.23 * dbu)
    gatepoly_width = int(0.13 * dbu)
    gatepoly_ex_activ = int(0.18 * dbu)
    gate_to_activ = int(0.07 * dbu)
    cont_width = int(0.16 * dbu)
    cont_space = int(0.18 * dbu)
    activ_en_cont = int(0.07 * dbu)
    gatepoly_en_cont = int(0.07 * dbu)
    cont_gatpoly_to_activ = int(0.14 * dbu)
    cont_activ_to_gatpoly = int(0.11 * dbu)
    metal1_en_cont = int(0.065 * dbu)
    psd_width = int(0.31 * dbu)
    psd_en_activ = int(0.03 * dbu)
    psd_en_cont = int(0.09 * dbu)
    psd_to_gate = int(0.3 * dbu)
    metal1_width = int(0.29 * dbu)
    metal1_space = int(0.21 * dbu)
    via_width = int(0.19 * dbu)
    via_space = int(0.22 * dbu)
    metal_en_via = int(0.05 * dbu)
    #
    # Device rules
    #
    min_width = int(3.17 * dbu)
    min_length = int(3.17 * dbu)
    #
    # Checking parameters
    #
    if width%xygrid!=0 :
        width = int(xygrid * int(width / xygrid))
        cv.dbReplaceProp("w", 1e-6 * (width / dbu))
        print("** NMOS WARNING: w is off-grid. Adjusting element width. **")
        cv.update()
    if length%xygrid!=0 :
        length = int(xygrid * int(length / xygrid))
        cv.dbReplaceProp("l", 1e-6 * (length / dbu))
        print("** NMOS WARNING: l is off-grid. Adjusting element length. **")
        cv.update()
    if width < min_width :
        width = min_width
        cv.dbReplaceProp("w", 1e-6 * (width / dbu))
        print("** NMOS WARNING: w < min_width. Resetting element width. **")
        cv.update()
    if length < length :
        length = min_length
        cv.dbReplaceProp("l", 1e-6 * (length / dbu))
        print("** NMOS WARNING: l < min_length. Resetting element length. **")
        cv.update()
    #
    # Creating the device
    #
    # Create N-buried Layer
    layer = tech.getLayerNum("nBuLay", "drawing")
    xnbl0 = 0
    ynbl0 = 0
    xnbl1 = int(length)
    ynbl1 = int(width)
    r = Rect(xnbl0, ynbl0, xnbl1, ynbl1)
    nbulay = cv.dbCreateRect(r, layer)
    # Create Nwell isolation ring
    layer = tech.getLayerNum("PWell", "drawing")
    xp0 = int(xnbl0 + 2 * nwell_en_nsd_activ + 2 * activ_en_cont + cont_width)
    yp0 = int(ynbl0 + 2 * nwell_en_nsd_activ + 2 * activ_en_cont + cont_width)
    xp1 = int(xnbl1 - 2 * nwell_en_nsd_activ - 2 * activ_en_cont - cont_width)
    yp1 = int(ynbl1 - 2 * nwell_en_nsd_activ - 2 * activ_en_cont - cont_width)
    r = Rect(xp0, yp0, xp1, yp1)
    pwell = cv.dbCreateRect(r, layer)
    xmpp0 = int(xnbl0 + nwell_en_nsd_activ + activ_en_cont + cont_width / 2)
    ympp0 = int(ynbl0 + nwell_en_nsd_activ + activ_en_cont + cont_width / 2)
    xmpp1 = int(xnbl1 - nwell_en_nsd_activ - activ_en_cont - cont_width / 2)
    ympp1 = ympp0
    xmpp2 = xmpp1
    ympp2 = int(ynbl1 - nwell_en_nsd_activ - activ_en_cont - cont_width / 2)
    xmpp3 = xmpp0
    ympp3 = ympp2
    xmpp4 = xmpp0
    ympp4 = ympp0
    ring = lib.getMPPRule("nguard")
    nring = cv.dbCreateMPP(ring, [[xmpp0,ympp0],[xmpp1,ympp1],[xmpp2,ympp2],[xmpp3,ympp3], [xmpp4,ympp4]], 5)
    net = cv.dbCreateNet("Iso")
    pin = cv.dbCreatePin("Iso", net, DB_PIN_INOUT)
    cv.dbCreatePort(pin, nring)
    # Create PWell block
    p_layer = tech.getLayerNum("PWell", "block")
    xmpp = intarray(5)
    ympp = intarray(5)
    xmpp[0] = int(xnbl0 - pwellblock_width / 2)
    ympp[0] = int(ynbl1 + pwellblock_width / 2)
    xmpp[1] = int(xnbl1 + pwellblock_width / 2)
    ympp[1] = ympp[0]
    xmpp[2] = xmpp[1]
    ympp[2] = int(ynbl0 - pwellblock_width / 2)
    xmpp[3] = xmpp[0]
    ympp[3] = ympp[2]
    xmpp[4] = xmpp[0]
    ympp[4] = ympp[0]
    p_path = cv.dbCreatePath(xmpp, ympp, 5, p_layer, pwellblock_width, 2, int(pwellblock_width / 2), int(pwellblock_width / 2))
    #
    # Save results
    #
    cv.update()