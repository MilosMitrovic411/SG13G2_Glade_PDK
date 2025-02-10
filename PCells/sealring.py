from ui import *
#
# The entry point
#
def sealring(cv, w=50e-6, l=50e-6, d=30e-6) :
    lib = cv.lib()
    tech = lib.tech()
    dbu = lib.dbuPerUU()
    width = int(w * 1e6 * dbu)
    length = int(w * 1e6 * dbu)
    distance = int(d * 1e6 * dbu)
    #
    # Layer rules
    #
    xygrid = int(0.005 * dbu)
    cont_width = int(0.16 * dbu)
    cont_space = int(0.18 * dbu)
    via_width = int(0.19 * dbu)
    via_space = int(0.22 * dbu)
    tvia1_width = int(0.42 * dbu)
    tvia1_space = int(0.42 * dbu)
    tvia2_width = int(0.9 * dbu)
    tvia2_space = int(1.06 * dbu)
    t = int(3.5 * dbu)
    pass_offset = int(4.85 * dbu)
    passiv_width = int(4.2 * dbu)
    #
    # Device rules
    #
    min_width = int(50 * dbu)
    min_length = int(50 * dbu)
    min_distance = int(7 * dbu)
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
    if distance%xygrid!=0 :
        distance = int(xygrid * int(distance / xygrid))
        cv.dbReplaceProp("d", 1e-6 * (distance / dbu))
        cv.update()
    if width < min_width :
        width = min_width
        cv.dbReplaceProp("w", 1e-6 * (width / dbu))
        cv.update()
    if length < min_length :
        length = min_length
        cv.dbReplaceProp("l", 1e-6 * (length / dbu))
        cv.update()
    if distance < min_distance :
        distance = min_distance
        cv.dbReplaceProp("d", 1e-6 * (distance / dbu))
        cv.update()
    #
    # Creating the "device"
    #
    xmpp0 = int(4 * t + t / 2)
    ympp0 = int(t / 2)
    xmpp1 = int(length - 2 * t - t / 2)
    ympp1 = ympp0
    xmpp2 = xmpp1
    ympp2 = int(ympp0 + t)
    xmpp3 = int(xmpp2 + t)
    ympp3 = ympp2
    xmpp4 = xmpp3
    ympp4 = int(ympp3 + t)
    xmpp5 = int(xmpp4 + t)
    ympp5 = ympp4
    xmpp6 = xmpp5
    ympp6 = int(ympp5 + t)
    xmpp7 = int(xmpp6 + t)
    ympp7 = ympp6
    xmpp8 = xmpp7
    ympp8 = int(ympp7 + t)
    xmpp9 = int(xmpp8 + t)
    ympp9 = ympp8
    xmpp10 = xmpp9
    ympp10 = int(width - 2 * t - t / 2)
    xmpp11 = int(xmpp10 - t)
    ympp11 = ympp10
    xmpp12 = xmpp11
    ympp12 = int(ympp11 + t)
    xmpp13 = int(xmpp12 - t)
    ympp13 = ympp12
    xmpp14 = xmpp13
    ympp14 = int(ympp13 + t)
    xmpp15 = int(xmpp14 - t)
    ympp15 = ympp14
    xmpp16 = xmpp15
    ympp16 = int(ympp15 + t)
    xmpp17 = int(xmpp16 - t)
    ympp17 = ympp16
    xmpp18 = xmpp17
    ympp18 = int(ympp17 + t)
    xmpp19 = int(4 * t + t / 2)
    ympp19 = ympp18
    xmpp20 = xmpp19
    ympp20 = int(ympp19 - t)
    xmpp21 = int(xmpp20 - t)
    ympp21 = ympp20
    xmpp22 = xmpp21
    ympp22 = int(ympp21 - t)
    xmpp23 = int(xmpp22 - t)
    ympp23 = ympp22
    xmpp24 = xmpp23
    ympp24 = int(ympp23 - t)
    xmpp25 = int(xmpp24 - t)
    ympp25 = ympp24
    xmpp26 = xmpp25
    ympp26 = int(ympp25 - t)
    xmpp27 = int(xmpp26 -t)
    ympp27 = ympp26
    xmpp28 = xmpp27
    ympp28 = int(4 * t + t / 2)
    xmpp29 = int(xmpp28 + t)
    ympp29 = ympp28
    xmpp30 = xmpp29
    ympp30 = int(ympp29 - t)
    xmpp31 = int(xmpp30 + t)
    ympp31 = ympp30
    xmpp32 = xmpp31
    ympp32 = int(ympp31 - t)
    xmpp33 = int(xmpp32 + t)
    ympp33 = ympp32
    xmpp34 = xmpp33
    ympp34 = int(ympp33 - t)
    xmpp35 = int(xmpp34 + t)
    ympp35 = ympp34
    xmpp36 = xmpp35
    ympp36 = int(ympp35 - t)
    ring = lib.getMPPRule("nguard")
    nring = cv.dbCreateMPP(ring, [[xmpp0,ympp0],[xmpp1,ympp1],[xmpp2,ympp2],[xmpp3,ympp3],[xmpp4,ympp4],[xmpp5,ympp5],[xmpp6,ympp6],[xmpp7,ympp7],[xmpp8,ympp8],[xmpp9,ympp9],[xmpp10,ympp10],[xmpp11,ympp11],[xmpp12,ympp12],[xmpp13,ympp13],[xmpp14,ympp14],[xmpp15,ympp15],[xmpp16,ympp16],[xmpp17,ympp17],[xmpp18,ympp18],[xmpp19,ympp19],[xmpp20,ympp20],[xmpp21,ympp21],[xmpp22,ympp22],[xmpp23,ympp23],[xmpp24,ympp24],[xmpp25,ympp25],[xmpp26,ympp26],[xmpp27,ympp27],[xmpp28,ympp28],[xmpp29,ympp29],[xmpp30,ympp30],[xmpp31,ympp31],[xmpp32,ympp32],[xmpp33,ympp33],[xmpp34,ympp34],[xmpp35,ympp35],[xmpp36,ympp36]], 37)
    ring = lib.getMPPRule("m1m2")
    m1m2ring = cv.dbCreateMPP(ring, [[xmpp0,ympp0],[xmpp1,ympp1],[xmpp2,ympp2],[xmpp3,ympp3],[xmpp4,ympp4],[xmpp5,ympp5],[xmpp6,ympp6],[xmpp7,ympp7],[xmpp8,ympp8],[xmpp9,ympp9],[xmpp10,ympp10],[xmpp11,ympp11],[xmpp12,ympp12],[xmpp13,ympp13],[xmpp14,ympp14],[xmpp15,ympp15],[xmpp16,ympp16],[xmpp17,ympp17],[xmpp18,ympp18],[xmpp19,ympp19],[xmpp20,ympp20],[xmpp21,ympp21],[xmpp22,ympp22],[xmpp23,ympp23],[xmpp24,ympp24],[xmpp25,ympp25],[xmpp26,ympp26],[xmpp27,ympp27],[xmpp28,ympp28],[xmpp29,ympp29],[xmpp30,ympp30],[xmpp31,ympp31],[xmpp32,ympp32],[xmpp33,ympp33],[xmpp34,ympp34],[xmpp35,ympp35],[xmpp36,ympp36]], 37)
    ring = lib.getMPPRule("m2m3")
    m2m3ring = cv.dbCreateMPP(ring, [[xmpp0,ympp0],[xmpp1,ympp1],[xmpp2,ympp2],[xmpp3,ympp3],[xmpp4,ympp4],[xmpp5,ympp5],[xmpp6,ympp6],[xmpp7,ympp7],[xmpp8,ympp8],[xmpp9,ympp9],[xmpp10,ympp10],[xmpp11,ympp11],[xmpp12,ympp12],[xmpp13,ympp13],[xmpp14,ympp14],[xmpp15,ympp15],[xmpp16,ympp16],[xmpp17,ympp17],[xmpp18,ympp18],[xmpp19,ympp19],[xmpp20,ympp20],[xmpp21,ympp21],[xmpp22,ympp22],[xmpp23,ympp23],[xmpp24,ympp24],[xmpp25,ympp25],[xmpp26,ympp26],[xmpp27,ympp27],[xmpp28,ympp28],[xmpp29,ympp29],[xmpp30,ympp30],[xmpp31,ympp31],[xmpp32,ympp32],[xmpp33,ympp33],[xmpp34,ympp34],[xmpp35,ympp35],[xmpp36,ympp36]], 37)
    ring = lib.getMPPRule("m3m4")
    m3m4ring = cv.dbCreateMPP(ring, [[xmpp0,ympp0],[xmpp1,ympp1],[xmpp2,ympp2],[xmpp3,ympp3],[xmpp4,ympp4],[xmpp5,ympp5],[xmpp6,ympp6],[xmpp7,ympp7],[xmpp8,ympp8],[xmpp9,ympp9],[xmpp10,ympp10],[xmpp11,ympp11],[xmpp12,ympp12],[xmpp13,ympp13],[xmpp14,ympp14],[xmpp15,ympp15],[xmpp16,ympp16],[xmpp17,ympp17],[xmpp18,ympp18],[xmpp19,ympp19],[xmpp20,ympp20],[xmpp21,ympp21],[xmpp22,ympp22],[xmpp23,ympp23],[xmpp24,ympp24],[xmpp25,ympp25],[xmpp26,ympp26],[xmpp27,ympp27],[xmpp28,ympp28],[xmpp29,ympp29],[xmpp30,ympp30],[xmpp31,ympp31],[xmpp32,ympp32],[xmpp33,ympp33],[xmpp34,ympp34],[xmpp35,ympp35],[xmpp36,ympp36]], 37)
    ring = lib.getMPPRule("m4m5")
    m4m5ring = cv.dbCreateMPP(ring, [[xmpp0,ympp0],[xmpp1,ympp1],[xmpp2,ympp2],[xmpp3,ympp3],[xmpp4,ympp4],[xmpp5,ympp5],[xmpp6,ympp6],[xmpp7,ympp7],[xmpp8,ympp8],[xmpp9,ympp9],[xmpp10,ympp10],[xmpp11,ympp11],[xmpp12,ympp12],[xmpp13,ympp13],[xmpp14,ympp14],[xmpp15,ympp15],[xmpp16,ympp16],[xmpp17,ympp17],[xmpp18,ympp18],[xmpp19,ympp19],[xmpp20,ympp20],[xmpp21,ympp21],[xmpp22,ympp22],[xmpp23,ympp23],[xmpp24,ympp24],[xmpp25,ympp25],[xmpp26,ympp26],[xmpp27,ympp27],[xmpp28,ympp28],[xmpp29,ympp29],[xmpp30,ympp30],[xmpp31,ympp31],[xmpp32,ympp32],[xmpp33,ympp33],[xmpp34,ympp34],[xmpp35,ympp35],[xmpp36,ympp36]], 37)
    ring = lib.getMPPRule("m5tm1")
    m5tm1ring = cv.dbCreateMPP(ring, [[xmpp0,ympp0],[xmpp1,ympp1],[xmpp2,ympp2],[xmpp3,ympp3],[xmpp4,ympp4],[xmpp5,ympp5],[xmpp6,ympp6],[xmpp7,ympp7],[xmpp8,ympp8],[xmpp9,ympp9],[xmpp10,ympp10],[xmpp11,ympp11],[xmpp12,ympp12],[xmpp13,ympp13],[xmpp14,ympp14],[xmpp15,ympp15],[xmpp16,ympp16],[xmpp17,ympp17],[xmpp18,ympp18],[xmpp19,ympp19],[xmpp20,ympp20],[xmpp21,ympp21],[xmpp22,ympp22],[xmpp23,ympp23],[xmpp24,ympp24],[xmpp25,ympp25],[xmpp26,ympp26],[xmpp27,ympp27],[xmpp28,ympp28],[xmpp29,ympp29],[xmpp30,ympp30],[xmpp31,ympp31],[xmpp32,ympp32],[xmpp33,ympp33],[xmpp34,ympp34],[xmpp35,ympp35],[xmpp36,ympp36]], 37)
    ring = lib.getMPPRule("tm1tm2")
    tm1tm2ring = cv.dbCreateMPP(ring, [[xmpp0,ympp0],[xmpp1,ympp1],[xmpp2,ympp2],[xmpp3,ympp3],[xmpp4,ympp4],[xmpp5,ympp5],[xmpp6,ympp6],[xmpp7,ympp7],[xmpp8,ympp8],[xmpp9,ympp9],[xmpp10,ympp10],[xmpp11,ympp11],[xmpp12,ympp12],[xmpp13,ympp13],[xmpp14,ympp14],[xmpp15,ympp15],[xmpp16,ympp16],[xmpp17,ympp17],[xmpp18,ympp18],[xmpp19,ympp19],[xmpp20,ympp20],[xmpp21,ympp21],[xmpp22,ympp22],[xmpp23,ympp23],[xmpp24,ympp24],[xmpp25,ympp25],[xmpp26,ympp26],[xmpp27,ympp27],[xmpp28,ympp28],[xmpp29,ympp29],[xmpp30,ympp30],[xmpp31,ympp31],[xmpp32,ympp32],[xmpp33,ympp33],[xmpp34,ympp34],[xmpp35,ympp35],[xmpp36,ympp36]], 37)
    layer = tech.getLayerNum("Activ", "drawing")
    apath = cv.dbCreatePath([[xmpp0,ympp0],[xmpp1,ympp1],[xmpp2,ympp2],[xmpp3,ympp3],[xmpp4,ympp4],[xmpp5,ympp5],[xmpp6,ympp6],[xmpp7,ympp7],[xmpp8,ympp8],[xmpp9,ympp9],[xmpp10,ympp10],[xmpp11,ympp11],[xmpp12,ympp12],[xmpp13,ympp13],[xmpp14,ympp14],[xmpp15,ympp15],[xmpp16,ympp16],[xmpp17,ympp17],[xmpp18,ympp18],[xmpp19,ympp19],[xmpp20,ympp20],[xmpp21,ympp21],[xmpp22,ympp22],[xmpp23,ympp23],[xmpp24,ympp24],[xmpp25,ympp25],[xmpp26,ympp26],[xmpp27,ympp27],[xmpp28,ympp28],[xmpp29,ympp29],[xmpp30,ympp30],[xmpp31,ympp31],[xmpp32,ympp32],[xmpp33,ympp33],[xmpp34,ympp34],[xmpp35,ympp35],[xmpp36,ympp36]], 37, layer, t, 2, int(t / 2), int(t / 2))
    layer = tech.getLayerNum("pSD", "drawing")
    ppath = cv.dbCreatePath([[xmpp0,ympp0],[xmpp1,ympp1],[xmpp2,ympp2],[xmpp3,ympp3],[xmpp4,ympp4],[xmpp5,ympp5],[xmpp6,ympp6],[xmpp7,ympp7],[xmpp8,ympp8],[xmpp9,ympp9],[xmpp10,ympp10],[xmpp11,ympp11],[xmpp12,ympp12],[xmpp13,ympp13],[xmpp14,ympp14],[xmpp15,ympp15],[xmpp16,ympp16],[xmpp17,ympp17],[xmpp18,ympp18],[xmpp19,ympp19],[xmpp20,ympp20],[xmpp21,ympp21],[xmpp22,ympp22],[xmpp23,ympp23],[xmpp24,ympp24],[xmpp25,ympp25],[xmpp26,ympp26],[xmpp27,ympp27],[xmpp28,ympp28],[xmpp29,ympp29],[xmpp30,ympp30],[xmpp31,ympp31],[xmpp32,ympp32],[xmpp33,ympp33],[xmpp34,ympp34],[xmpp35,ympp35],[xmpp36,ympp36]], 37, layer, t, 2, int(t / 2), int(t / 2))
    layer = tech.getLayerNum("Metal1", "drawing")
    m1path = cv.dbCreatePath([[xmpp0,ympp0],[xmpp1,ympp1],[xmpp2,ympp2],[xmpp3,ympp3],[xmpp4,ympp4],[xmpp5,ympp5],[xmpp6,ympp6],[xmpp7,ympp7],[xmpp8,ympp8],[xmpp9,ympp9],[xmpp10,ympp10],[xmpp11,ympp11],[xmpp12,ympp12],[xmpp13,ympp13],[xmpp14,ympp14],[xmpp15,ympp15],[xmpp16,ympp16],[xmpp17,ympp17],[xmpp18,ympp18],[xmpp19,ympp19],[xmpp20,ympp20],[xmpp21,ympp21],[xmpp22,ympp22],[xmpp23,ympp23],[xmpp24,ympp24],[xmpp25,ympp25],[xmpp26,ympp26],[xmpp27,ympp27],[xmpp28,ympp28],[xmpp29,ympp29],[xmpp30,ympp30],[xmpp31,ympp31],[xmpp32,ympp32],[xmpp33,ympp33],[xmpp34,ympp34],[xmpp35,ympp35],[xmpp36,ympp36]], 37, layer, t, 2, int(t / 2), int(t / 2))
    layer = tech.getLayerNum("Metal2", "drawing")
    m2path = cv.dbCreatePath([[xmpp0,ympp0],[xmpp1,ympp1],[xmpp2,ympp2],[xmpp3,ympp3],[xmpp4,ympp4],[xmpp5,ympp5],[xmpp6,ympp6],[xmpp7,ympp7],[xmpp8,ympp8],[xmpp9,ympp9],[xmpp10,ympp10],[xmpp11,ympp11],[xmpp12,ympp12],[xmpp13,ympp13],[xmpp14,ympp14],[xmpp15,ympp15],[xmpp16,ympp16],[xmpp17,ympp17],[xmpp18,ympp18],[xmpp19,ympp19],[xmpp20,ympp20],[xmpp21,ympp21],[xmpp22,ympp22],[xmpp23,ympp23],[xmpp24,ympp24],[xmpp25,ympp25],[xmpp26,ympp26],[xmpp27,ympp27],[xmpp28,ympp28],[xmpp29,ympp29],[xmpp30,ympp30],[xmpp31,ympp31],[xmpp32,ympp32],[xmpp33,ympp33],[xmpp34,ympp34],[xmpp35,ympp35],[xmpp36,ympp36]], 37, layer, t, 2, int(t / 2), int(t / 2))
    layer = tech.getLayerNum("Metal3", "drawing")
    m3path = cv.dbCreatePath([[xmpp0,ympp0],[xmpp1,ympp1],[xmpp2,ympp2],[xmpp3,ympp3],[xmpp4,ympp4],[xmpp5,ympp5],[xmpp6,ympp6],[xmpp7,ympp7],[xmpp8,ympp8],[xmpp9,ympp9],[xmpp10,ympp10],[xmpp11,ympp11],[xmpp12,ympp12],[xmpp13,ympp13],[xmpp14,ympp14],[xmpp15,ympp15],[xmpp16,ympp16],[xmpp17,ympp17],[xmpp18,ympp18],[xmpp19,ympp19],[xmpp20,ympp20],[xmpp21,ympp21],[xmpp22,ympp22],[xmpp23,ympp23],[xmpp24,ympp24],[xmpp25,ympp25],[xmpp26,ympp26],[xmpp27,ympp27],[xmpp28,ympp28],[xmpp29,ympp29],[xmpp30,ympp30],[xmpp31,ympp31],[xmpp32,ympp32],[xmpp33,ympp33],[xmpp34,ympp34],[xmpp35,ympp35],[xmpp36,ympp36]], 37, layer, t, 2, int(t / 2), int(t / 2))
    layer = tech.getLayerNum("Metal4", "drawing")
    m4path = cv.dbCreatePath([[xmpp0,ympp0],[xmpp1,ympp1],[xmpp2,ympp2],[xmpp3,ympp3],[xmpp4,ympp4],[xmpp5,ympp5],[xmpp6,ympp6],[xmpp7,ympp7],[xmpp8,ympp8],[xmpp9,ympp9],[xmpp10,ympp10],[xmpp11,ympp11],[xmpp12,ympp12],[xmpp13,ympp13],[xmpp14,ympp14],[xmpp15,ympp15],[xmpp16,ympp16],[xmpp17,ympp17],[xmpp18,ympp18],[xmpp19,ympp19],[xmpp20,ympp20],[xmpp21,ympp21],[xmpp22,ympp22],[xmpp23,ympp23],[xmpp24,ympp24],[xmpp25,ympp25],[xmpp26,ympp26],[xmpp27,ympp27],[xmpp28,ympp28],[xmpp29,ympp29],[xmpp30,ympp30],[xmpp31,ympp31],[xmpp32,ympp32],[xmpp33,ympp33],[xmpp34,ympp34],[xmpp35,ympp35],[xmpp36,ympp36]], 37, layer, t, 2, int(t / 2), int(t / 2))
    layer = tech.getLayerNum("Metal5", "drawing")
    m5path = cv.dbCreatePath([[xmpp0,ympp0],[xmpp1,ympp1],[xmpp2,ympp2],[xmpp3,ympp3],[xmpp4,ympp4],[xmpp5,ympp5],[xmpp6,ympp6],[xmpp7,ympp7],[xmpp8,ympp8],[xmpp9,ympp9],[xmpp10,ympp10],[xmpp11,ympp11],[xmpp12,ympp12],[xmpp13,ympp13],[xmpp14,ympp14],[xmpp15,ympp15],[xmpp16,ympp16],[xmpp17,ympp17],[xmpp18,ympp18],[xmpp19,ympp19],[xmpp20,ympp20],[xmpp21,ympp21],[xmpp22,ympp22],[xmpp23,ympp23],[xmpp24,ympp24],[xmpp25,ympp25],[xmpp26,ympp26],[xmpp27,ympp27],[xmpp28,ympp28],[xmpp29,ympp29],[xmpp30,ympp30],[xmpp31,ympp31],[xmpp32,ympp32],[xmpp33,ympp33],[xmpp34,ympp34],[xmpp35,ympp35],[xmpp36,ympp36]], 37, layer, t, 2, int(t / 2), int(t / 2))
    layer = tech.getLayerNum("TopMetal1", "drawing")
    tm1path = cv.dbCreatePath([[xmpp0,ympp0],[xmpp1,ympp1],[xmpp2,ympp2],[xmpp3,ympp3],[xmpp4,ympp4],[xmpp5,ympp5],[xmpp6,ympp6],[xmpp7,ympp7],[xmpp8,ympp8],[xmpp9,ympp9],[xmpp10,ympp10],[xmpp11,ympp11],[xmpp12,ympp12],[xmpp13,ympp13],[xmpp14,ympp14],[xmpp15,ympp15],[xmpp16,ympp16],[xmpp17,ympp17],[xmpp18,ympp18],[xmpp19,ympp19],[xmpp20,ympp20],[xmpp21,ympp21],[xmpp22,ympp22],[xmpp23,ympp23],[xmpp24,ympp24],[xmpp25,ympp25],[xmpp26,ympp26],[xmpp27,ympp27],[xmpp28,ympp28],[xmpp29,ympp29],[xmpp30,ympp30],[xmpp31,ympp31],[xmpp32,ympp32],[xmpp33,ympp33],[xmpp34,ympp34],[xmpp35,ympp35],[xmpp36,ympp36]], 37, layer, t, 2, int(t / 2), int(t / 2))
    layer = tech.getLayerNum("TopMetal2", "drawing")
    tm2path = cv.dbCreatePath([[xmpp0,ympp0],[xmpp1,ympp1],[xmpp2,ympp2],[xmpp3,ympp3],[xmpp4,ympp4],[xmpp5,ympp5],[xmpp6,ympp6],[xmpp7,ympp7],[xmpp8,ympp8],[xmpp9,ympp9],[xmpp10,ympp10],[xmpp11,ympp11],[xmpp12,ympp12],[xmpp13,ympp13],[xmpp14,ympp14],[xmpp15,ympp15],[xmpp16,ympp16],[xmpp17,ympp17],[xmpp18,ympp18],[xmpp19,ympp19],[xmpp20,ympp20],[xmpp21,ympp21],[xmpp22,ympp22],[xmpp23,ympp23],[xmpp24,ympp24],[xmpp25,ympp25],[xmpp26,ympp26],[xmpp27,ympp27],[xmpp28,ympp28],[xmpp29,ympp29],[xmpp30,ympp30],[xmpp31,ympp31],[xmpp32,ympp32],[xmpp33,ympp33],[xmpp34,ympp34],[xmpp35,ympp35],[xmpp36,ympp36]], 37, layer, t, 2, int(t / 2), int(t / 2))
    layer = tech.getLayerNum("EdgeSeal", "drawing")
    spath = cv.dbCreatePath([[xmpp0,ympp0],[xmpp1,ympp1],[xmpp2,ympp2],[xmpp3,ympp3],[xmpp4,ympp4],[xmpp5,ympp5],[xmpp6,ympp6],[xmpp7,ympp7],[xmpp8,ympp8],[xmpp9,ympp9],[xmpp10,ympp10],[xmpp11,ympp11],[xmpp12,ympp12],[xmpp13,ympp13],[xmpp14,ympp14],[xmpp15,ympp15],[xmpp16,ympp16],[xmpp17,ympp17],[xmpp18,ympp18],[xmpp19,ympp19],[xmpp20,ympp20],[xmpp21,ympp21],[xmpp22,ympp22],[xmpp23,ympp23],[xmpp24,ympp24],[xmpp25,ympp25],[xmpp26,ympp26],[xmpp27,ympp27],[xmpp28,ympp28],[xmpp29,ympp29],[xmpp30,ympp30],[xmpp31,ympp31],[xmpp32,ympp32],[xmpp33,ympp33],[xmpp34,ympp34],[xmpp35,ympp35],[xmpp36,ympp36]], 37, layer, t, 2, int(t / 2), int(t / 2))
    xmpp0 = int(4 * t + t / 2 - pass_offset)
    ympp0 = int(t / 2 - pass_offset)
    xmpp1 = int(length - 2 * t - t / 2 + pass_offset)
    ympp1 = ympp0
    xmpp2 = xmpp1
    ympp2 = int(ympp0 + t)
    xmpp3 = int(xmpp2 + t)
    ympp3 = ympp2
    xmpp4 = xmpp3
    ympp4 = int(ympp3 + t)
    xmpp5 = int(xmpp4 + t)
    ympp5 = ympp4
    xmpp6 = xmpp5
    ympp6 = int(ympp5 + t)
    xmpp7 = int(xmpp6 + t)
    ympp7 = ympp6
    xmpp8 = xmpp7
    ympp8 = int(ympp7 + t)
    xmpp9 = int(xmpp8 + t)
    ympp9 = ympp8
    xmpp10 = xmpp9
    ympp10 = int(width - 2 * t - t / 2 + pass_offset)
    xmpp11 = int(xmpp10 - t)
    ympp11 = ympp10
    xmpp12 = xmpp11
    ympp12 = int(ympp11 + t)
    xmpp13 = int(xmpp12 - t)
    ympp13 = ympp12
    xmpp14 = xmpp13
    ympp14 = int(ympp13 + t)
    xmpp15 = int(xmpp14 - t)
    ympp15 = ympp14
    xmpp16 = xmpp15
    ympp16 = int(ympp15 + t)
    xmpp17 = int(xmpp16 - t)
    ympp17 = ympp16
    xmpp18 = xmpp17
    ympp18 = int(ympp17 + t)
    xmpp19 = int(4 * t + t / 2 - pass_offset)
    ympp19 = ympp18
    xmpp20 = xmpp19
    ympp20 = int(ympp19 - t)
    xmpp21 = int(xmpp20 - t)
    ympp21 = ympp20
    xmpp22 = xmpp21
    ympp22 = int(ympp21 - t)
    xmpp23 = int(xmpp22 - t)
    ympp23 = ympp22
    xmpp24 = xmpp23
    ympp24 = int(ympp23 - t)
    xmpp25 = int(xmpp24 - t)
    ympp25 = ympp24
    xmpp26 = xmpp25
    ympp26 = int(ympp25 - t)
    xmpp27 = int(xmpp26 -t)
    ympp27 = ympp26
    xmpp28 = xmpp27
    ympp28 = int(4 * t + t / 2 - pass_offset)
    xmpp29 = int(xmpp28 + t)
    ympp29 = ympp28
    xmpp30 = xmpp29
    ympp30 = int(ympp29 - t)
    xmpp31 = int(xmpp30 + t)
    ympp31 = ympp30
    xmpp32 = xmpp31
    ympp32 = int(ympp31 - t)
    xmpp33 = int(xmpp32 + t)
    ympp33 = ympp32
    xmpp34 = xmpp33
    ympp34 = int(ympp33 - t)
    xmpp35 = int(xmpp34 + t)
    ympp35 = ympp34
    xmpp36 = xmpp35
    ympp36 = int(ympp35 - t)
    layer = tech.getLayerNum("Passiv", "drawing")
    paspath = cv.dbCreatePath([[xmpp0,ympp0],[xmpp1,ympp1],[xmpp2,ympp2],[xmpp3,ympp3],[xmpp4,ympp4],[xmpp5,ympp5],[xmpp6,ympp6],[xmpp7,ympp7],[xmpp8,ympp8],[xmpp9,ympp9],[xmpp10,ympp10],[xmpp11,ympp11],[xmpp12,ympp12],[xmpp13,ympp13],[xmpp14,ympp14],[xmpp15,ympp15],[xmpp16,ympp16],[xmpp17,ympp17],[xmpp18,ympp18],[xmpp19,ympp19],[xmpp20,ympp20],[xmpp21,ympp21],[xmpp22,ympp22],[xmpp23,ympp23],[xmpp24,ympp24],[xmpp25,ympp25],[xmpp26,ympp26],[xmpp27,ympp27],[xmpp28,ympp28],[xmpp29,ympp29],[xmpp30,ympp30],[xmpp31,ympp31],[xmpp32,ympp32],[xmpp33,ympp33],[xmpp34,ympp34],[xmpp35,ympp35],[xmpp36,ympp36]], 37, layer, passiv_width, 2, int(passiv_width / 2), int(passiv_width / 2))
    layer = tech.getLayerNum("EdgeSeal", "boundary")
    x0 = -distance
    y0 = -distance
    x1 = int(length + 2 * t + distance)
    y1 = int(length + 2 * t + distance)
    r = Rect(x0, y0, x1, y1)
    seal = cv.dbCreateRect(r, layer)
    #
    # Save results
    #
    cv.update()