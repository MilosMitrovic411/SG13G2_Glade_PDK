#
# Import the db 
#
from ui import *
#
# The entry point
#
def inmos(cv, w=0.15e-6, l=0.13e-6, nf=1, gate_contacts=["none", "bottom"], body_tie=["left", "left&right"], drain_metal=["m1", "m2", "m3"], source_metal=["m1", "m2", "m3"], bulk_metal=["m1", "m2", "m3"]) :
    lib = cv.lib()
    tech = lib.tech()
    dbu = lib.dbuPerUU()
    width = int(w * 1e9)
    length = int(l * 1e9)
    n_fingers = int(nf)
    #
    # Layer rules
    #
    xygrid = int(0.005 * dbu)
    nwell_width = int(0.62 * dbu)
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
    min_width = activ_width
    min_length = gatepoly_width
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
    if (n_fingers < 1) :
        n_fingers = 1
        cv.dbReplaceProp("nf", n_fingers)
        cv.update()
    #
    # Creating the device
    #
    # Create active diffusion
    activ_ex_offset = 0
    layer = tech.getLayerNum("Activ", "drawing")
    if (width < (2 * activ_en_cont + cont_width)) :
        gate_offset = int(2 * activ_en_cont + cont_width + 2 * gate_to_activ)
        activ_ex_offset = int(((2 * activ_en_cont + cont_width) - width) / 2)
        if activ_ex_offset%xygrid!=0 :
            activ_ex_offset = int(xygrid * int(activ_ex_offset / xygrid))
        for n in range(n_fingers + 1) :
            n_points = 12
            xa = intarray(n_points)
            ya = intarray(n_points)
            xa[0] = int(n * (length + gate_offset) + length)
            ya[0] = int(width)
            xa[1] = int(xa[0] - gate_to_activ - length)
            ya[1] = ya[0]
            xa[2] = xa[1]
            ya[2] = int(ya[1] + activ_ex_offset)
            xa[3] = int(xa[2] - 2 * activ_en_cont - cont_width)
            ya[3] = ya[2]
            xa[4] = xa[3]
            ya[4] = ya[0]
            xa[5] = int(xa[4] - gate_to_activ)
            ya[5] = ya[0]
            xa[6] = xa[5]
            ya[6] = 0
            xa[7] = xa[3]
            ya[7] = 0
            xa[8] = xa[3]
            ya[8] = int(-activ_ex_offset)
            xa[9] = xa[1]
            ya[9] = ya[8]
            xa[10] = xa[1]
            ya[10] = 0
            xa[11] = xa[0]
            ya[11] = ya[6]
            if (n == 0) :
                xa[5] = xa[3]
                xa[6] = xa[3]
            if (n == n_fingers) :
                xa[0] = xa[1]
                xa[11] = xa[1]
            activ = cv.dbCreatePolygon(xa, ya, n_points, layer) 
    else :
        gate_offset = int(2 * cont_activ_to_gatpoly + cont_width)
        xa0 = int(-(cont_activ_to_gatpoly + cont_width + activ_en_cont))
        ya0 = int(0)
        xa1 = int(n_fingers * (length + gate_offset) - cont_activ_to_gatpoly + activ_en_cont)
        ya1 = int(width)
        r = Rect(xa0, ya0, xa1, ya1)
        activ = cv.dbCreateRect(r, layer)
    # Create gate poly
    layer = tech.getLayerNum("GatPoly", "drawing")
    for n in range(n_fingers) :
        r = Rect(int(n * (length + gate_offset)), int(-gatepoly_ex_activ), int(n * (length + gate_offset) + length), int(width + gatepoly_ex_activ))
        gatpoly = cv.dbCreateRect(r, layer)
        net = cv.dbCreateNet("G")
        pin = cv.dbCreatePin("G", net, DB_PIN_INOUT)
        cv.dbCreatePort(pin, gatpoly)
    # Creating Gate contacts (if selected)
    if (gate_contacts == "bottom"):
        layer1 = tech.getLayerNum("Cont", "drawing")
        layer2 = tech.getLayerNum("Metal1", "drawing")
        layer3 = tech.getLayerNum("GatPoly", "drawing")
        if (length < (2 * gatepoly_en_cont + cont_width)) :
            gate_ex_offset = int(((2 * gatepoly_en_cont + cont_width) - length) / 2)
            for n in range(n_fingers) :
                xm0 = int(n * (length + gate_offset) - gate_ex_offset + gatepoly_en_cont - metal1_en_cont)
                ym0 = int(-(metal1_space + activ_ex_offset))
                xm1 = int(n * (length + gate_offset) + length + gate_ex_offset - gatepoly_en_cont + metal1_en_cont)
                ym1 = int(ym0 - metal1_width)
                r = Rect(xm0, ym0, xm1, ym1)
                metal1 = cv.dbCreateRect(r, layer2)
                xc0 = int(xm0 + metal1_en_cont)
                yc0 = int(ym0 - metal1_en_cont)
                xc1 = int(xc0 + cont_width)
                yc1 = int(yc0 - cont_width)
                r = Rect(xc0, yc0, xc1, yc1)
                cont = cv.dbCreateRect(r, layer1)
                xp0 = int(xc0 - gatepoly_en_cont)
                yp0 = int(yc0 + gatepoly_en_cont)
                xp1 = int(xc1 + gatepoly_en_cont)
                yp1 = int(yc1 - gatepoly_en_cont)
                r = Rect(xp0, yp0, xp1, yp1)
                gatpoly = cv.dbCreateRect(r, layer3)
                net = cv.dbCreateNet("G")
                pin = cv.dbCreatePin("G", net, DB_PIN_INOUT)
                cv.dbCreatePort(pin, gatpoly)
                xp0 = int(n * (length + gate_offset))
                yp0 = int(-gatepoly_ex_activ)
                xp1 = int(xp0 + length)
                yp1 = int(yc0 + gatepoly_en_cont)
                r = Rect(xp0, yp0, xp1, yp1)
                gatpoly = cv.dbCreateRect(r, layer3)
                net = cv.dbCreateNet("G")
                pin = cv.dbCreatePin("G", net, DB_PIN_INOUT)
                cv.dbCreatePort(pin, gatpoly)
        else :
            n_cont = int((length - 2 * gatepoly_en_cont + cont_space) / (cont_width + cont_space))
            s_cont = 0
            if (n_cont > 1) :
                s_cont = cont_space
            offset = int((length - (2 * gatepoly_en_cont + n_cont * (cont_width + s_cont) - s_cont)) / 2)
            for n in range(n_fingers) :
                xm0 = int(n * (length + gate_offset) + gatepoly_en_cont + offset - metal1_en_cont)
                ym0 = int(-(metal1_space + activ_ex_offset))
                xm1 = int(n * (length + gate_offset) + gatepoly_en_cont + offset + n_cont * (cont_width + cont_space) - cont_space + metal1_en_cont)
                ym1 = int(ym0 - metal1_width)
                r = Rect(xm0, ym0, xm1, ym1)
                metal1 = cv.dbCreateRect(r, layer2)
                xg0 = int(n * (length + gate_offset))
                yg0 = int(-gatepoly_ex_activ)
                xg1 = int(n * (length + gate_offset) + length)
                yg1 = int(ym1 + metal1_en_cont - gatepoly_en_cont)
                r = Rect(xg0, yg0, xg1, yg1)
                gatpoly = cv.dbCreateRect(r, layer3)
                net = cv.dbCreateNet("G")
                pin = cv.dbCreatePin("G", net, DB_PIN_INOUT)
                cv.dbCreatePort(pin, gatpoly)
                for m in range(n_cont) :
                    xc0 = int(n * (length + gate_offset) + gatepoly_en_cont + offset + m * (cont_width + s_cont))
                    yc0 = int(ym0 - metal1_en_cont)
                    xc1 = int(n * (length + gate_offset) + gatepoly_en_cont + offset + m * (cont_width + s_cont) + cont_width)
                    yc1 = int(yc0 - cont_width)
                    r = Rect(xc0, yc0, xc1, yc1)
                    cont = cv.dbCreateRect(r, layer1)
    # Create Drain and Soucre contacts
    layer = tech.getLayerNum("Cont", "drawing")
    s_cont = 0
    if (width < (2 * activ_en_cont + cont_width)) :
        cont_offset = int(gate_to_activ)
        x = 1
        y = 0
        n_cont = 1
        offset = 0
    else :
        n_cont = int((width - 2 * activ_en_cont + cont_space) / (cont_width + cont_space))
        cont_offset = 0
        x = 0
        y = 1
        if (n_cont > 1) :
            s_cont = cont_space
        offset = int((width - (2 * activ_en_cont + n_cont * (cont_width + s_cont) - s_cont)) / 2)
    for n in range(n_cont) :
        for m in range(n_fingers + 1) :
            r = Rect(int(m * (length + gate_offset)-(y * cont_activ_to_gatpoly + cont_width + cont_offset + x * activ_en_cont)), int(activ_en_cont + offset + n * (cont_width + s_cont) - activ_ex_offset), int(m * (length + gate_offset) - y * cont_activ_to_gatpoly - cont_offset - x * activ_en_cont), int(activ_en_cont + offset + cont_width + n * (cont_width + s_cont) - activ_ex_offset))
            cont = cv.dbCreateRect(r, layer)
    # Create metalization over Soucre and Drain
    for n in range(n_fingers + 1) :
        layer = tech.getLayerNum("Metal1", "drawing")
        xm0 = int(n * (length + gate_offset)-(y * cont_activ_to_gatpoly + cont_width + metal1_en_cont + cont_offset + x * activ_en_cont))
        ym0 = int(-activ_ex_offset)
        xm1 = int(xm0 + metal1_width)
        ym1 = int(width + activ_ex_offset)
        r = Rect(xm0, ym0, xm1, ym1)
        metal1 = cv.dbCreateRect(r, layer)
        if n%2==0 :
            net = cv.dbCreateNet("S")
            pin = cv.dbCreatePin("S", net, DB_PIN_INOUT)
            cv.dbCreatePort(pin, metal1)
            if ((source_metal == "m2") or (source_metal == "m3")) :
                layer = tech.getLayerNum("Metal2", "drawing")
                r = Rect(xm0, ym0, xm1, ym1)
                metal2 = cv.dbCreateRect(r, layer)
                layer = tech.getLayerNum("Via1", "drawing")
                n_via = int(((ym1 - ym0) - 2 * metal_en_via + via_space) / (via_width + via_space))
                via_offset = int(((ym1 - ym0) - (2 * metal_en_via + n_via * (via_width + via_space) - via_space)) / 2)
                for m in range(n_via) :
                    xv0 = int(xm0 + metal_en_via)
                    yv0 = int(ym0 + metal_en_via + m * (via_width + via_space) + via_offset)
                    xv1 = int(xm1 - metal_en_via)
                    yv1 = int(yv0 + via_width)
                    r = Rect(xv0, yv0, xv1, yv1)
                    via1 = cv.dbCreateRect(r, layer)
            if (source_metal == "m3") :
                layer = tech.getLayerNum("Metal3", "drawing")
                r = Rect(xm0, ym0, xm1, ym1)
                metal2 = cv.dbCreateRect(r, layer)
                layer = tech.getLayerNum("Via2", "drawing")
                for m in range(n_via) :
                    xv0 = int(xm0 + metal_en_via)
                    yv0 = int(ym0 + metal_en_via + m * (via_width + via_space) + via_offset)
                    xv1 = int(xm1 - metal_en_via)
                    yv1 = int(yv0 + via_width)
                    r = Rect(xv0, yv0, xv1, yv1)
                    via2 = cv.dbCreateRect(r, layer)
        else :
            net = cv.dbCreateNet("D")
            pin = cv.dbCreatePin("D", net, DB_PIN_INOUT)
            cv.dbCreatePort(pin, metal1)
            if ((drain_metal == "m2") or (drain_metal == "m3")) :
                layer = tech.getLayerNum("Metal2", "drawing")
                r = Rect(xm0, ym0, xm1, ym1)
                metal2 = cv.dbCreateRect(r, layer)
                layer = tech.getLayerNum("Via1", "drawing")
                n_via = int(((ym1 - ym0) - 2 * metal_en_via + via_space) / (via_width + via_space))
                via_offset = int(((ym1 - ym0) - (2 * metal_en_via + n_via * (via_width + via_space) - via_space)) / 2)
                for m in range(n_via) :
                    xv0 = int(xm0 + metal_en_via)
                    yv0 = int(ym0 + metal_en_via + m * (via_width + via_space) + via_offset)
                    xv1 = int(xm1 - metal_en_via)
                    yv1 = int(yv0 + via_width)
                    r = Rect(xv0, yv0, xv1, yv1)
                    via1 = cv.dbCreateRect(r, layer)
            if (drain_metal == "m3") :
                layer = tech.getLayerNum("Metal3", "drawing")
                r = Rect(xm0, ym0, xm1, ym1)
                metal2 = cv.dbCreateRect(r, layer)
                layer = tech.getLayerNum("Via2", "drawing")
                for m in range(n_via) :
                    xv0 = int(xm0 + metal_en_via)
                    yv0 = int(ym0 + metal_en_via + m * (via_width + via_space) + via_offset)
                    xv1 = int(xm1 - metal_en_via)
                    yv1 = int(yv0 + via_width)
                    r = Rect(xv0, yv0, xv1, yv1)
                    via2 = cv.dbCreateRect(r, layer)
    # Creating body tie (bulk)
    layer = tech.getLayerNum("pSD", "drawing")
    xp0 = int(-(y * cont_activ_to_gatpoly + cont_width + cont_offset + x * activ_en_cont + metal1_space + metal1_width + activ_en_cont + psd_en_activ))
    yp0 = int(-(activ_ex_offset + psd_en_activ))
    xp1 = int(-(y * cont_activ_to_gatpoly + cont_width + cont_offset + x * activ_en_cont + metal1_space + metal1_width + activ_en_cont - activ_en_cont - cont_width - psd_en_cont))
    yp1 = int(width + activ_ex_offset + psd_en_activ)
    r = Rect(xp0, yp0, xp1, yp1)
    psd = cv.dbCreateRect(r, layer)
    layer = tech.getLayerNum("Activ", "drawing")
    xa0 = int(-(y * cont_activ_to_gatpoly + cont_width + cont_offset + x * activ_en_cont + metal1_space + metal1_width + activ_en_cont))
    ya0 = int(-activ_ex_offset)
    xa1 = int(x * gate_to_activ - gate_offset + y * (cont_activ_to_gatpoly - activ_en_cont))
    ya1 = int(width + activ_ex_offset)
    r = Rect(xa0, ya0, xa1, ya1)
    activ = cv.dbCreateRect(r, layer)
    layer = tech.getLayerNum("Cont", "drawing")
    for n in range(n_cont) :
        xc0 = int(-(y * cont_activ_to_gatpoly + cont_width + cont_offset + x * activ_en_cont + metal1_space + metal1_width))
        yc0 = int(activ_en_cont + offset + n * (cont_width + s_cont) - activ_ex_offset)
        xc1 = int(-(y * cont_activ_to_gatpoly + cont_offset + x * activ_en_cont + metal1_space + metal1_width))
        yc1 = int(activ_en_cont + offset + cont_width + n * (cont_width + s_cont) - activ_ex_offset)
        r = Rect(xc0, yc0, xc1, yc1)
        cont = cv.dbCreateRect(r, layer)
    layer = tech.getLayerNum("Metal1", "drawing")
    xm0 = int(-(y * cont_activ_to_gatpoly + cont_width + metal1_en_cont + cont_offset + x * activ_en_cont + metal1_space + metal1_width))
    ym0 = int(-activ_ex_offset)
    xm1 = int(-(y * cont_activ_to_gatpoly + cont_width + metal1_en_cont + cont_offset + x * activ_en_cont + metal1_space))
    ym1 = int(width + activ_ex_offset)
    r = Rect(xm0, ym0, xm1, ym1)
    metal1 = cv.dbCreateRect(r, layer)
    net = cv.dbCreateNet("B")
    pin = cv.dbCreatePin("B", net, DB_PIN_INOUT)
    cv.dbCreatePort(pin, metal1)
    if ((bulk_metal == "m2") or (bulk_metal == "m3")) :
        layer = tech.getLayerNum("Metal2", "drawing")
        r = Rect(xm0, ym0, xm1, ym1)
        metal2 = cv.dbCreateRect(r, layer)
        layer = tech.getLayerNum("Via1", "drawing")
        n_via = int(((ym1 - ym0) - 2 * metal_en_via + via_space) / (via_width + via_space))
        via_offset = int(((ym1 - ym0) - (2 * metal_en_via + n_via * (via_width + via_space) - via_space)) / 2)
        for n in range(n_via) :
            xv0 = int(xm0 + metal_en_via)
            yv0 = int(ym0 + metal_en_via + n * (via_width + via_space) + via_offset)
            xv1 = int(xm1 - metal_en_via)
            yv1 = int(yv0 + via_width)
            r = Rect(xv0, yv0, xv1, yv1)
            via1 = cv.dbCreateRect(r, layer)
    if (bulk_metal == "m3") :
        layer = tech.getLayerNum("Metal3", "drawing")
        r = Rect(xm0, ym0, xm1, ym1)
        metal2 = cv.dbCreateRect(r, layer)
        layer = tech.getLayerNum("Via2", "drawing")
        for n in range(n_via) :
            xv0 = int(xm0 + metal_en_via)
            yv0 = int(ym0 + metal_en_via + n * (via_width + via_space) + via_offset)
            xv1 = int(xm1 - metal_en_via)
            yv1 = int(yv0 + via_width)
            r = Rect(xv0, yv0, xv1, yv1)
            via2 = cv.dbCreateRect(r, layer)
    if (body_tie == "left&right") :
        layer = tech.getLayerNum("Metal1", "drawing")
        xm0 = int(n_fingers * (length + gate_offset) - y * cont_activ_to_gatpoly + metal1_en_cont - cont_offset - x * activ_en_cont + metal1_space)
        ym0 = int(-activ_ex_offset)
        xm1 = int(n_fingers * (length + gate_offset) - y * cont_activ_to_gatpoly + metal1_en_cont - cont_offset - x * activ_en_cont + metal1_space + metal1_width)
        ym1 = int(width + activ_ex_offset)
        r = Rect(xm0, ym0, xm1, ym1)
        metal1 = cv.dbCreateRect(r, layer)
        net = cv.dbCreateNet("B")
        pin = cv.dbCreatePin("B", net, DB_PIN_INOUT)
        cv.dbCreatePort(pin, metal1)
        layer = tech.getLayerNum("Cont", "drawing")
        for n in range(n_cont) :
            xc0 = int(xm0 + metal1_en_cont)
            yc0 = int(activ_en_cont + offset + n * (cont_width + s_cont) - activ_ex_offset)
            xc1 = int(xm1 - metal1_en_cont)
            yc1 = int(activ_en_cont + offset + cont_width + n * (cont_width + s_cont) - activ_ex_offset)
            r = Rect(xc0, yc0, xc1, yc1)
            cont = cv.dbCreateRect(r, layer)
        layer = tech.getLayerNum("Activ", "drawing")
        xa0 = int(n_fingers * (length + gate_offset) - cont_activ_to_gatpoly + activ_en_cont)
        if (width < (2 * activ_en_cont + cont_width)) :
            xa0 = int(n_fingers * (length + gate_offset) - gate_to_activ)
        ya0 = int(-activ_ex_offset)
        xa1 = int(xc1 + activ_en_cont)
        ya1 = int(width + activ_ex_offset)
        r = Rect(xa0, ya0, xa1, ya1)
        activ = cv.dbCreateRect(r, layer)
        layer = tech.getLayerNum("pSD", "drawing")
        xp0 = int(xc0 - psd_en_cont)
        yp0 = int(-(activ_ex_offset + psd_en_activ))
        xp1 = int(xa1 + psd_en_activ)
        yp1 = int(width + activ_ex_offset + psd_en_activ)
        r = Rect(xp0, yp0, xp1, yp1)
        psd = cv.dbCreateRect(r, layer)
        if ((bulk_metal == "m2") or (bulk_metal == "m3")) :
            layer = tech.getLayerNum("Metal2", "drawing")
            r = Rect(xm0, ym0, xm1, ym1)
            metal2 = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("Via1", "drawing")
            n_via = int(((ym1 - ym0) - 2 * metal_en_via + via_space) / (via_width + via_space))
            via_offset = int(((ym1 - ym0) - (2 * metal_en_via + n_via * (via_width + via_space) - via_space)) / 2)
            for n in range(n_via) :
                xv0 = int(xm0 + metal_en_via)
                yv0 = int(ym0 + metal_en_via + n * (via_width + via_space) + via_offset)
                xv1 = int(xm1 - metal_en_via)
                yv1 = int(yv0 + via_width)
                r = Rect(xv0, yv0, xv1, yv1)
                via1 = cv.dbCreateRect(r, layer)
        if (bulk_metal == "m3") :
            layer = tech.getLayerNum("Metal3", "drawing")
            r = Rect(xm0, ym0, xm1, ym1)
            metal2 = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("Via2", "drawing")
            for n in range(n_via) :
                xv0 = int(xm0 + metal_en_via)
                yv0 = int(ym0 + metal_en_via + n * (via_width + via_space) + via_offset)
                xv1 = int(xm1 - metal_en_via)
                yv1 = int(yv0 + via_width)
                r = Rect(xv0, yv0, xv1, yv1)
                via2 = cv.dbCreateRect(r, layer)
    # Create N-buried Layer
    layer = tech.getLayerNum("nBuLay", "drawing")
    xnbl0 = int(-(y * cont_activ_to_gatpoly + cont_width + metal1_en_cont + cont_offset + x * activ_en_cont + metal1_space + metal1_width - metal1_en_cont + activ_en_cont + nbulay_en_activ))
    ynbl0 = int(-(nbulay_en_activ + activ_ex_offset))
    xnbl1 = int(n_fingers * (length + gate_offset) - gate_offset + cont_activ_to_gatpoly + cont_width + activ_en_cont + nbulay_en_activ)
    ynbl1 = int(width + activ_ex_offset + nbulay_en_activ)
    if (body_tie == "left&right") :
        xnbl1 = (xa1 + nbulay_en_activ)
    if (gate_contacts == "bottom") :
        ynbl0 = int(-(metal1_space + 2 * activ_ex_offset + metal1_en_cont + cont_width + gatepoly_en_cont + nbulay_en_activ - gatepoly_ex_activ))
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
    n_layer = tech.getLayerNum("NWell", "drawing")
    a_layer = tech.getLayerNum("Activ", "drawing")
    m_layer = tech.getLayerNum("Metal1", "drawing")
    xmpp = intarray(4)
    ympp = intarray(4)
    xmpp[0] = int(xnbl0 + nwell_en_nsd_activ + activ_en_cont + cont_width / 2)
    ympp[0] = int(ynbl0 + nwell_en_nsd_activ + activ_en_cont + cont_width / 2)
    xmpp[1] = int(xnbl1 - nwell_en_nsd_activ - activ_en_cont - cont_width / 2)
    ympp[1] = ympp[0]
    xmpp[2] = xmpp[1]
    ympp[2] = int(ynbl1 - nwell_en_nsd_activ - activ_en_cont - cont_width / 2)
    xmpp[3] = xmpp[0]
    ympp[3] = ympp[2]
    xmpp[4] = xmpp[0]
    ympp[4] = ympp[0]
    n_path = cv.dbCreatePath(xmpp, ympp, 5, n_layer, int(2 * activ_en_cont + cont_width + 2 * nwell_en_nsd_activ), 2, int(metal1_width / 2), int((2 * activ_en_cont + cont_width + 2 * nwell_en_nsd_activ) / 2))
    a_path = cv.dbCreatePath(xmpp, ympp, 5, a_layer, int(2 * activ_en_cont + cont_width), 2, int(metal1_width / 2), int((2 * activ_en_cont + cont_width) / 2))
    m_path = cv.dbCreatePath(xmpp, ympp, 5, m_layer, metal1_width, 2, int(metal1_width / 2), int(metal1_width / 2))
    net = cv.dbCreateNet("Iso")
    pin = cv.dbCreatePin("Iso", net, DB_PIN_INOUT)
    cv.dbCreatePort(pin, m_path)
    c_layer = tech.getLayerNum("Cont", "drawing")
    a_width = int((xnbl1 - xnbl0) - 2 * nwell_en_nsd_activ - 2 * activ_en_cont)
    a_length = int((ynbl1 - ynbl0) - 2 * nwell_en_nsd_activ - 2 * activ_en_cont)
    n_cont_w1 = int((a_width + cont_space) / (cont_width + cont_space))
    n_cont_l1 = int((a_length - cont_width) / (cont_width + cont_space))
    n_cont_w2 = int((a_width - cont_width) / (cont_width + cont_space))
    n_cont_l2 = int((a_length - 2 * cont_width - cont_space) / (cont_width + cont_space))
    for n in range(n_cont_w1) :
        xc0 = int(xnbl0 + nwell_en_nsd_activ + activ_en_cont + n * (cont_width + cont_space))
        yc0 = int(ynbl1 - nwell_en_nsd_activ - activ_en_cont - cont_width)
        xc1 = int(xc0 + cont_width)
        yc1 = int(yc0 + cont_width)
        r = Rect(xc0, yc0, xc1, yc1)
        cont = cv.dbCreateRect(r, c_layer)
    for n in range(n_cont_l1) :
        xc0 = int(xnbl1 - nwell_en_nsd_activ - activ_en_cont - cont_width)
        yc0 = int(ynbl1 - nwell_en_nsd_activ - activ_en_cont - cont_width - cont_space - n * (cont_width + cont_space))
        xc1 = int(xc0 + cont_width)
        yc1 = int(yc0 - cont_width)
        r = Rect(xc0, yc0, xc1, yc1)
        cont = cv.dbCreateRect(r, c_layer)
    for n in range(n_cont_w2) :
        xc0 = int(xnbl1 - nwell_en_nsd_activ - activ_en_cont - cont_width - cont_space - n * (cont_width + cont_space))
        yc0 = int(ynbl0 + nwell_en_nsd_activ + activ_en_cont)
        xc1 = int(xc0 - cont_width)
        yc1 = int(yc0 + cont_width)
        r = Rect(xc0, yc0, xc1, yc1)
        cont = cv.dbCreateRect(r, c_layer)
    for n in range(n_cont_l2) :
        xc0 = int(xnbl0 + nwell_en_nsd_activ + activ_en_cont)
        yc0 = int(ynbl0 + nwell_en_nsd_activ + activ_en_cont + cont_width + cont_space + n * (cont_width + cont_space))
        xc1 = int(xc0 + cont_width)
        yc1 = int(yc0 + cont_width)
        r = Rect(xc0, yc0, xc1, yc1)
        cont = cv.dbCreateRect(r, c_layer)
    # mpp = cv.dbCreateMPP(xmpp, ympp, 4)
    # layer = tech.getLayerNum("Metal1", "drawing")
    # mpp.setNumLayers(1) 
    # n_layers = mpp.numLayers()
    # metal_layer = tech.getLayerName(layer)
    # print(metal_layer)
    # mpp.setLayers(metal_layer, n_layers)
    # print(n_layers)
    #
    # Add device type
    #
    cv.dbAddProp("type", "mos")
    cv.dbAddProp("nf", 1)
    #
    # Save results
    #
    cv.update()