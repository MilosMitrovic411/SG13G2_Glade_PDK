#
# Import the db 
#
from ui import *
#
# The entry point
#
def diodevdd_4k(cv, type="dio", model = "diodevdd_4kv") :
    lib = cv.lib()
    tech = lib.tech()
    dbu = lib.dbuPerUU()
    #
    # Layer rules
    #
    cont_width = int(0.16 * dbu)
    cont_space = int(0.2 * dbu)
    activ_en_cont = int(0.07 * dbu)
    via_width = int(0.19 * dbu)
    via_space = int(0.29 * dbu)
    metal_en_via = int(0.005 * dbu)
    #
    # Creating the device
    #
    activ_layer = tech.getLayerNum("Activ", "drawing")
    psd_layer = tech.getLayerNum("pSD", "drawing")
    nwell_layer = tech.getLayerNum("NWell", "drawing")
    nwell_layer = tech.getLayerNum("NWell", "drawing")
    cont_layer = tech.getLayerNum("Cont", "drawing")
    metal1_layer = tech.getLayerNum("Metal1", "drawing")
    via1_layer = tech.getLayerNum("Via1", "drawing")
    metal2_layer = tech.getLayerNum("Metal2", "drawing")
    via2_layer = tech.getLayerNum("Via2", "drawing")
    metal3_layer = tech.getLayerNum("Metal3", "drawing")
    recog_layer = tech.getLayerNum("Recog", "esd")
    text_layer = tech.getLayerNum("TEXT", "drawing")
    gatpoly_layer = tech.getLayerNum("GatPoly", "drawing")
    nbulay_layer = tech.getLayerNum("nBuLay", "drawing")
    salblock_layer = tech.getLayerNum("SalBlock", "drawing")
    thickgateox_layer = tech.getLayerNum("ThickGateOx", "drawing")
    recog_layer = tech.getLayerNum("Recog", "drawing")
    recog_esd_layer = tech.getLayerNum("Recog", "esd")
    #
    # Creating Anode
    #
    for i in range(2) :
        xa0 = int(i * 4.53 * dbu)
        ya0 = 0
        xa1 = int(xa0 + 1.26 * dbu)
        ya1 = int(27.78 * dbu)
        r = Rect(xa0, ya0, xa1, ya1)
        activ = cv.dbCreateRect(r, activ_layer)
        xp0 = int(xa0 - 0.66 * dbu)
        yp0 = int(ya0 - 0.42 * dbu)
        xp1 = int(xa1 + 0.66 * dbu)
        yp1 = int(ya1 + 0.42 * dbu)
        r = Rect(xp0, yp0, xp1, yp1)
        psd = cv.dbCreateRect(r, psd_layer)
        xm0 = int(xa0 - 0.27 * dbu)
        ym0 = int(ya0 - 0.3 * dbu)
        xm1 = int(xa1 + 0.27 * dbu)
        ym1 = int(ya1 + 0.3 * dbu)
        r = Rect(xm0, ym0, xm1, ym1)
        metal = cv.dbCreateRect(r, metal1_layer)
        nx_cont = int((int(xa1 - xa0) - 2 * activ_en_cont + cont_space ) / (cont_width + cont_space))
        ny_cont = int((ya1 - 2 * activ_en_cont + cont_space) / (cont_width + cont_space))
        for n in range(nx_cont) :
            for m in range(ny_cont) :
                xc0 = int(0.21 * dbu + n * (cont_width + cont_space) + xa0)
                yc0 = int(0.16 * dbu + m * (cont_width + cont_space))
                xc1 = int(xc0 + cont_width)
                yc1 = int(yc0 + cont_width)
                r = Rect(xc0, yc0, xc1, yc1)
                cont = cv.dbCreateRect(r, cont_layer)
    #
    # Creating Cathode
    #
    xn0 = int(-2.67 * dbu)
    yn0 = int(-3.17 * dbu)
    xn1 = int(xn0 + 11.23 * dbu)
    yn1 = int(ya1 + 2.98 * dbu)
    r = Rect(xn0, yn0, xn1, yn1)
    nwell = cv.dbCreateRect(r, nwell_layer)
    xap = intarray(5)
    yap = intarray(5)
    xap[0] = int(xn0 + 1.05 * dbu)
    yap[0] = int(yn0 + 1.05 * dbu)
    xap[1] = int(xn1 - 1.05 * dbu)
    yap[1] = yap[0]
    xap[2] = xap[1]
    yap[2] = int(yn1 - 1.05 * dbu)
    xap[3] = xap[0]
    yap[3] = yap[2]
    xap[4] = xap[0]
    yap[4] = yap[0]
    activ_path = cv.dbCreatePath(xap, yap, 5, activ_layer, int(1.26 * dbu), 2, int(0.63 * dbu), int(0.63 * dbu))
    xa0 = int(xn0 + 4.95 * dbu)
    ya0 = int(yn0 + 1.68 * dbu)
    xa1 = int(xn0 + 6.21 * dbu)
    ya1 = int(yn1 - 1.68 * dbu)
    r = Rect(xa0, ya0, xa1, ya1)
    activ = cv.dbCreateRect(r, activ_layer)
    n_points = 10
    xm = intarray(n_points)
    ym = intarray(n_points)
    xm[0] = int(xn0 + 0.27 * dbu)
    ym[0] = int(yn0 + 0.33 * dbu)
    xm[1] = int(xn1 - 0.27 * dbu)
    ym[1] = ym[0]
    xm[2] = xm[1]
    ym[2] = int(yn1 - 0.33 * dbu)
    xm[3] = xm[0]
    ym[3] = ym[2]
    xm[4] = xm[0]
    ym[4] = int(yn0 + 1.74 * dbu)
    xm[5] = int (xn0 + 1.8 * dbu)
    ym[5] = ym[4]
    xm[6] = xm[5]
    ym[6] = int(yn1 - 1.74 * dbu)
    xm[7] = int(xn1 - 1.83 * dbu)
    ym[7] = ym[6]
    xm[8] = xm[7]
    ym[8] = ym[4]
    xm[9] = xm[0]
    ym[9] = ym[4]
    metal1 = cv.dbCreatePolygon(xm, ym, n_points, metal1_layer)
    xm0 = int(xn0 + 4.8 * dbu)
    ym0 = int(yn0 + 1.74 * dbu)
    xm1 = int(xn0 + 6.36 * dbu)
    ym1 = int(yn1 - 1.74 * dbu)
    r = Rect(xm0, ym0, xm1, ym1)
    metal1 = cv.dbCreateRect(r, metal1_layer)
    nx_cont = int((int(xap[1] + 1.26 * dbu - xap[0]) - 2 * activ_en_cont + cont_space) / (cont_width + cont_space))
    ny_cont = int((int(yap[1] + 1.26 * dbu - yap[0])  - 2 * activ_en_cont + cont_space) / (cont_width + cont_space))
    for n in range(nx_cont) :
        for m in range(ny_cont) :
            xc0 = int(int(xm[0] + 0.225 * dbu) + n * (cont_width + cont_space))
            yc0 = int(int(ym[0] + 0.3 * dbu) + m * (cont_width + cont_space))
            xc1 = int(xc0 + cont_width)
            yc1 = int(yc0 + cont_width)
            r = Rect(xc0, yc0, xc1, yc1)
            cont = cv.dbCreateRect(r, cont_layer)
            yc0 = int(int(ym[2] - 0.26 * dbu) - m * (cont_width + cont_space))
            yc1 = int(yc0 - cont_width)
            r = Rect(xc0, yc0, xc1, yc1)
            cont = cv.dbCreateRect(r, cont_layer)
    ny_cont = int((30.57 * dbu  - 2 * activ_en_cont + cont_space) / (cont_width + cont_space))
    for n in range(3) :
        for m in range(ny_cont) :
            xc0 = int(int(xm[8] + 0.335 * dbu) + n * (cont_width + cont_space))
            yc0 = int(int(ym[0] + 1.515 * dbu) + m * (cont_width + cont_space))
            xc1 = int(xc0 + cont_width)
            yc1 = int(yc0 + cont_width)
            r = Rect(xc0, yc0, xc1, yc1)
            cont = cv.dbCreateRect(r, cont_layer)
            xc0 = int(int(xn0 + 5.165 * dbu) + n * (cont_width + cont_space))
            xc1 = int(xc0 + cont_width)
            r = Rect(xc0, yc0, xc1, yc1)
            cont = cv.dbCreateRect(r, cont_layer)
            xc0 = int(int(xm[0] + 0.335 * dbu) + n * (cont_width + cont_space))
            xc1 = int(xc0 + cont_width)
            r = Rect(xc0, yc0, xc1, yc1)
            cont = cv.dbCreateRect(r, cont_layer)
    #
    # Creating tap
    #
    xap = intarray(5)
    yap = intarray(5)
    xap[0] = int(xn0 - 0.9 * dbu)
    yap[0] = int(yn0 - 0.87 * dbu)
    xap[1] = int(xn1 + 0.87 * dbu)
    yap[1] = yap[0]
    xap[2] = xap[1]
    yap[2] = int(yn1 + 0.87* dbu)
    xap[3] = xap[0]
    yap[3] = yap[2]
    xap[4] = xap[0]
    yap[4] = yap[0]
    activ_path = cv.dbCreatePath(xap, yap, 5, activ_layer, int(0.48 * dbu), 2, int(0.24 * dbu), int(0.24 * dbu))
    n_points = 10
    xm = intarray(n_points)
    ym = intarray(n_points)
    xm[0] = int(xn0 - 1.56 * dbu)
    ym[0] = int(yn0 - 1.56 * dbu)
    xm[1] = int(xn1 + 1.53 * dbu)
    ym[1] = ym[0]
    xm[2] = xm[1]
    ym[2] = int(yn1 + 1.56 * dbu)
    xm[3] = xm[0]
    ym[3] = ym[2]
    xm[4] = xm[0]
    ym[4] = int(yn0 - 0.21 * dbu)
    xm[5] = int (xn0 - 0.21 * dbu)
    ym[5] = ym[4]
    xm[6] = xm[5]
    ym[6] = int(yn1 + 0.21 * dbu)
    xm[7] = int(xn1 + 0.21 * dbu)
    ym[7] = ym[6]
    xm[8] = xm[7]
    ym[8] = ym[4]
    xm[9] = xm[0]
    ym[9] = ym[4]
    metal1 = cv.dbCreatePolygon(xm, ym, n_points, metal1_layer)
    net = cv.dbCreateNet("VSS / sub")
    pin = cv.dbCreatePin("VSS / sub", net, DB_PIN_INOUT)
    cv.dbCreatePort(pin, metal1)
    psd = cv.dbCreatePolygon(xm, ym, n_points, psd_layer)
    n_cont = int((13.48 * dbu  - 2 * activ_en_cont + cont_space) / (cont_width + cont_space))
    for n in range(n_cont) :
        xc0 = int(xn0 - 0.92 * dbu + n * (cont_space + cont_width))
        yc0 = int(yn0 - 0.79 * dbu)
        xc1 = int(xc0 + cont_width)
        yc1 = int(yc0 - cont_width)
        r = Rect(xc0, yc0, xc1, yc1)
        cont = cv.dbCreateRect(r, cont_layer)
        yc0 = int(yn1 + 0.79 * dbu)
        yc1 = int(yc0 + cont_width)
        r = Rect(xc0, yc0, xc1, yc1)
        cont = cv.dbCreateRect(r, cont_layer)
    n_cont = int((34.77 * dbu  - 2 * activ_en_cont + cont_space) / (cont_width + cont_space))
    for n in range(n_cont) :
        xc0 = int(xn0 - 0.98 * dbu)
        yc0 = int(yn0 - 0.415 * dbu + n * (cont_space + cont_width))
        xc1 = int(xc0 + cont_width)
        yc1 = int(yc0 + cont_width)
        r = Rect(xc0, yc0, xc1, yc1)
        cont = cv.dbCreateRect(r, cont_layer)
        xc0 = int(xn1 + 0.79 * dbu)
        xc1 = int(xc0 + cont_width)
        r = Rect(xc0, yc0, xc1, yc1)
        cont = cv.dbCreateRect(r, cont_layer)
    p = Point(int(xn0 + 5.615 * dbu), int(yn0 - 0.87 * dbu))
    text = cv.dbCreateLabel(p, "VSS / sub!", R0, 0.2,  centreCentre, text_layer)
    #
    # Creating Cathode pin
    #
    n_points = 16
    xm = intarray(n_points)
    ym = intarray(n_points)
    xm[0] = int(xn0 + 0.38 * dbu)
    ym[0] = int(yn0 + 2.175 * dbu)
    xm[1] = int(xn1 + 2.75 * dbu)
    ym[1] = ym[0]
    xm[2] = xm[1]
    ym[2] = int(yn1 - 2.155 * dbu)
    xm[3] = xm[0]
    ym[3] = ym[2]
    xm[4] = xm[0]
    ym[4] = int(yn1 - 4.755 * dbu)
    xm[5] = int (xn1 - 0.85 * dbu)
    ym[5] = ym[4]
    xm[6] = xm[5]
    ym[6] = int(yn1 - 11.16 * dbu)
    xm[7] = xm[0]
    ym[7] = ym[6]
    xm[8] = xm[0]
    ym[8] = int(yn1 - 13.755 * dbu)
    xm[9] = xm[5]
    ym[9] = ym[8]
    xm[10] = xm[5]
    ym[10] = int(yn1 - 20.155 * dbu)
    xm[11] = xm[0]
    ym[11] = ym[10]
    xm[12] = xm[0]
    ym[12] = int(yn1 - 22.755 * dbu)
    xm[13] = xm[5]
    ym[13] = ym[12]
    xm[14] = xm[5]
    ym[14] = int(yn0 + 4.775 * dbu)
    xm[15] = xm[0]
    ym[15] = ym[14]
    metal2 = cv.dbCreatePolygon(xm, ym, n_points, metal2_layer)
    net = cv.dbCreateNet("VDD")
    pin = cv.dbCreatePin("VDD", net, DB_PIN_INOUT)
    cv.dbCreatePort(pin, metal2)
    n_via1 = int((2.6 * dbu  - 2 * metal_en_via + via_space) / (via_space + via_width))
    for n in range(3) :
        for m in range(n_via1) :
            xv0 = int(xn0 + 0.43 * dbu + n * (via_space + via_width))
            yv0 = int(yn0 + 2.18 * dbu + m * (via_space + via_width))
            xv1 = int(xv0 + via_width)
            yv1 = int(yv0 + via_width)
            r = Rect(xv0, yv0, xv1, yv1)
            via1 = cv.dbCreateRect(r, via1_layer)
            yv0 = int(yn0 + 11.18 * dbu + m * (via_space + via_width))
            yv1 = int(yv0 + via_width)
            r = Rect(xv0, yv0, xv1, yv1)
            via1 = cv.dbCreateRect(r, via1_layer)
            yv0 = int(yn1 - 13.75 * dbu + m * (via_space + via_width))
            yv1 = int(yv0 + via_width)
            r = Rect(xv0, yv0, xv1, yv1)
            via1 = cv.dbCreateRect(r, via1_layer)
            yv0 = int(yn1 - 4.75 * dbu + m * (via_space + via_width))
            yv1 = int(yv0 + via_width)
            r = Rect(xv0, yv0, xv1, yv1)
            via1 = cv.dbCreateRect(r, via1_layer)
            xv0 = int(xn0 + 5.005 * dbu + n * (via_space + via_width))
            yv0 = int(yn0 + 2.18 * dbu + m * (via_space + via_width))
            xv1 = int(xv0 + via_width)
            yv1 = int(yv0 + via_width)
            r = Rect(xv0, yv0, xv1, yv1)
            via1 = cv.dbCreateRect(r, via1_layer)
            yv0 = int(yn0 + 11.18 * dbu + m * (via_space + via_width))
            yv1 = int(yv0 + via_width)
            r = Rect(xv0, yv0, xv1, yv1)
            via1 = cv.dbCreateRect(r, via1_layer)
            yv0 = int(yn1 - 13.75 * dbu + m * (via_space + via_width))
            yv1 = int(yv0 + via_width)
            r = Rect(xv0, yv0, xv1, yv1)
            via1 = cv.dbCreateRect(r, via1_layer)
            yv0 = int(yn1 - 4.75 * dbu + m * (via_space + via_width))
            yv1 = int(yv0 + via_width)
            r = Rect(xv0, yv0, xv1, yv1)
            via1 = cv.dbCreateRect(r, via1_layer)
            xv0 = int(xn1 - 1.64 * dbu + n * (via_space + via_width))
            yv0 = int(yn0 + 2.18 * dbu + m * (via_space + via_width))
            xv1 = int(xv0 + via_width)
            yv1 = int(yv0 + via_width)
            r = Rect(xv0, yv0, xv1, yv1)
            via1 = cv.dbCreateRect(r, via1_layer)
            yv0 = int(yn0 + 11.18 * dbu + m * (via_space + via_width))
            yv1 = int(yv0 + via_width)
            r = Rect(xv0, yv0, xv1, yv1)
            via1 = cv.dbCreateRect(r, via1_layer)
            yv0 = int(yn1 - 13.75 * dbu + m * (via_space + via_width))
            yv1 = int(yv0 + via_width)
            r = Rect(xv0, yv0, xv1, yv1)
            via1 = cv.dbCreateRect(r, via1_layer)
            yv0 = int(yn1 - 4.75 * dbu + m * (via_space + via_width))
            yv1 = int(yv0 + via_width)
            r = Rect(xv0, yv0, xv1, yv1)
            via1 = cv.dbCreateRect(r, via1_layer)
    p = Point(int(xn1+ 0.68 * dbu), int(yn0 + 16.85 * dbu))
    text = cv.dbCreateLabel(p, "VDD", R0, 0.2,  bottomLeft, text_layer)
    #
    # Creating Anode pin
    #
    n_points = 12
    xm = intarray(n_points)
    ym = intarray(n_points)
    xm[0] = int(xn0 + 8.475 * dbu)
    ym[0] = int(yn0 + 6.195 * dbu)
    xm[1] = int(xn0 - 3.68 * dbu)
    ym[1] = ym[0]
    xm[2] = xm[1]
    ym[2] = int(yn1 - 6.175 * dbu)
    xm[3] = xm[0]
    ym[3] = ym[2]
    xm[4] = xm[0]
    ym[4] = int(yn1 - 9.735 * dbu)
    xm[5] = int(xn0 - 0.08 * dbu)
    ym[5] = ym[4]
    xm[6] = xm[5]
    ym[6] = int(yn1 - 15.175 * dbu)
    xm[7] = xm[0]
    ym[7] = ym[6]
    xm[8] = xm[0]
    ym[8] = int(yn1 - 18.735 * dbu)
    xm[9] = xm[5]
    ym[9] = ym[8]
    xm[10] = xm[5]
    ym[10] = int(yn0 +  9.755 * dbu)
    xm[11] = xm[0]
    ym[11] = ym[10]
    metal2 = cv.dbCreatePolygon(xm, ym, n_points, metal2_layer)
    metal2 = cv.dbCreatePolygon(xm, ym, n_points, metal2_layer)
    net = cv.dbCreateNet("PAD")
    pin = cv.dbCreatePin("PAD", net, DB_PIN_INOUT)
    cv.dbCreatePort(pin, metal2)
    n_via1 = int((3.56 * dbu  - 2 * metal_en_via + via_space) / (via_space + via_width))
    for n in range(3) :
        for m in range(n_via1) :
            xv0 = int(xn0 + 2.745 * dbu + n * (via_space + via_width))
            yv0 = int(yn0 + 6.2 * dbu + m * (via_space + via_width))
            xv1 = int(xv0 + via_width)
            yv1 = int(yv0 + via_width)
            r = Rect(xv0, yv0, xv1, yv1)
            via1 = cv.dbCreateRect(r, via1_layer)
            yv0 = int(yn0 + 15.27 * dbu + m * (via_space + via_width))
            yv1 = int(yv0 + via_width)
            r = Rect(xv0, yv0, xv1, yv1)
            via1 = cv.dbCreateRect(r, via1_layer)
            yv0 = int(yn1 - 9.73 * dbu + m * (via_space + via_width))
            yv1 = int(yv0 + via_width)
            r = Rect(xv0, yv0, xv1, yv1)
            via1 = cv.dbCreateRect(r, via1_layer)
            xv0 = int(xn0 + 7.275 * dbu + n * (via_space + via_width))
            yv0 = int(yn0 + 6.2 * dbu + m * (via_space + via_width))
            xv1 = int(xv0 + via_width)
            yv1 = int(yv0 + via_width)
            r = Rect(xv0, yv0, xv1, yv1)
            via1 = cv.dbCreateRect(r, via1_layer)
            yv0 = int(yn0 + 15.27 * dbu + m * (via_space + via_width))
            yv1 = int(yv0 + via_width)
            r = Rect(xv0, yv0, xv1, yv1)
            via1 = cv.dbCreateRect(r, via1_layer)
            yv0 = int(yn1 - 9.73 * dbu + m * (via_space + via_width))
            yv1 = int(yv0 + via_width)
            r = Rect(xv0, yv0, xv1, yv1)
            via1 = cv.dbCreateRect(r, via1_layer)
    p = Point(int(xm[1] + 1.55 * dbu), int(yn0 + 16.85 * dbu))
    text = cv.dbCreateLabel(p, "PAD", R0, 0.2,  bottomLeft, text_layer)
    #
    # Create recognition layer
    #
    xr0 = int(xn0 - 1.56 * dbu)
    yr0 = int(yn0 - 1.56 * dbu)
    xr1 = int(xn0 + 12.76* dbu)
    yr1 = int(yn1 + 1.56 * dbu)
    r = Rect(xr0, yr0, xr1, yr1)
    recog = cv.dbCreateRect(r, recog_layer)
    #
    # Save results
    #
    cv.update()