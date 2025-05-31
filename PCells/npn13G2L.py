#
# Import the db 
#
from ui import *
#
# The entry point
#
def npn13G2L(cv, emitterLength=1e-6, numberOfEmitters=1, type="bjt", modelName="npn13G2l") :
    lib = cv.lib()
    tech = lib.tech()
    dbu = lib.dbuPerUU()
    l = max(int(emitterLength * 1e6 * dbu), int(emitterLength * 1e9))
    ne=int(numberOfEmitters)
    #
    # Layer rules
    #
    xygrid = int(0.005 * dbu)
    emwind_width = int(0.07 * dbu)
    via_width = int(0.19 * dbu)
    via_space = int(0.22 * dbu)
    metal_en_via = int(0.05 * dbu)
    activ_en_cont = int(0.07 * dbu)
    cont_width = int(0.16 * dbu)
    cont_space = int(0.18 * dbu)
    #
    # Device rules
    #
    #
    # Checking parameters
    #
    if (l < int(1 * dbu)) :
        l = int(1 * dbu)
        cv.dbReplaceProp("le", 1e-6 * (l / dbu))
        cv.update()
    if (l > int(2.5 * dbu)) :
        l = int(2.5 * dbu)
        cv.dbReplaceProp("le", 1e-6 * (l / dbu))
        cv.update()
    if (l%xygrid!=0) :
        l = int(xygrid * int(l / xygrid))
        cv.dbReplaceProp("le", 1e-6 * (l / dbu))
        cv.update()
    if (ne < 1) :
        ne = 1
        cv.dbReplaceProp("numberOfEmitters", ne)
        cv.update()
    if (ne > 4) :
        ne = 4
        cv.dbReplaceProp("numberOfEmitters", ne)
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
    heattrans_layer = tech.getLayerNum("HeatTrans", "drawing")
    device_offset = int(2.8 * dbu)
    for i in range(ne):
        xe0 = int(i * device_offset)
        ye0 = 0
        xe1 = int(xe0 + emwind_width)
        ye1 = l
        r = Rect(xe0, ye0, xe1, ye1)
        emwind = cv.dbCreateRect(r, emwind_layer)
        xh0 = int(xe0 - 0.05 * dbu)
        yh0 = int(ye0 - 0.05 * dbu)
        xh1 = int(xe1 + 0.05 * dbu)
        yh1 = int(ye1 + 0.05 * dbu)
        r = Rect(xh0, yh0, xh1, yh1)
        heattrans = cv.dbCreateRect(r, heattrans_layer)
        xc0 = int(xe0 - 0.045 * dbu)
        yc0 = int(ye0 - 0.15 * dbu)
        xc1 = int(xe1 + 0.045 * dbu)
        yc1 = int(ye1 + 0.15 * dbu)
        r = Rect(xc0, yc0, xc1, yc1)
        cont = cv.dbCreateRect(r, cont_layer)
        xm10 = int(xc0 - 0.05 * dbu)
        ym10 = int(yc0 - 0.05 * dbu)
        xm11 = int(xc1 + 0.05 * dbu)
        ym11 = int(yc1 + 0.05 * dbu)
        r = Rect(xm10, ym10, xm11, ym11)
        metal1 = cv.dbCreateRect(r, metal1_layer)
        xa0 = xm10
        ya0 = int(yc0 - 0.13 * dbu)
        xa1 = xm11
        ya1 = int(yc1 + 0.13 * dbu)
        r = Rect(xa0, ya0, xa1, ya1)
        activ = cv.dbCreateRect(r, activ_layer)
        xv10 = int(xc0 - 0.015 * dbu)
        yv10 = int(yc0 + 0.05 * dbu)
        xv11 = int(xc1 + 0.015 * dbu)
        yv11 = int(yc1 - 0.05 * dbu)
        r = Rect(xv10, yv10, xv11, yv11)
        via1 = cv.dbCreateRect(r, via1_layer)
        #
        xcb0 = int(xe0 - 1.185 * dbu)
        ycb0 = int(ye0 - 0.15 * dbu)
        xcb1 = int(xcb0 + 0.16 * dbu)
        ycb1 = int(ye1 + 0.15 * dbu)
        r = Rect(xcb0, ycb0, xcb1, ycb1)
        cont = cv.dbCreateRect(r, cont_layer)
        xm10 = int(xcb0 - 0.18 * dbu)
        ym10 = int(ycb0 - 0.13 * dbu)
        xm11 = int(xcb1 + 0.05 * dbu)
        ym11 = int(ycb1 + 0.85 * dbu)
        r = Rect(xm10, ym10, xm11, ym11)
        metal1 = cv.dbCreateRect(r, metal1_layer)
        xa0 = xm10
        ya0 = int(ycb0 - 0.13 * dbu)
        xa1 = int(xcb1 + 0.32 * dbu)
        ya1 = int(ycb1 + 0.13 * dbu)
        r = Rect(xa0, ya0, xa1, ya1)
        activ = cv.dbCreateRect(r, activ_layer)
        #
        xam0 = xa1
        yam0 = ya0
        xam1 = int(xam0 + 0.61 * dbu)
        yam1 = ya1
        r = Rect(xam0, yam0, xam1, yam1)
        activ_mask = cv.dbCreateRect(r, activ_mask_layer)
        n_cont = int((yam1 - yam0 - 2 * activ_en_cont + cont_space) / (cont_width + cont_space))
        for n in range(n_cont) :
            xc0 = int(xam0 + 0.225 * dbu)
            yc0 = int(yam0 + activ_en_cont + n * (cont_width + cont_space))
            xc1 = int(xc0 + cont_width)
            yc1 = int(yc0 + cont_width)
            r = Rect(xc0, yc0, xc1, yc1)
            cont = cv.dbCreateRect(r, cont_layer)
        xm10 = xc0
        ym10 = int(yam0 - 0.72 * dbu)
        xm11 = xc1
        ym11 = yam1
        r = Rect(xm10, ym10, xm11, ym11)
        metal1 = cv.dbCreateRect(r, metal1_layer)
        #
        xcb0 = int(xe0 + 1.095 * dbu)
        ycb0 = int(ye0 - 0.15 * dbu)
        xcb1 = int(xcb0 + 0.16 * dbu)
        ycb1 = int(ye1 + 0.15 * dbu)
        r = Rect(xcb0, ycb0, xcb1, ycb1)
        cont = cv.dbCreateRect(r, cont_layer)
        xm10 = int(xcb0 - 0.05 * dbu)
        ym10 = int(ycb0 - 0.13 * dbu)
        xm11 = int(xcb1 + 0.18 * dbu)
        ym11 = int(ycb1 + 0.85 * dbu)
        r = Rect(xm10, ym10, xm11, ym11)
        metal1 = cv.dbCreateRect(r, metal1_layer)
        xa0 = int(xcb0 - 0.32 * dbu)
        ya0 = int(ycb0 - 0.13 * dbu)
        xa1 = xm11
        ya1 = int(ycb1 + 0.13 * dbu)
        r = Rect(xa0, ya0, xa1, ya1)
        activ = cv.dbCreateRect(r, activ_layer)
        #
        xam0 = int(xa0 - 0.61 * dbu)
        yam0 = ya0
        xam1 = xa0
        yam1 = ya1
        r = Rect(xam0, yam0, xam1, yam1)
        activ_mask = cv.dbCreateRect(r, activ_mask_layer)
        for n in range(n_cont) :
            xc0 = int(xam0 + 0.225 * dbu)
            yc0 = int(yam0 + activ_en_cont + n * (cont_width + cont_space))
            xc1 = int(xc0 + cont_width)
            yc1 = int(yc0 + cont_width)
            r = Rect(xc0, yc0, xc1, yc1)
            cont = cv.dbCreateRect(r, cont_layer)
        xm10 = xc0
        ym10 = int(yam0 - 0.72 * dbu)
        xm11 = xc1
        ym11 = yam1
        r = Rect(xm10, ym10, xm11, ym11)
        metal1 = cv.dbCreateRect(r, metal1_layer)
    #
    xm20 = int(-1.365 * dbu)
    ym20 = int(-0.2 * dbu)
    xm21 = int(xcb1 + 0.18 * dbu)
    ym21 = int(ym20 + 1.4 * dbu)
    r = Rect(xm20, ym20, xm21, ym21)
    metal2 = cv.dbCreateRect(r, metal2_layer)
    net = cv.dbCreateNet("E")
    pin = cv.dbCreatePin("E", net, DB_PIN_INOUT)
    cv.dbCreatePort(pin, metal2)
    p = Point(int((xm21 - xm20) / 2 - 1.365 * dbu), int((ym21 - ym20) / 2 - 0.2 * dbu))
    text = cv.dbCreateLabel(p, "E", R0, 0.7, centreCentre, text_layer)
    #
    xm10 = int(-1.365 * dbu)
    ym10 = int(l + 1 * dbu)
    xm11 = int(xcb1 + 0.18 * dbu)
    ym11 = int(ym10 + 0.65 * dbu)
    r = Rect(xm10, ym10, xm11, ym11)
    metal1 = cv.dbCreateRect(r, metal1_layer)
    net = cv.dbCreateNet("C")
    pin = cv.dbCreatePin("C", net, DB_PIN_INOUT)
    cv.dbCreatePort(pin, metal1)
    p = Point(int((xm11 - xm10) / 2 - 1.365 * dbu), int((ym11 - ym10) / 2 + l + 1 * dbu))
    text = cv.dbCreateLabel(p, "C", R0, 0.3, centreCentre, text_layer)
    #
    xm10 = int(-0.48 * dbu)
    ym10 = int(-1 * dbu)
    xm11 = int(xcb1 - 0.705 * dbu)
    ym11 = int(ym10 - 0.65 * dbu)
    r = Rect(xm10, ym10, xm11, ym11)
    metal1 = cv.dbCreateRect(r, metal1_layer)
    net = cv.dbCreateNet("B")
    pin = cv.dbCreatePin("B", net, DB_PIN_INOUT)
    cv.dbCreatePort(pin, metal1)
    p = Point(int((xm11 - xm10) / 2 - 0.48 * dbu), int((ym11 - ym10) / 2 - 1 * dbu))
    text = cv.dbCreateLabel(p, "B", R0, 0.3, centreCentre, text_layer)
    #
    xt0 = int(xm10 - 2.485 * dbu)
    yt0 = int(ym11 - 0.55 * dbu)
    xt1 = int(xm11 + 2.485 * dbu)
    yt1 = int(yt0 + 4.4 * dbu + l)
    r = Rect(xt0, yt0, xt1, yt1)
    trans = cv.dbCreateRect(r, trans_layer)
    #
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
    activ_path = cv.dbCreatePath(xmpp, ympp, 5, activ_layer, int(0.5 * dbu), 2, int(0.25 * dbu), int(0.25 * dbu))
    net = cv.dbCreateNet("sub!")
    pin = cv.dbCreatePin("sub!", net, DB_PIN_INOUT)
    cv.dbCreatePort(pin, activ_path)  
    #
    p = Point(int(xt0 + 0.92 * dbu), int(yt0 + 0.105 * dbu))
    text = cv.dbCreateLabel(p, "npn13G2L", R0, 0.37, bottomLeft, text_layer)
    str_ne = str(ne)
    float_l = float(l / dbu)
    str_l = str(float_l)
    string = "Ae = " + str_ne + " * " + str_l + " * 0.07"
    p = Point(int(xt0 + 0.23 * dbu), int(yt0 + 0.13 * dbu))
    text = cv.dbCreateLabel(p, string, R90, 0.37, topLeft, text_layer)
    #
    # Save results
    #
    cv.update()