#
# Import the db 
#
from ui import *
import math
#
# The entry point
#
def sbumppad(cv) :
    lib = cv.lib()
    tech = lib.tech()
    dbu = lib.dbuPerUU()
    radius = int(30 * dbu)
    #
    # Layer rules
    #
    xygrid = int(0.005 * dbu)
    topmetal2_en_passiv = int(10 * dbu)
    #
    # Creating the "device"
    #
    # Create active diffusion
    layer = tech.getLayerNum("Passiv", "sbump")
    p = Point(0, 0)
    passiv_sbump = cv.dbCreateCircle(p, radius, layer)
    layer = tech.getLayerNum("dfpad", "drawing")
    p = Point(0, 0)
    dfpad = cv.dbCreateCircle(p, radius, layer)
    layer = tech.getLayerNum("TopMetal2", "drawing")
    c = int((radius + topmetal2_en_passiv) / math.sin(1.178097))
    a = int(c * math.cos(1.178097))
    a = int(xygrid * int(a / xygrid))
    xmpp = intarray(9)
    ympp = intarray(9)
    xmpp[0] = int(-a)
    ympp[0] = int(-(radius + topmetal2_en_passiv))
    xmpp[1] = int(a)
    ympp[1] = ympp[0]
    xmpp[2] = int(radius + topmetal2_en_passiv)
    ympp[2] = int(-a)
    xmpp[3] = xmpp[2]
    ympp[3] = int(+a)
    xmpp[4] = xmpp[1]
    ympp[4] = int(radius + topmetal2_en_passiv)
    xmpp[5] = xmpp[0]
    ympp[5] = ympp[4]
    xmpp[6] = int(-(radius + topmetal2_en_passiv))
    ympp[6] = ympp[3]
    xmpp[7] = xmpp[6]
    ympp[7] = ympp[2]
    xmpp[8] = xmpp[0]
    ympp[8] = ympp[0]
    topmetal2 = cv.dbCreatePolygon(xmpp, ympp, 9, layer)
    #
    # Save results
    #
    cv.update()