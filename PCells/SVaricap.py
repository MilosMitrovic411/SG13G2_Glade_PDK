#
# Import the db 
#
from ui import *
#
# The entry point
#
def SVaricap(cv, Width=["3.74u" , "9.74u"], Length=["0.3u", "0.8u"], Nx=1, type="cap", model="sg13_hv_svaricap") :
    lib = cv.lib()
    tech = lib.tech()
    dbu = lib.dbuPerUU()
    w = int(3.74 * dbu)
    l = int(0.3 * dbu)
    if (Width == "9.74u") :
        w = int(9.74 * dbu)
    if (Length == "0.8u") :
        l = int(0.8 * dbu)
    nf = int(Nx)
    #
    # Layer rules
    # 
    xygrid = int(0.005 * dbu)
    cont_width = int(0.16 * dbu)
    cont_space = int(0.18 * dbu)
    gatepoly_en_cont = int(0.07 * dbu)
    activ_en_cont = int(0.07 * dbu)
    nwell_en_nsd_activ = int(0.24 * dbu)
    #
    # Creating the device
    #
    gatpoly_layer = tech.getLayerNum("GatPoly", "drawing")
    cont_layer = tech.getLayerNum("Cont", "drawing")
    metal_layer = tech.getLayerNum("Metal1", "drawing")
    activ_layer = tech.getLayerNum("Activ", "drawing")
    nbulay_layer = tech.getLayerNum("nBuLay", "drawing")
    psd_layer = tech.getLayerNum("pSD", "drawing")
    nwell_layer = tech.getLayerNum("NWell", "drawing")
    thickgateox_layer = tech.getLayerNum("ThickGateOx", "drawing")
    text_layer = tech.getLayerNum("TEXT", "drawing")
    substrate_layer = tech.getLayerNum("Substrate", "drawing")
    #
    cont_x_offset = gatepoly_en_cont
    if (l == int(0.8 * dbu)) :
        cont_x_offset = int(0.32 * dbu)
    for n in range(nf) :
        cont_y_offset = 0
        xg0 = int(n * (2 * l + 0.5 * dbu))
        yg0 = 0
        xg1 = int(xg0 + l)
        yg1 = int(yg0 + w)
        r = Rect(xg0 , yg0, xg1, yg1)
        gatpoly = cv.dbCreateRect(r, gatpoly_layer)
        if (w == int(3.74 * dbu)) :
            for m in range(10) :
                xc0 = int(xg0 + cont_x_offset)
                if (m != 0) :
                    cont_y_offset = int(cont_y_offset + 0.215 * dbu + cont_width)
                    if (m % 3 == 0) :
                        cont_y_offset = int(cont_y_offset - 0.215 * dbu + 0.22 * dbu)
                yc0 = int(0.13 * dbu + cont_y_offset)
                xc1 = int(xc0 + cont_width)
                yc1 = int(yc0 + cont_width)
                r = Rect(xc0 , yc0, xc1, yc1)
                cont = cv.dbCreateRect(r, cont_layer)
        else :
            for m in range(28) :
                xc0 = int(xg0 + cont_x_offset)
                if (m != 0) :
                    cont_y_offset = int(cont_y_offset + 0.185 * dbu + cont_width)
                    if ((m % 2 == 0) or (m == 27)) :
                        cont_y_offset = int(cont_y_offset - 0.185 * dbu + 0.19 * dbu)
                yc0 = int(0.13 * dbu + cont_y_offset)
                xc1 = int(xc0 + cont_width)
                yc1 = int(yc0 + cont_width)
                r = Rect(xc0 , yc0, xc1, yc1)
                cont = cv.dbCreateRect(r, cont_layer)
        xm0 = int(xc0 - 0.05 * dbu)
        ym0 = int(yg0 + 0.08 * dbu)
        xm1 = int(xc1 + 0.05 * dbu)
        ym1 = int(yg1 + 0.12 * dbu)
        r = Rect(xm0 , ym0, xm1, ym1)
        metal = cv.dbCreateRect(r, metal_layer)
    #
    for n in range(nf) :
        cont_y_offset = 0
        xg0 = int(l + 0.25 * dbu + n * (2 * l + 0.5 * dbu))
        yg0 = int(-0.25 * dbu)
        xg1 = int(xg0 + l)
        yg1 = int(yg0 + w)
        r = Rect(xg0 , yg0, xg1, yg1)
        gatpoly = cv.dbCreateRect(r, gatpoly_layer)
        if (w == int(3.74 * dbu)) :
            for m in range(10) :
                xc0 = int(xg0 + cont_x_offset)
                if (m != 0) :
                    cont_y_offset = int(cont_y_offset + 0.215 * dbu + cont_width)
                    if (m % 3 == 0) :
                        cont_y_offset = int(cont_y_offset - 0.215 * dbu + 0.22 * dbu)
                yc0 = int(-0.19 * dbu + cont_y_offset)
                xc1 = int(xc0 + cont_width)
                yc1 = int(yc0 + cont_width)
                r = Rect(xc0 , yc0, xc1, yc1)
                cont = cv.dbCreateRect(r, cont_layer)
        else :
            for m in range(28) :
                xc0 = int(xg0 + cont_x_offset)
                if (m != 0) :
                    cont_y_offset = int(cont_y_offset + 0.185 * dbu + cont_width)
                    if ((m % 2 == 0) or (m == 27)) :
                        cont_y_offset = int(cont_y_offset - 0.185 * dbu + 0.19 * dbu)
                yc0 = int(-0.19 * dbu + cont_y_offset)
                xc1 = int(xc0 + cont_width)
                yc1 = int(yc0 + cont_width)
                r = Rect(xc0 , yc0, xc1, yc1)
                cont = cv.dbCreateRect(r, cont_layer)
        xm0 = int(xc0 - 0.05 * dbu)
        ym0 = int(yg0 - 0.12 * dbu)
        xm1 = int(xc1 + 0.05 * dbu)
        ym1 = int(yg1 - 0.08 * dbu)
        r = Rect(xm0 , ym0, xm1, ym1)
        metal = cv.dbCreateRect(r, metal_layer)
        #
    xpoly0 = 0
    ypoly0 = w
    xpoly1 = xg1
    ypoly1 = int(ypoly0 + 0.5 * dbu)
    r = Rect(xpoly0 , ypoly0, xpoly1, ypoly1)
    poly = cv.dbCreateRect(r, gatpoly_layer)
    xm0 = int(0.02 * dbu)
    ym0 = int(ypoly0 + 0.12 * dbu)
    xm1 = int(xpoly1 - 0.02 * dbu)
    ym1 = int(ypoly1 - 0.12 * dbu)
    r = Rect(xm0 , ym0, xm1, ym1)
    metal = cv.dbCreateRect(r, metal_layer)
    net = cv.dbCreateNet("G2")
    pin = cv.dbCreatePin("G2", net, DB_PIN_INOUT)
    cv.dbCreatePort(pin, metal)
    if ((nf == 1) and (l == int(0.3 * dbu))) :
        xc0 = int(xm0 + 0.05 * dbu)
        yc0 = int(ym0  + 0.05 * dbu)
        xc1 = int(xc0 + cont_width)
        yc1 = int(yc0 + cont_width)
        r = Rect(xc0 , yc0, xc1, yc1)
        cont = cv.dbCreateRect(r, cont_layer)
        xc0 = int(xm1 - 0.05 * dbu)
        xc1 = int(xc0 - cont_width)
        r = Rect(xc0 , yc0, xc1, yc1)
        cont = cv.dbCreateRect(r, cont_layer)
    else :
        xc0 = int(xpoly1 / 2 - cont_width / 2)
        yc0 = int(ym0 + 0.05 * dbu)
        xc1 = int(xc0 + cont_width)
        yc1 = int(yc0 + cont_width)
        r = Rect(xc0 , yc0, xc1, yc1)
        cont = cv.dbCreateRect(r, cont_layer)
        n_cont = int(((xm1 - xm0) / 2 - 0.05 * dbu) / (cont_width + cont_space))
        offset = int(((xm1 - xm0)/ 2 - (0.05 * dbu+ n_cont * (cont_width + cont_space))) / (2 * n_cont))
        if (offset%xygrid!=0) :
            offset = int(xygrid * int(offset / xygrid))
        for n in range(n_cont) :
            xc0 = int(xm0 + 0.05 * dbu + n * (cont_width + cont_space + offset))
            yc0 = int(ym0 + 0.05 * dbu)
            xc1 = int(xc0 + cont_width)
            yc1 = int(yc0 + cont_width)
            r = Rect(xc0 , yc0, xc1, yc1)
            cont = cv.dbCreateRect(r, cont_layer)
        for n in range(n_cont) :
            xc0 = int(xm1 - 0.05 * dbu - n * (cont_width + cont_space + offset))
            yc0 = int(ym0 + 0.05 * dbu)
            xc1 = int(xc0 - cont_width)
            yc1 = int(yc0 + cont_width)
            r = Rect(xc0 , yc0, xc1, yc1)
            cont = cv.dbCreateRect(r, cont_layer)
    ypoly0 = yg0
    ypoly1 = int(ypoly0 - 0.5 * dbu)
    r = Rect(xpoly0 , ypoly0, xpoly1, ypoly1)
    poly = cv.dbCreateRect(r, gatpoly_layer)
    ym0 = int(ypoly0 - 0.12 * dbu)
    ym1 = int(ypoly1 + 0.12 * dbu)
    r = Rect(xm0 , ym0, xm1, ym1)
    metal = cv.dbCreateRect(r, metal_layer)
    net = cv.dbCreateNet("G1")
    pin = cv.dbCreatePin("G1", net, DB_PIN_INOUT)
    cv.dbCreatePort(pin, metal)
    if ((nf == 1) and (l == int(0.3 * dbu))) :
        xc0 = int(xm0 + 0.05 * dbu)
        yc0 = int(ym0 - 0.05 * dbu)
        xc1 = int(xc0 + cont_width)
        yc1 = int(yc0 - cont_width)
        r = Rect(xc0 , yc0, xc1, yc1)
        cont = cv.dbCreateRect(r, cont_layer)
        xc0 = int(xm1 - 0.05 * dbu)
        xc1 = int(xc0 - cont_width)
        r = Rect(xc0 , yc0, xc1, yc1)
        cont = cv.dbCreateRect(r, cont_layer)
    else :
        xc0 = int(xpoly1 / 2 - cont_width / 2)
        yc0 = int(ym0 - 0.05 * dbu)
        xc1 = int(xc0 + cont_width)
        yc1 = int(yc0 - cont_width)
        r = Rect(xc0 , yc0, xc1, yc1)
        cont = cv.dbCreateRect(r, cont_layer)
        n_cont = int(((xm1 - xm0) / 2 - 0.05 * dbu) / (cont_width + cont_space))
        offset = int(((xm1 - xm0)/ 2 - (0.05 * dbu+ n_cont * (cont_width + cont_space))) / (2 * n_cont))
        if (offset%xygrid!=0) :
            offset = int(xygrid * int(offset / xygrid))
        for n in range(n_cont) :
            xc0 = int(xm0 + 0.05 * dbu + n * (cont_width + cont_space + offset))
            yc0 = int(ym0  - 0.05 * dbu)
            xc1 = int(xc0 + cont_width)
            yc1 = int(yc0 - cont_width)
            r = Rect(xc0 , yc0, xc1, yc1)
            cont = cv.dbCreateRect(r, cont_layer)
        for n in range(n_cont) :
            xc0 = int(xm1 - 0.05 * dbu - n * (cont_width + cont_space + offset))
            yc0 = int(ym0 - 0.05 * dbu)
            xc1 = int(xc0 - cont_width)
            yc1 = int(yc0 - cont_width)
            r = Rect(xc0 , yc0, xc1, yc1)
            cont = cv.dbCreateRect(r, cont_layer)
    #
    xa0 = int(-0.49 * dbu)
    ya0 = int(-0.4 * dbu)
    xa1 = int(xg1 + 0.33 * dbu)
    ya1 = int(yg1 + 0.4 * dbu)
    r = Rect(xa0 , ya0, xa1, ya1)
    activ = cv.dbCreateRect(r, activ_layer)
    xn0 = int(xa0 - 0.24 * dbu)
    yn0 = int(ya0 - 0.24 * dbu)
    xn1 = int(xa1 + 0.24 * dbu)
    yn1 = int(ya1 + 0.24 * dbu)
    xm0 = int(xa0 + 0.05 * dbu)
    ym0 = int(ya0 + 1.665 * dbu)
    xm1 = int(xm0 + 0.2 * dbu)
    ym1 = int(ym0 + 0.96 * dbu)
    if (w == int(9.74 * dbu)) :
        yn0 = int(ya0 - 0.25 * dbu)
        yn1 = int(ya1 + 0.25 * dbu)
        r = Rect(xa0 , yn0, xa1, yn1)
        yn0 = int(ya0 - 0.49 * dbu)
        yn1 = int(ya1 + 0.49 * dbu)
        ym0 = int(ya0 + 4.665 * dbu)
        ym1 = int(ym0 + 0.96 * dbu)
    nbulay = cv.dbCreateRect(r, nbulay_layer)
    r = Rect(xn0 , yn0, xn1, yn1)
    nwell = cv.dbCreateRect(r, nwell_layer)
    r = Rect(xm0 , ym0, xm1, ym1)
    metal = cv.dbCreateRect(r, metal_layer)
    net = cv.dbCreateNet("W")
    pin = cv.dbCreatePin("W", net, DB_PIN_INOUT)
    cv.dbCreatePort(pin, metal)
    for n in range(3) :
        xc0 = int(xm0 + 0.02 * dbu)
        yc0 = int(ym0 + 0.05 * dbu + n * (cont_width + 0.19 * dbu))
        xc1 = int(xc0 + cont_width)
        yc1 = int(yc0 + cont_width)
        r = Rect(xc0 , yc0, xc1, yc1)
        cont = cv.dbCreateRect(r, cont_layer)
    #
    xac0 = int(xpoly1 / 2 - 0.12 * dbu)
    yac0 = ya0
    xac1 = int(xac0 + 0.24 * dbu)
    yac1 = int(yac0 - 0.76 * dbu)
    yt0 = int(yac1 - 0.27 * dbu)
    r = Rect(xac0 , yac0, xac1, yac1)
    activ = cv.dbCreateRect(r, activ_layer)
    xp0 = int(xac0 - 0.1 *dbu)
    yp0 = int(yac0 - 0.1 * dbu)
    xp1 = int(xac1 + 0.1 * dbu)
    yp1 = int(yac1 - 0.1 * dbu)
    r = Rect(xp0 , yp0, xp1, yp1)
    psd = cv.dbCreateRect(r, psd_layer)
    yac0 = ya1
    yac1 = int(yac0 + 0.76 * dbu)
    yt1 = int(yac1 + 0.27 * dbu)
    r = Rect(xac0 , yac0, xac1, yac1)
    activ = cv.dbCreateRect(r, activ_layer)
    yp0 = int(yac0 + 0.1 * dbu)
    yp1 = int(yac1 + 0.1 * dbu)
    r = Rect(xp0 , yp0, xp1, yp1)
    psd = cv.dbCreateRect(r, psd_layer)
    #
    xt0 = int(xa0 - 0.27 * dbu)
    xt1 = int(xa1 + 0.27 * dbu)
    r = Rect(xt0 , yt0, xt1, yt1)
    thickgateox = cv.dbCreateRect(r, thickgateox_layer)
    substrate = cv.dbCreateRect(r, substrate_layer)
    net = cv.dbCreateNet("sub!")
    pin = cv.dbCreatePin("sub!", net, DB_PIN_INOUT)
    #
    p = Point(int(xa0 + 0.035 * dbu), int(ya0 - 0.05 * dbu))
    text = cv.dbCreateLabel(p, "SVaricap", R0, 0.285,  bottomLeft, text_layer)
    #
    # Save results
    #
    cv.update()