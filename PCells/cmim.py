#
# Import the db 
#
from ui import *
#
# The entry point
#
def cmim(cv, capacitance=1.95e-15, width=1.14e-6, length=1.14e-6, calculate=["L", "C"], contacts=["none", "width", "length", "full"], type="cap", modelName="cap_cmim") :
    lib = cv.lib()
    tech = lib.tech()
    dbu = lib.dbuPerUU()
    width = max(int(width * 1e6 * dbu), int(width * 1e9))
    cap = max(int(capacitance * 1e15 * dbu), int(capacitance * 1e18))
    length = int(cap / (width * 1.5 / dbu))
    if (calculate == "L") : 
        length = int(cap / (width * 1.5 / dbu))
        cv.dbReplaceProp("length", 1e-6 * length / dbu)
        cv.update()
    if (calculate == "C") :
        length = max(int(l * 1e6 * dbu), int(l * 1e9))
        cap = float(width * length * 1.5 / (dbu * dbu))
        cv.dbReplaceProp("capacitance", 1e-15 * cap)
        cv.update()
    area = int(width * length)
    #
    # Layer rules
    #
    xygrid = int(0.005 * dbu)
    mim_width = int(1.14 * dbu)
    metal5_en_mim = int(0.6 * dbu)
    mim_en_topvia1 = int(0.36 * dbu)
    topvia1_width = int(0.42 * dbu)
    topvia1_space = int(0.42 * dbu)
    topmetal1_width = int(1.64 * dbu)
    topmetal1_en_topvia1 = int(0.61 * dbu)
    min_topmetal1_en_topvia1 = int(0.42 * dbu)
    #
    # Device rules
    #
    min_width = mim_width
    min_length = mim_width
    max_mim_area = int(5625 * dbu * dbu)
    #
    # Checking parameters
    #
    if width%xygrid!=0 :
        width = int(xygrid * int(width / xygrid))
        cv.dbReplaceProp("width", 1e-6 * (width / dbu))
        cv.update()
    if length%xygrid!=0 :
        length = int(xygrid * int(length / xygrid))
        cv.dbReplaceProp("length", 1e-6 * (length / dbu))
        cv.update()
    if width < min_width :
        width = min_width
        cv.dbReplaceProp("width", 1e-6 * (width / dbu))
        cv.update()
    if length < min_length :
        length = min_length
        cv.dbReplaceProp("length", 1e-6 * (length / dbu))
        cv.update()
    if area > max_mim_area :
        length = int(max_mim_area / width)
        if length%xygrid!=0 :
            length = int(xygrid * int(length / xygrid))
        cv.dbReplaceProp("length", 1e-6 * (length / dbu))
        cv.update()
    #
    # Creating the device
    #
    # Create Metal5 plate
    layer = tech.getLayerNum("Metal5", "drawing")
    r = Rect(int(-metal5_en_mim), int(-metal5_en_mim), int(length + metal5_en_mim), int(width + metal5_en_mim))
    metal5 = cv.dbCreateRect(r, layer)
    net = cv.dbCreateNet("MINUS")
    pin = cv.dbCreatePin("MINUS", net, DB_PIN_INOUT)
    cv.dbCreatePort(pin, metal5)
    # Create MIM plate
    layer = tech.getLayerNum("MIM", "drawing")
    r = Rect(0, 0, int(length), int(width))
    mim = cv.dbCreateRect(r, layer)
    if (contacts == "none") :
        net = cv.dbCreateNet("PLUS")
        pin = cv.dbCreatePin("PLUS", net, DB_PIN_INOUT)
        cv.dbCreatePort(pin, mim)
    # Create contacts and metalization over them
    if (contacts == "width") :
        layer = tech.getLayerNum("TopVia1", "drawing")
        n_cont = int((width - 2 * mim_en_topvia1 + topvia1_space) / (topvia1_width + topvia1_space))
        s_cont = 0
        top_en_via = topmetal1_en_topvia1
        if (n_cont > 1) :
            s_cont = topvia1_space
            top_en_via = min_topmetal1_en_topvia1
        offset = abs(int((width - (2 * mim_en_topvia1 + n_cont * (topvia1_width + s_cont) - s_cont)) / 2))
        if offset%xygrid!=0 :
            offset = int(xygrid * int(offset / xygrid))
        for n in range(n_cont) :
            xc0 = int(mim_en_topvia1)
            yc0 = int(mim_en_topvia1 + offset + n * (topvia1_width + s_cont))
            xc1 = int(xc0 + topvia1_width)
            yc1 = int(yc0 + topvia1_width)
            r = Rect(xc0, yc0, xc1, yc1)
            topvia1 = cv.dbCreateRect(r, layer)
        layer = tech.getLayerNum("TopMetal1", "drawing")
        xm0 = int(mim_en_topvia1 - top_en_via)
        ym0 = int(mim_en_topvia1 + offset - top_en_via)
        xm1 = int(mim_en_topvia1 + topvia1_width + top_en_via)
        ym1 = int(mim_en_topvia1 + topvia1_width + offset + n * (topvia1_width + s_cont) + top_en_via)
        r = Rect(xm0, ym0, xm1, ym1)
        topmetal1 = cv.dbCreateRect(r, layer)
        net = cv.dbCreateNet("PLUS")
        pin = cv.dbCreatePin("PLUS", net, DB_PIN_INOUT)
        cv.dbCreatePort(pin, topmetal1)
    if (contacts == "length") :
        layer = tech.getLayerNum("TopVia1", "drawing")
        n_cont = int((length - 2 * mim_en_topvia1 + topvia1_space) / (topvia1_width + topvia1_space))
        s_cont = 0
        top_en_via = topmetal1_en_topvia1
        if (n_cont > 1) :
            s_cont = topvia1_space
            top_en_via = min_topmetal1_en_topvia1
        offset = abs(int((length - (2 * mim_en_topvia1 + n_cont * (topvia1_width + s_cont) - s_cont)) / 2))
        if offset%xygrid!=0 :
            offset = int(xygrid * int(offset / xygrid))
        for n in range(n_cont) :
            xc0 = int(mim_en_topvia1 + offset + n * (topvia1_width + s_cont))
            yc0 = int(mim_en_topvia1)
            xc1 = int(xc0 + topvia1_width)
            yc1 = int(yc0 + topvia1_width)
            r = Rect(xc0, yc0, xc1, yc1)
            topvia1 = cv.dbCreateRect(r, layer)
        layer = tech.getLayerNum("TopMetal1", "drawing")
        xm0 = int(mim_en_topvia1 + offset - top_en_via)
        ym0 = int(mim_en_topvia1 - top_en_via)
        xm1 = int(mim_en_topvia1 + topvia1_width + offset + n * (topvia1_width + s_cont) + top_en_via)
        ym1 = int(mim_en_topvia1 + topvia1_width + top_en_via)
        r = Rect(xm0, ym0, xm1, ym1)
        topmetal1 = cv.dbCreateRect(r, layer)
        net = cv.dbCreateNet("PLUS")
        pin = cv.dbCreatePin("PLUS", net, DB_PIN_INOUT)
        cv.dbCreatePort(pin, topmetal1)
    if (contacts == "full") :
        layer = tech.getLayerNum("TopVia1", "drawing")
        n_cont = int((width - 2 * mim_en_topvia1 + topvia1_space) / (topvia1_width + topvia1_space))
        m_cont = int((length - 2 * mim_en_topvia1 + topvia1_space) / (topvia1_width + topvia1_space))
        s_cont = 0
        top_en_via = topmetal1_en_topvia1
        if ((n_cont > 1) or (m_cont > 1)) :
            s_cont = topvia1_space
            top_en_via = min_topmetal1_en_topvia1
        w_offset = abs(int((width - (2 * mim_en_topvia1 + n_cont * (topvia1_width + s_cont) - s_cont)) / 2))
        l_offset = abs(int((length - (2 * mim_en_topvia1 + m_cont * (topvia1_width + s_cont) - s_cont)) / 2))
        if w_offset%xygrid!=0 :
            w_offset = int(xygrid * int(w_offset / xygrid))
        if l_offset%xygrid!=0 :
            l_offset = int(xygrid * int(l_offset / xygrid))
        for n in range(n_cont) :
            for m in range(m_cont) :
                xc0 = int(mim_en_topvia1 + l_offset + m * (topvia1_width + s_cont))
                yc0 = int(mim_en_topvia1 + w_offset + n * (topvia1_width + s_cont))
                xc1 = int(xc0 + topvia1_width)
                yc1 = int(yc0 + topvia1_width)
                r = Rect(xc0, yc0, xc1, yc1)
                topvia1 = cv.dbCreateRect(r, layer)
        layer = tech.getLayerNum("TopMetal1", "drawing")
        xm0 = int(mim_en_topvia1 + l_offset - top_en_via)
        ym0 = int(mim_en_topvia1 + w_offset - top_en_via)
        xm1 = int(mim_en_topvia1 + topvia1_width + l_offset + m * (topvia1_width + s_cont) + top_en_via)
        ym1 = int(mim_en_topvia1 + topvia1_width + w_offset + n * (topvia1_width + s_cont) + top_en_via)
        r = Rect(xm0, ym0, xm1, ym1)
        topmetal1 = cv.dbCreateRect(r, layer)
        net = cv.dbCreateNet("PLUS")
        pin = cv.dbCreatePin("PLUS", net, DB_PIN_INOUT)
        cv.dbCreatePort(pin, topmetal1)
    #
    # Save results
    #
    cv.update()