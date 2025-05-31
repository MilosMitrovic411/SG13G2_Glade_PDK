#
# Import the db 
#
from ui import *
#
# The entry point
#
def npn13G2(cv, numberOfEmitters=1, type="bjt", modelName="npn13G2") :
    lib = cv.lib()
    tech = lib.tech()
    dbu = lib.dbuPerUU()
    n_emitt=int(numberOfEmitters)
    #
    # Layer rules
    #
    emwind_width = int(0.07 * dbu)
    emwind_length = int(0.9 * dbu)
    via_width = int(0.19 * dbu)
    via_space = int(0.22 * dbu)
    metal_en_via = int(0.05 * dbu)
    activ_en_cont = int(0.07 * dbu)
    cont_width = int(0.16 * dbu)
    offset = int(1.85 * dbu)
    #
    # Device rules
    #
    #
    # Checking parameters
    #
    if (n_emitt < 1) :
        n_emitt = 1
        cv.dbReplaceProp("numberOfEmitters", n_emitt)
        cv.update()
    if (n_emitt > 10) :
        n_emitt = 10
        cv.dbReplaceProp("numberOfEmitters", n_emitt)
        cv.update()
	#
    # Creating the device
    #
    emwind_layer = tech.getLayerNum("EmWind", "drawing")
    metal1_layer = tech.getLayerNum("Metal1", "drawing")
    via1_layer = tech.getLayerNum("Via1", "drawing")
    metal2_layer = tech.getLayerNum("Metal2", "drawing")
    activ_mask_layer = tech.getLayerNum("Activ", "mask")
    activ_layer = tech.getLayerNum("Activ", "drawing")
    cont_layer = tech.getLayerNum("Cont", "drawing")
    nsd_block_layer = tech.getLayerNum("nSD", "block")
    trans_layer = tech.getLayerNum("TRANS", "drawing")
    psd_layer = tech.getLayerNum("pSD", "drawing")
    text_layer = tech.getLayerNum("TEXT", "drawing")
    for n in range(n_emitt) :
        # Create EmWind
        xe0 = int(n * offset)
        ye0 = 0
        xe1 = xe0 + emwind_width
        ye1 = emwind_length
        r = Rect(xe0, ye0, xe1, ye1)
        emwind = cv.dbCreateRect(r, emwind_layer)
        # Create Metal1 over Emitter
        xm10 = int(-0.315 * dbu + n * offset)
        ym10 = int(-0.335 * dbu)
        xm11 = int(emwind_width + 0.315 * dbu + n * offset)
        ym11 = int(emwind_length + 0.32 * dbu)
        r = Rect(xm10, ym10, xm11, ym11)
        metal1 = cv.dbCreateRect(r, metal1_layer)
        net = cv.dbCreateNet("E")
        pin = cv.dbCreatePin("E", net, DB_PIN_INOUT)
        cv.dbCreatePort(pin, metal1)
        # Create Via1
        n_via1 = int((ym11 - ym10 - 2 * metal_en_via + via_space) / (via_width + via_space))
        via_offset = int((ym11 - ym10 - (2 * metal_en_via + n_via1 * (via_width + via_space) - via_space)) / 2)
        for m in range (n_via1) :
            for k in range (2) :
                xv10 = int(xm10 + metal_en_via + k * (via_space + via_width))
                yv10 = int(ym10 + via_offset + metal_en_via + m * (via_space + via_width))
                xv11 = int(xv10 + via_width)
                yv11 = int(yv10 + via_width)
                r = Rect(xv10, yv10, xv11, yv11)
                via1 = cv.dbCreateRect(r, via1_layer)
        # Create Activ:mask
        n_points = 8
        xam = intarray(n_points)
        yam = intarray(n_points)
        xam[0] = int(-0.89 * dbu + n * offset)
        yam[0] = int(-0.17 * dbu)
        xam[1] = int(xam[0] + 0.48 * dbu)
        yam[1] = yam[0]
        xam[2] = int(xam[1] + 0.21 * dbu)
        yam[2] = int(-0.38 * dbu)
        xam[3] = int(xam[2] + 0.47 * dbu)
        yam[3] = yam[2]
        xam[4] = int(xam[3] + 0.21 * dbu)
        yam[4] = yam[0]
        xam[5] = int(xam[4] + 0.48 * dbu)
        yam[5] = yam[0]
        xam[6] = xam[5]
        yam[6] = int(yam[0] + 1.6 * dbu)
        xam[7] = xam[0]
        yam[7] = yam[6]
        activ_mask = cv.dbCreatePolygon(xam, yam, n_points, activ_mask_layer)
        # Create Activ
        xa0 = int(-0.89 * dbu + n * offset)
        ya0 = yam[6]
        xa1 = int(xa0 + offset)
        ya1 = int(ya0 + 2 * activ_en_cont + cont_width)
        r = Rect(xa0, ya0, xa1, ya1)
        activ = cv.dbCreateRect(r, activ_layer)
        # Create Cont for Collector
        xc0 = int(xa0 + 0.1 * dbu)
        yc0 = int(ya0 + activ_en_cont)
        xc1 = int(xa1 - 0.1 * dbu)
        yc1 = int(yc0 + cont_width)
        r = Rect(xc0, yc0, xc1, yc1)
        cont = cv.dbCreateRect(r, cont_layer)
        # Create Cont for Base
        xc0 = int(xa0 + 0.165 * dbu)
        yc0 = int(-0.65 * dbu)
        xc1 = int(xa1 - 0.165 * dbu)
        yc1 = int(yc0 - cont_width)
        r = Rect(xc0, yc0, xc1, yc1)
        cont = cv.dbCreateRect(r, cont_layer)
        # Create nSD blcok
        n_points = 10
        xn = intarray(n_points)
        yn = intarray(n_points)
        xn[0] = int(-0.94 * dbu + n * offset)
        yn[0] = int(ym10 - 1.645 * dbu)
        xn[1] = int(xn[0] + 1.95 * dbu)
        yn[1] = yn[0]
        xn[2] = xn[1]
        yn[2] = int(yn[1] + 1.53 * dbu)
        xn[3] = int(xn[2] - 0.42 * dbu)
        yn[3] = int(yn[2] + 0.42 * dbu)
        xn[4] = xn[3]
        yn[4] = int(yn[3] + 1.17 * dbu)
        xn[5] = int(xn[4] - 0.25 * dbu)
        yn[5] = int(yn[4] + 0.25 * dbu)
        xn[6] = int(xn[5] - 0.61* dbu)
        yn[6] = yn[5]
        xn[7] = int(xn[6] - 0.25 * dbu)
        yn[7] = int(yn[6] - 0.25 * dbu)
        xn[8] = xn[7]
        yn[8] = int(yn[7] - 1.17 * dbu)
        xn[9] = int(xn[8] - 0.42 * dbu)
        yn[9] = int(yn[8] - 0.42 * dbu)
        nsd_block = cv.dbCreatePolygon(xn, yn, n_points, nsd_block_layer)
    # Create Metal2
    xm20 = int(-0.89 * dbu)
    ym20 = ym10
    xm21 = int(xm20 + n_emitt * offset)
    ym21 = ym11
    r = Rect(xm20, ym20, xm21, ym21)
    metal2 = cv.dbCreateRect(r, metal2_layer)
    net = cv.dbCreateNet("E")
    pin = cv.dbCreatePin("E", net, DB_PIN_INOUT)
    cv.dbCreatePort(pin, metal2)
    # Create Metal1 over Collector
    if (n_emitt > 1) :
        xm10 = xm20
        ym10 = int(ya0 + activ_en_cont - 0.03 * dbu)
        xm11 = xm21
        ym11 = int(ym10 + 0.44 * dbu)
        r = Rect(xm10, ym10, xm11, ym11)
        metal1 = cv.dbCreateRect(r, metal1_layer)
        net = cv.dbCreateNet("C")
        pin = cv.dbCreatePin("C", net, DB_PIN_INOUT)
        cv.dbCreatePort(pin, metal1)
    else :
        xm10 = xm20
        ym10 = int(ya0 + activ_en_cont - 0.04 * dbu)
        xm11 = xm21
        ym11 = int(ym10 + 0.24 * dbu)
        r = Rect(xm10, ym10, xm11, ym11)
        metal1 = cv.dbCreateRect(r, metal1_layer)
        net = cv.dbCreateNet("C")
        pin = cv.dbCreatePin("C", net, DB_PIN_INOUT)
        cv.dbCreatePort(pin, metal1)
    # Create Metal1 over Base
    xm10 = int(-0.94 * dbu)
    ym10 = int(yc0 + 0.04 * dbu)
    xm11 = int(xc1 + 0.215 * dbu)
    ym11 = int(yc1 - 0.04 * dbu)
    r = Rect(xm10, ym10, xm11, ym11)
    metal1 = cv.dbCreateRect(r, metal1_layer)
    net = cv.dbCreateNet("B")
    pin = cv.dbCreatePin("B", net, DB_PIN_INOUT)
    cv.dbCreatePort(pin, metal1)
    # Create Trans
    xt0 = int(xm10 - 1.475 * dbu)
    yt0 = yn[0]
    xt1 = int(xm11 + 1.475 * dbu)
    yt1 = int(yt0 + 5.31 * dbu)
    r = Rect(xt0, yt0, xt1, yt1)
    trans = cv.dbCreateRect(r, trans_layer)
    # Create Text
    p = Point(int(xt0 + 1.37 * dbu), int(yt1 - 0.43 * dbu))
    text = cv.dbCreateLabel(p, "npn13G2", R0, 0.43, topLeft, text_layer)
    p = Point(int(xt0 + 0.1 * dbu), int(yt0 + 0.1 * dbu))
    str_NE = str(n_emitt)
    string = "Ae =" + str_NE + "*0.07*0.90"
    text = cv.dbCreateLabel(p, string, R90, 0.43, topLeft, text_layer)
    p = Point(int((xt1 - xt0) / 2 - 2.415 * dbu), int(yt0 + 1.18 * dbu))
    text = cv.dbCreateLabel(p, "B", R0, 0.15, bottomCentre, text_layer)
    p = Point(int((xt1 - xt0) / 2 - 2.415 * dbu), int(yt0 + 1.98 * dbu))
    text = cv.dbCreateLabel(p, "E", R0, 0.7, bottomCentre, text_layer)
    if (n_emitt > 1) :
        p = Point(int((xt1 - xt0) / 2 - 2.415 * dbu), int(yt0 + 3.535 * dbu))
        text = cv.dbCreateLabel(p, "C", R0, 0.7, bottomCentre, text_layer)
    else :
        p = Point(int((xt1 - xt0) / 2 - 2.415 * dbu), int(yt0 + 3.49 * dbu))
        text = cv.dbCreateLabel(p, "C", R0, 0.15, bottomCentre, text_layer)
    # Create pSD
    xmpp = intarray(5)
    ympp = intarray(5)
    xmpp[0] = int(xt0 - 0.45 * dbu)
    ympp[0] = int(yt0 - 0.45 * dbu)
    xmpp[1] = int(xt1 + 0.45 * dbu)
    ympp[1] = ympp[0]
    xmpp[2] = xmpp[1]
    ympp[2] = int(yt1 + 0.45 * dbu)
    xmpp[3] = xmpp[0]
    ympp[3] = ympp[2]
    xmpp[4] = xmpp[0]
    ympp[4] = ympp[0]
    psd_path = cv.dbCreatePath(xmpp, ympp, 5, psd_layer, int(0.9 * dbu), 2, int(0.45 * dbu), int(0.45 * dbu))
    # Create Activ
    activ_path = cv.dbCreatePath(xmpp, ympp, 5, activ_layer, int(0.5 * dbu), 2, int(0.25 * dbu), int(0.25 * dbu))
    net = cv.dbCreateNet("sub!")
    pin = cv.dbCreatePin("sub!", net, DB_PIN_INOUT)
    cv.dbCreatePort(pin, activ_path)
    #
    # Save results
    #
    cv.update()