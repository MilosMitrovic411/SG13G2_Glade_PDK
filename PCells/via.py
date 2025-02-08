#
# Import the db 
#
from ui import *
#
# The entry point
#
def via(cv, x=2, y=1, w=0.29e-6, l=0.7e-6, selection_type=["x&y", "w&l"], via=["m1m2","am1", "pm1", "m2m3", "m3m4", "m4m5", "m5tm1", "tm1tm2"]) :
    lib = cv.lib()
    tech = lib.tech()
    dbu = lib.dbuPerUU()
    nx = int(x)
    ny = int(y)
    width = int(w * 1e9)
    length = int(l * 1e9)
    #
    # Layer rules
    #
    xygrid = int(0.005 * dbu)
    cont_width = int(0.16 * dbu)
    cont_space = int(0.18 * dbu)
    cont_space_matrix = int(0.2 * dbu)
    activ_en_cont = int(0.07 * dbu)
    gatepoly_en_cont = int(0.07 * dbu)
    metal1_en_cont = int(0.065 * dbu)
    via_width = int(0.19 * dbu)
    via_space = int(0.22 * dbu)
    via_space_matrix = int(0.29 * dbu)
    metal_en_via = int(0.05 * dbu)
    tvia1_width = int(0.42 * dbu)
    tvia1_space = int(0.42 * dbu)
    metal5_en_tvia1 = int(0.1 * dbu)
    tmetal1_en_tvia1 = int(0.42 * dbu)
    tvia2_width = int(0.9 * dbu)
    tvia2_space = int(1.06 * dbu)
    tmetal1_en_tvia2 = int(0.5 * dbu)
    tmetal2_en_tvia2 = int(0.5 * dbu)
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
    if (selection_type == "x&y") :
        if (nx < 1) :
            nx = 1
            cv.dbReplaceProp("x", nx)
        if (ny < 1) :
            ny = 1
            cv.dbReplaceProp("y", ny)
    if (selection_type == "w&l") :
        if ((via == "am1") or (via == "pm1")) :
            if (width < int(2 * activ_en_cont + cont_width)) :
                width = int(2 * activ_en_cont + cont_width)
                cv.dbReplaceProp("w", 1e-6 * width / dbu)
                cv.update()
            if (length < int(2 * activ_en_cont + cont_width)) :
                length = int(2 * activ_en_cont + cont_width)
                cv.dbReplaceProp("l", 1e-6 * length / dbu)
                cv.update()
        if ((via == "m1m2") or (via == "m2m3") or (via == "m3m4") or (via == "m4m5")) :
            if (width < int(2 * metal_en_via + via_width)) :
                width = int(2 * metal_en_via + via_width)
                cv.dbReplaceProp("w", 1e-6 * width / dbu)
                cv.update()
            if (length < int(2 * metal_en_via + via_width)) :
                length = int(2 * metal_en_via + via_width)
                cv.dbReplaceProp("l", 1e-6 * length / dbu)
                cv.update()
        if (via == "m5tm1")  :
            if (width < int(2 * tmetal1_en_tvia1 + tvia1_width)) :
                width = int(2 * tmetal1_en_tvia1 + tvia1_width)
                cv.dbReplaceProp("w", 1e-6 * width / dbu)
                cv.update()
            if (length < int(2 * tmetal1_en_tvia1 + tvia1_width)) :
                length = int(2 * tmetal1_en_tvia1 + tvia1_width)
                cv.dbReplaceProp("l", 1e-6 * length / dbu)
                cv.update()
        if (via == "tm1tm2")  :
            if (width < int(2 * tmetal2_en_tvia2 + tvia2_width)) :
                width = int(2 * tmetal2_en_tvia2 + tvia2_width)
                cv.dbReplaceProp("w", 1e-6 * width / dbu)
                cv.update()
            if (length < int(2 * tmetal2_en_tvia2 + tvia2_width)) :
                length = int(2 * tmetal2_en_tvia2 + tvia2_width)
                cv.dbReplaceProp("l", 1e-6 * length / dbu)
                cv.update()
    #
    # Creating the device
    #
    if (selection_type == "x&y") :
        nx = int(x)
        ny = int(y)
        if (via == "am1") :
            layer = tech.getLayerNum("Cont", "drawing")
            space = int(cont_space)
            if ((nx > 4) and (ny > 4)) :
                space = int(cont_space_matrix)
            for n in range(nx) :
                for m in range(ny) :
                    xc0 = int(n*(cont_width + space))
                    yc0 = int(m*(cont_width + space))
                    xc1 = int(xc0 + cont_width)
                    yc1 = int(yc0 + cont_width)
                    r = Rect(xc0, yc0, xc1, yc1)
                    cont = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("Activ", "drawing")
            xa0 = int(-activ_en_cont)
            ya0 = int(-activ_en_cont)
            xa1 = int(nx * (cont_width + space) - space + activ_en_cont)
            ya1 = int(ny * (cont_width + space) - space + activ_en_cont)
            r = Rect(xa0, ya0, xa1, ya1)
            activ = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("Metal1", "drawing")
            xm0 = int(-metal1_en_cont)
            ym0 = int(-metal1_en_cont)
            xm1 = int(nx * (cont_width + space) - space + metal1_en_cont)
            ym1 = int(ny * (cont_width + space) - space + metal1_en_cont)
            r = Rect(xm0, ym0, xm1, ym1)
            metal1 = cv.dbCreateRect(r, layer)
            width = int(ya1 - ya0)
            length = int(xa1 - xa0)
        if (via == "pm1") :
            layer = tech.getLayerNum("Cont", "drawing")
            space = int(cont_space)
            if ((nx > 4) and (ny > 4)) :
                space = int(cont_space_matrix)
            for n in range(nx) :
                for m in range(ny) :
                    xc0 = int(n*(cont_width + space))
                    yc0 = int(m*(cont_width + space))
                    xc1 = int(xc0 + cont_width)
                    yc1 = int(yc0 + cont_width)
                    r = Rect(xc0, yc0, xc1, yc1)
                    cont = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("GatPoly", "drawing")
            xp0 = int(-activ_en_cont)
            yp0 = int(-activ_en_cont)
            xp1 = int(nx * (cont_width + space) - space + gatepoly_en_cont)
            yp1 = int(ny * (cont_width + space) - space + gatepoly_en_cont)
            r = Rect(xp0, yp0, xp1, yp1)
            gatpoly = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("Metal1", "drawing")
            xm0 = int(-metal1_en_cont)
            ym0 = int(-metal1_en_cont)
            xm1 = int(nx * (cont_width + space) - space + metal1_en_cont)
            ym1 = int(ny * (cont_width + space) - space + metal1_en_cont)
            r = Rect(xm0, ym0, xm1, ym1)
            metal1 = cv.dbCreateRect(r, layer)
            width = int(yp1 - yp0)
            length = int(xp1 - xp0)
        if (via == "m1m2") :
            layer = tech.getLayerNum("Via1", "drawing")
            space = int(via_space)
            if ((nx > 3) and (ny > 3)) :
                space = int(via_space_matrix)
            for n in range(nx) :
                for m in range(ny) :
                    xv0 = int(n*(via_width + space))
                    yv0 = int(m*(via_width + space))
                    xv1 = int(xv0 + via_width)
                    yv1 = int(yv0 + via_width)
                    r = Rect(xv0, yv0, xv1, yv1)
                    via1 = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("Metal1", "drawing")
            xm0 = int(-metal_en_via)
            ym0 = int(-metal_en_via)
            xm1 = int(nx * (via_width + space) - space + metal_en_via)
            ym1 = int(ny * (via_width + space) - space + metal_en_via)
            r = Rect(xm0, ym0, xm1, ym1)
            metal1 = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("Metal2", "drawing")
            metal2 = cv.dbCreateRect(r, layer)
            width = int(ym1 - ym0)
            length = int(xm1 - xm0)
        if (via == "m2m3") :
            layer = tech.getLayerNum("Via2", "drawing")
            space = int(via_space)
            if ((nx > 3) and (ny > 3)) :
                space = int(via_space_matrix)
            for n in range(nx) :
                for m in range(ny) :
                    xv0 = int(n*(via_width + space))
                    yv0 = int(m*(via_width + space))
                    xv1 = int(xv0 + via_width)
                    yv1 = int(yv0 + via_width)
                    r = Rect(xv0, yv0, xv1, yv1)
                    via2 = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("Metal2", "drawing")
            xm0 = int(-metal_en_via)
            ym0 = int(-metal_en_via)
            xm1 = int(nx * (via_width + space) - space + metal_en_via)
            ym1 = int(ny * (via_width + space) - space + metal_en_via)
            r = Rect(xm0, ym0, xm1, ym1)
            metal2 = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("Metal3", "drawing")
            metal3 = cv.dbCreateRect(r, layer)
            width = int(ym1 - ym0)
            length = int(xm1 - xm0)
        if (via == "m3m4") :
            layer = tech.getLayerNum("Via3", "drawing")
            space = int(via_space)
            if ((nx > 3) and (ny > 3)) :
                space = int(via_space_matrix)
            for n in range(nx) :
                for m in range(ny) :
                    xv0 = int(n*(via_width + space))
                    yv0 = int(m*(via_width + space))
                    xv1 = int(xv0 + via_width)
                    yv1 = int(yv0 + via_width)
                    r = Rect(xv0, yv0, xv1, yv1)
                    via3 = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("Metal3", "drawing")
            xm0 = int(-metal_en_via)
            ym0 = int(-metal_en_via)
            xm1 = int(nx * (via_width + space) - space + metal_en_via)
            ym1 = int(ny * (via_width + space) - space + metal_en_via)
            r = Rect(xm0, ym0, xm1, ym1)
            metal3 = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("Metal4", "drawing")
            metal4 = cv.dbCreateRect(r, layer)
            width = int(ym1 - ym0)
            length = int(xm1 - xm0)
        if (via == "m4m5") :
            layer = tech.getLayerNum("Via4", "drawing")
            space = int(via_space)
            if ((nx > 3) and (ny > 3)) :
                space = int(via_space_matrix)
            for n in range(nx) :
                for m in range(ny) :
                    xv0 = int(n*(via_width + space))
                    yv0 = int(m*(via_width + space))
                    xv1 = int(xv0 + via_width)
                    yv1 = int(yv0 + via_width)
                    r = Rect(xv0, yv0, xv1, yv1)
                    via4 = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("Metal4", "drawing")
            xm0 = int(-metal_en_via)
            ym0 = int(-metal_en_via)
            xm1 = int(nx * (via_width + space) - space + metal_en_via)
            ym1 = int(ny * (via_width + space) - space + metal_en_via)
            r = Rect(xm0, ym0, xm1, ym1)
            metal4 = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("Metal5", "drawing")
            metal5 = cv.dbCreateRect(r, layer)
            width = int(ym1 - ym0)
            length = int(xm1 - xm0)
        if (via == "m5tm1") :
            layer = tech.getLayerNum("TopVia1", "drawing")
            for n in range(nx) :
                for m in range(ny) :
                    xv0 = int(n*(tvia1_width + tvia1_space))
                    yv0 = int(m*(tvia1_width + tvia1_space))
                    xv1 = int(xv0 + tvia1_width)
                    yv1 = int(yv0 + tvia1_width)
                    r = Rect(xv0, yv0, xv1, yv1)
                    topvia1 = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("Metal5", "drawing")
            xm50 = int(-metal5_en_tvia1)
            ym50 = int(-metal5_en_tvia1)
            xm51 = int(nx * (tvia1_width + tvia1_space) - tvia1_space + metal5_en_tvia1)
            ym51 = int(ny * (tvia1_width + tvia1_space) - tvia1_space + metal5_en_tvia1)
            r = Rect(xm50, ym50, xm51, ym51)
            metal5 = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("TopMetal1", "drawing")
            xtm10 = int(-tmetal1_en_tvia1)
            ytm10 = int(-tmetal1_en_tvia1)
            xtm11 = int(nx * (tvia1_width + tvia1_space) - tvia1_space + tmetal1_en_tvia1)
            ytm11 = int(ny * (tvia1_width + tvia1_space) - tvia1_space + tmetal1_en_tvia1)
            r = Rect(xtm10, ytm10, xtm11, ytm11)
            topmetal1 = cv.dbCreateRect(r, layer)
            width = int(ytm11 - ytm10)
            length = int(xtm11 - xtm10)
        if (via == "tm1tm2") :
            layer = tech.getLayerNum("TopVia2", "drawing")
            for n in range(nx) :
                for m in range(ny) :
                    xv0 = int(n*(tvia2_width + tvia2_space))
                    yv0 = int(m*(tvia2_width + tvia2_space))
                    xv1 = int(xv0 + tvia2_width)
                    yv1 = int(yv0 + tvia2_width)
                    r = Rect(xv0, yv0, xv1, yv1)
                    topvia2 = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("TopMetal1", "drawing")
            xtm0 = int(-tmetal1_en_tvia2)
            ytm0 = int(-tmetal1_en_tvia2)
            xtm1 = int(nx * (tvia2_width + tvia2_space) - tvia2_space + tmetal1_en_tvia2)
            ytm1 = int(ny * (tvia2_width + tvia2_space) - tvia2_space + tmetal1_en_tvia2)
            r = Rect(xtm0, ytm0, xtm1, ytm1)
            topmetal1 = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("TopMetal2", "drawing")
            topmetal2 = cv.dbCreateRect(r, layer)
            width = int(ytm1 - ytm0)
            length = int(xtm1 - xtm0)
        cv.dbReplaceProp("w", 1e-6 * (width / dbu))
        cv.dbReplaceProp("l", 1e-6 * (length / dbu))
    if (selection_type == "w&l") :
        width = int(w * 1.0e6 * dbu)
        length = int(l * 1.0e6 * dbu)
        if (via == "am1") :
            layer = tech.getLayerNum("Activ", "drawing")
            xa0 = 0
            ya0 = 0
            xa1 = int(length)
            ya1 = int(width)
            r = Rect(xa0, ya0, xa1, ya1)
            activ = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("Metal1", "drawing")
            xm0 = int(activ_en_cont - metal1_en_cont)
            ym0 = int(activ_en_cont - metal1_en_cont)
            xm1 = int(length - activ_en_cont + metal1_en_cont)
            ym1 = int(width - activ_en_cont + metal1_en_cont)
            r = Rect(xm0, ym0, xm1, ym1)
            metal1 = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("Cont", "drawing")
            space = int(cont_space)
            nx = int((length - 2 * activ_en_cont + space) / (cont_width + space))
            ny = int((width - 2 * activ_en_cont + space) / (cont_width + space))
            if ((nx > 4) and (ny > 4)) :
                space = int(cont_space_matrix)
                nx = int((length - 2 * activ_en_cont + space) / (cont_width + space))
                ny = int((width - 2 * activ_en_cont + space) / (cont_width + space))
            x_offset = int((length - (nx * (cont_width + space) - space)) / 2)
            y_offset = int((width - (ny * (cont_width + space) - space)) / 2)
            for n in range(nx) :
                for m in range(ny) :
                    xc0 = int(x_offset + n * (cont_width + space))
                    yc0 = int(y_offset + m * (cont_width + space))
                    xc1 = int(xc0 + cont_width)
                    yc1 = int(yc0 + cont_width)
                    r = Rect(xc0, yc0, xc1, yc1)
                    cont = cv.dbCreateRect(r, layer)
        if (via == "pm1") :
            layer = tech.getLayerNum("GatPoly", "drawing")
            xp0 = 0
            yp0 = 0
            xp1 = int(length)
            yp1 = int(width)
            r = Rect(xp0, yp0, xp1, yp1)
            gatpoly = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("Metal1", "drawing")
            xm0 = int(gatepoly_en_cont - metal1_en_cont)
            ym0 = int(gatepoly_en_cont - metal1_en_cont)
            xm1 = int(length - gatepoly_en_cont + metal1_en_cont)
            ym1 = int(width - gatepoly_en_cont + metal1_en_cont)
            r = Rect(xm0, ym0, xm1, ym1)
            metal1 = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("Cont", "drawing")
            space = int(cont_space)
            nx = int((length - 2 * gatepoly_en_cont + space) / (cont_width + space))
            ny = int((width - 2 * gatepoly_en_cont + space) / (cont_width + space))
            if ((nx > 4) and (ny > 4)) :
                space = int(cont_space_matrix)
                nx = int((length - 2 * gatepoly_en_cont + space) / (cont_width + space))
                ny = int((width - 2 * gatepoly_en_cont + space) / (cont_width + space))
            x_offset = int((length - (nx * (cont_width + space) - space)) / 2)
            y_offset = int((width - (ny * (cont_width + space) - space)) / 2)
            for n in range(nx) :
                for m in range(ny) :
                    xc0 = int(x_offset + n * (cont_width + space))
                    yc0 = int(y_offset + m * (cont_width + space))
                    xc1 = int(xc0 + cont_width)
                    yc1 = int(yc0 + cont_width)
                    r = Rect(xc0, yc0, xc1, yc1)
                    cont = cv.dbCreateRect(r, layer)
        if (via == "m1m2") :
            layer = tech.getLayerNum("Metal1", "drawing")
            r = Rect(0, 0, length, width)
            metal1 = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("Metal2", "drawing")
            metal2 = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("Via1", "drawing")
            space = int(via_space)
            nx = int((length - 2 * metal_en_via + space) / (via_width + space))
            ny = int((width - 2 * metal_en_via + space) / (via_width + space))
            if ((nx > 3) and (ny > 3)) :
                space = int(via_space_matrix)
                nx = int((length - 2 * metal_en_via + space) / (via_width + space))
                ny = int((width - 2 * metal_en_via + space) / (via_width + space))
            x_offset = int((length - (nx * (via_width + space) - space)) / 2)
            y_offset = int((width - (ny * (via_width + space) - space)) / 2)
            for n in range(nx) :
                for m in range(ny) :
                    xv0 = int(x_offset + n * (via_width + space))
                    yv0 = int(y_offset + m * (via_width + space))
                    xv1 = int(xv0 + via_width)
                    yv1 = int(yv0 + via_width)
                    r = Rect(xv0, yv0, xv1, yv1)
                    via1 = cv.dbCreateRect(r, layer)
        if (via == "m2m3") :
            layer = tech.getLayerNum("Metal2", "drawing")
            r = Rect(0, 0, length, width)
            metal2 = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("Metal3", "drawing")
            metal3 = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("Via2", "drawing")
            space = int(via_space)
            nx = int((length - 2 * metal_en_via + space) / (via_width + space))
            ny = int((width - 2 * metal_en_via + space) / (via_width + space))
            if ((nx > 3) and (ny > 3)) :
                space = int(via_space_matrix)
                nx = int((length - 2 * metal_en_via + space) / (via_width + space))
                ny = int((width - 2 * metal_en_via + space) / (via_width + space))
            x_offset = int((length - (nx * (via_width + space) - space)) / 2)
            y_offset = int((width - (ny * (via_width + space) - space)) / 2)
            for n in range(nx) :
                for m in range(ny) :
                    xv0 = int(x_offset + n * (via_width + space))
                    yv0 = int(y_offset + m * (via_width + space))
                    xv1 = int(xv0 + via_width)
                    yv1 = int(yv0 + via_width)
                    r = Rect(xv0, yv0, xv1, yv1)
                    via2 = cv.dbCreateRect(r, layer)
        if (via == "m3m4") :
            layer = tech.getLayerNum("Metal3", "drawing")
            r = Rect(0, 0, length, width)
            metal3 = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("Metal4", "drawing")
            metal4 = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("Via3", "drawing")
            space = int(via_space)
            nx = int((length - 2 * metal_en_via + space) / (via_width + space))
            ny = int((width - 2 * metal_en_via + space) / (via_width + space))
            if ((nx > 3) and (ny > 3)) :
                space = int(via_space_matrix)
                nx = int((length - 2 * metal_en_via + space) / (via_width + space))
                ny = int((width - 2 * metal_en_via + space) / (via_width + space))
            x_offset = int((length - (nx * (via_width + space) - space)) / 2)
            y_offset = int((width - (ny * (via_width + space) - space)) / 2)
            for n in range(nx) :
                for m in range(ny) :
                    xv0 = int(x_offset + n * (via_width + space))
                    yv0 = int(y_offset + m * (via_width + space))
                    xv1 = int(xv0 + via_width)
                    yv1 = int(yv0 + via_width)
                    r = Rect(xv0, yv0, xv1, yv1)
                    via3 = cv.dbCreateRect(r, layer)
        if (via == "m4m5") :
            layer = tech.getLayerNum("Metal4", "drawing")
            r = Rect(0, 0, length, width)
            metal4 = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("Metal5", "drawing")
            metal5 = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("Via4", "drawing")
            space = int(via_space)
            nx = int((length - 2 * metal_en_via + space) / (via_width + space))
            ny = int((width - 2 * metal_en_via + space) / (via_width + space))
            if ((nx > 3) and (ny > 3)) :
                space = int(via_space_matrix)
                nx = int((length - 2 * metal_en_via + space) / (via_width + space))
                ny = int((width - 2 * metal_en_via + space) / (via_width + space))
            x_offset = int((length - (nx * (via_width + space) - space)) / 2)
            y_offset = int((width - (ny * (via_width + space) - space)) / 2)
            for n in range(nx) :
                for m in range(ny) :
                    xv0 = int(x_offset + n * (via_width + space))
                    yv0 = int(y_offset + m * (via_width + space))
                    xv1 = int(xv0 + via_width)
                    yv1 = int(yv0 + via_width)
                    r = Rect(xv0, yv0, xv1, yv1)
                    via4 = cv.dbCreateRect(r, layer)
        if (via == "m5tm1") :
            layer = tech.getLayerNum("TopMetal1", "drawing")
            r = Rect(0, 0, length, width)
            topmetal1 = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("Metal5", "drawing")
            xm0 = int(tmetal1_en_tvia1 - metal5_en_tvia1)
            ym0 = int(tmetal1_en_tvia1 - metal5_en_tvia1)
            xm1 = int(length - tmetal1_en_tvia1 + metal5_en_tvia1)
            ym1 = int(width - tmetal1_en_tvia1 + metal5_en_tvia1)
            r = Rect(xm0, ym0, xm1, ym1)
            metal5 = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("TopVia1", "drawing")
            nx = int((length - 2 * tmetal1_en_tvia1 + tvia1_space) / (tvia1_width + tvia1_space))
            x_offset = int((length - (nx * (tvia1_width + tvia1_space) - tvia1_space)) / 2)
            ny = int((width - 2 * tmetal1_en_tvia1 + tvia1_space) / (tvia1_width + tvia1_space))
            y_offset = int((width - (ny * (tvia1_width + tvia1_space) - tvia1_space)) / 2)
            for n in range(nx) :
                for m in range(ny) :
                    xtv10 = int(x_offset + n * (tvia1_width + tvia1_space))
                    ytv10 = int(y_offset + m * (tvia1_width + tvia1_space))
                    xtv11 = int(xtv10 + tvia1_width)
                    ytv11 = int(ytv10 + tvia1_width)
                    r = Rect(xtv10, ytv10, xtv11, ytv11)
                    topvia1 = cv.dbCreateRect(r, layer)
        if (via == "tm1tm2") :
            layer = tech.getLayerNum("TopMetal1", "drawing")
            r = Rect(0, 0, length, width)
            topmetal1 = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("TopMetal2", "drawing")
            topmetal2 = cv.dbCreateRect(r, layer)
            layer = tech.getLayerNum("TopVia2", "drawing")
            nx = int((length - 2 * tmetal2_en_tvia2 + tvia2_space) / (tvia2_width + tvia2_space))
            x_offset = int((length - (nx * (tvia2_width + tvia2_space) - tvia2_space)) / 2)
            ny = int((width - 2 * tmetal2_en_tvia2 + tvia2_space) / (tvia2_width + tvia2_space))
            y_offset = int((width - (ny * (tvia2_width + tvia2_space) - tvia2_space)) / 2)
            for n in range(nx) :
                for m in range(ny) :
                    xtv10 = int(x_offset + n * (tvia2_width + tvia2_space))
                    ytv10 = int(y_offset + m * (tvia2_width + tvia2_space))
                    xtv11 = int(xtv10 + tvia2_width)
                    ytv11 = int(ytv10 + tvia2_width)
                    r = Rect(xtv10, ytv10, xtv11, ytv11)
                    topvia1 = cv.dbCreateRect(r, layer)
        cv.dbReplaceProp("x", nx)
        cv.dbReplaceProp("y", ny)
    #
    # Save results
    #
    cv.update()