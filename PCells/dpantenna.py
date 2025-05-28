#
# Import the db 
#
from ui import *
#
# The entry point
#
def dpantenna(cv, Width=0.78e-6, Length=0.78e-6, type="dio", model="dpantenna" ) :
    lib = cv.lib()
    tech = lib.tech()
    dbu = lib.dbuPerUU()
    w = max(int(Width * 1e6 * dbu), int(Width * 1e9))
    l = max(int(Length * 1e6 * dbu), int(Length * 1e9))
    #
    # Layer rules
    #
    xygrid = int(0.005 * dbu)
    activ_en_cont = int(0.07 * dbu)
    cont_width = int(0.16 * dbu)
    cont_space = int(0.18 * dbu)
    cont_matrix_space = int(0.2 * dbu)
    extblock_en_activ = int(0.02 * dbu)
    metal1_en_cont = int(0.0 * dbu)
    psd_en_activ = int(0.18 * dbu)
    nwell_en_activ = int(0.31 * dbu)
    #
    # Checking parameters
    #
    if (w < int(0.78 * dbu)) :
        w = int(0.78 * dbu)
        cv.dbReplaceProp("Width", 1e-6 * (w / dbu))
        cv.update()
    if (l < int(0.78 * dbu)) :
        l = int(0.78 * dbu)
        cv.dbReplaceProp("Length", 1e-6 * (l / dbu))
        cv.update()
    if (w%xygrid!=0) :
        w = int(xygrid * int(w / xygrid))
        cv.dbReplaceProp("Width", 1e-6 * (w / dbu))
        cv.update()
    if (l%xygrid!=0) :
        l = int(xygrid * int(l / xygrid))
        cv.dbReplaceProp("Length", 1e-6 * (l / dbu))
        cv.update()
    #
    # Creating the device
    #
    cont_layer = tech.getLayerNum("Cont", "drawing")
    activ_layer = tech.getLayerNum("Activ", "drawing")
    extblock_layer = tech.getLayerNum("EXTBlock", "drawing")
    metal_layer = tech.getLayerNum("Metal1", "drawing")
    text_layer = tech.getLayerNum("TEXT", "drawing")
    psd_layer = tech.getLayerNum("pSD", "drawing")
    nwell_layer = tech.getLayerNum("NWell", "drawing")
    # Create activ
    xa0 = 0
    ya0 = 0
    xa1 = l
    ya1 = w
    r = Rect(xa0, ya0, xa1, ya1)
    activ = cv.dbCreateRect(r, activ_layer)
    #
    xe0 = int(-extblock_en_activ)
    ye0 = int(-extblock_en_activ)
    xe1 = int(l + extblock_en_activ)
    ye1 = int(w + extblock_en_activ)
    r = Rect(xe0, ye0, xe1, ye1)
    extblock = cv.dbCreateRect(r, extblock_layer)
    # Create contacts
    space = cont_space
    n_contx = int((l - 2 * activ_en_cont + space) / (cont_width + space))
    n_conty = int((w- 2 * activ_en_cont + space) / (cont_width + space))
    if ((n_contx > 3) or (n_conty > 3)) :
        space = cont_matrix_space
        n_contx = int((l - 2 * activ_en_cont + space) / (cont_width + space))
        n_conty = int((w- 2 * activ_en_cont + space) / (cont_width + space))
    xoffset = int((l - n_contx * (cont_width + space) + space) / 2)
    yoffset = int((w - n_conty * (cont_width + space) + space) / 2)
    for n in range (n_contx) :
        for m in range(n_conty) :
            xc0 = int(xoffset + n * (cont_width + space))
            yc0 = int(yoffset + m * (cont_width + space))
            xc1 = int(xc0 + cont_width)
            yc1 = int(yc0 + cont_width)
            r = Rect(xc0, yc0, xc1, yc1)
            cont = cv.dbCreateRect(r, cont_layer)
    # Create metalization
    xm0 = int(xoffset)
    ym0 = int(yoffset)
    xm1 = int(l - xoffset)
    ym1 = int(w - yoffset)
    r = Rect(xm0, ym0, xm1, ym1)
    metal = cv.dbCreateRect(r, metal_layer)
    # Create psd
    xp0 = int(- psd_en_activ)
    yp0 = int(- psd_en_activ)
    xp1 = int(l + psd_en_activ)
    yp1 = int(w + psd_en_activ)
    r = Rect(xp0, yp0, xp1, yp1)
    psd = cv.dbCreateRect(r, psd_layer)
    # Create nwell
    xn0 = int(- nwell_en_activ)
    yn0 = int(- nwell_en_activ)
    xn1 = int(l + nwell_en_activ)
    yn1 = int(w + nwell_en_activ)
    r = Rect(xn0, yn0, xn1, yn1)
    nwell = cv.dbCreateRect(r, nwell_layer)
    # Create label
    p = Point(int(l / 2), int(w / 2))
    text = cv.dbCreateLabel(p, "dpant", R0, 0.2,  centreCentre, text_layer)    
    #
    # Save results
    #
    cv.update()