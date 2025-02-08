#
# Import the db 
#
from ui import *
#
# The entry point
#
def pad(cv, w=30e-6) :
    lib = cv.lib()
    tech = lib.tech()
    dbu = lib.dbuPerUU()
    width = int(w * 1e9)
    #
    # Layer rules
    #
    xygrid = int(0.005 * dbu)
    topmetal2_en_passiv = int(2.1 * dbu)
    #
    # Device rules
    #
    min_width = int(30 * dbu)
    max_width = int(150 * dbu)
    #
    # Checking parameters
    #
    if width%xygrid!=0 :
        width = int(xygrid * int(width / xygrid))
        cv.dbReplaceProp("w", 1e-6 * (width / dbu))
        cv.update()
    if width < min_width :
        width = min_width
        cv.dbReplaceProp("w", 1e-6 * (width / dbu))
        cv.update()
    if width > max_width :
        width = max_width
        cv.dbReplaceProp("w", 1e-6 * (width / dbu))
        cv.update()
    #
    # Creating the "device"
    #
    # Create active diffusion
    layer = tech.getLayerNum("Passiv", "drawing")
    r = Rect(0, 0, width, width)
    passiv = cv.dbCreateRect(r, layer)
    layer = tech.getLayerNum("Passiv", "sbump")
    r = Rect(0, 0, width, width)
    passiv_sbump = cv.dbCreateRect(r, layer)
    layer = tech.getLayerNum("Passiv", "pillar")
    r = Rect(0, 0, width, width)
    passiv_pillar = cv.dbCreateRect(r, layer)
    layer = tech.getLayerNum("dfpad", "drawing")
    r = Rect(0, 0, width, width)
    dfpad = cv.dbCreateRect(r, layer)
    layer = tech.getLayerNum("TopMetal2", "drawing")
    xp0 = int(-topmetal2_en_passiv)
    yp0 = int(-topmetal2_en_passiv)
    xp1 = int(width + topmetal2_en_passiv)
    yp1 = int(width + topmetal2_en_passiv)
    r = Rect(xp0, yp0, xp1, yp1)
    topmetal2 = cv.dbCreateRect(r, layer)
    #
    # Save results
    #
    cv.update()