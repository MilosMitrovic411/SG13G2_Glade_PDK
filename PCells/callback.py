def callback(pyDBObject) :
    lib = pyDBObject.lib()
    tech = lib.tech()
    dbu = lib.dbuPerUU()
    xygrid = int(0.005 * dbu)
    inst = pyDBObject.toInst()
    cell_name = pyDBObject.cellName()
    if (cell_name.find("cmim") >= 0) :
        name = "cmim"
    if (cell_name.find("rsil") >= 0) :
        name = "rsil"
    if (cell_name.find("rppd") >= 0) :
        name = "rppd"
    if (cell_name.find("rhigh") >= 0) :
        name = "rhigh"
    if (cell_name.find("via") >= 0) :
        name = "via"
    if (cell_name.find("mos") >= 0) :
        name = "mos"
    if (cell_name.find("isolbox") >= 0) :
        name = "isolbox"
    if (cell_name.find("pad") >= 0) :
        name = "pad"
    if (cell_name.find("seal") >= 0) :
        name = "sealring"
    if (cell_name.find("npn13G2") >= 0) :
        name = "npn13G2"
    if (cell_name.find("SVaricap") >= 0) :
        name = "SVaricap"
    if (cell_name.find("nmoscl_2") >= 0) :
        name = "nmoscl_2"
    if (cell_name.find("nmoscl_4") >= 0) :
        name = "nmoscl_4"
    if (cell_name.find("dantenna") >= 0) :
        name = "dantenna"
    if (cell_name.find("dpantenna") >= 0) :
        name = "dpantenna"
    print()
    print("Selected device is: ", end="")
    print(name)
    #
    if (name == "cmim") :
        model = inst.dbGetStringProp("model", True)
        if(not model) :
            inst.dbAddProp("model", "cap_cmim")
        type = inst.dbGetStringProp("type", True)
        if(not type) :
            inst.dbAddProp("type", "cap")
        select = inst.dbGetListProp("calculate", True)
        if (not select) :
            inst.dbAddProp("calculate", "L", "[L, C]")
            select = inst.dbGetListProp("calculate", True)  
        print("Calculation mode: ", end="")
        print(select)
        w = max(int(inst.dbGetFloatProp("w", True) * 1e6 * dbu), int(inst.dbGetFloatProp("w", True) * 1e9))
        if (w < int(1.14 * dbu)) :
            w = int(1.14 * dbu)
            print("The width value is smaller then minimal, adjusting. The new width value is: w=", end="")
            print(1e-6 * w / dbu)
        if w%xygrid!=0 :
            w = int(xygrid * int(w / xygrid))
            print("The width value is of grid, adjusting. The new width value is: w=", end="")
            print(1e-6 * w / dbu)
        inst.dbReplaceProp("w", 1e-6 * w / dbu)
        if (select == "L") :
            c = max(int(inst.dbGetFloatProp("c", True) * 1e15 * dbu), int(inst.dbGetFloatProp("c", True) * 1e18))
            if (c < int(1.95 * dbu)) :
                c = int(1.95 * dbu)
                print("The capacitance is smaller than minimal, adjusting capacitance. The new capactiance value is: c=", end="")
                print(1e-15 * c / dbu)
            if (c > int(8437.5 * dbu)) :
                c = int(8437.5 * dbu)
                print("The capacitance is larger than maximal, adjusting capacitance. The new capactiance value is: c=", end="")
                print(1e-15 * c / dbu)
            inst.dbReplaceProp("c", 1e-15 * c / dbu)
            l = int(c / (w * 1.5 / dbu))
            if (l < int(1.14 * dbu)) :
                l = int(1.14 * dbu)
                c = float(w * l * 1.5 / (dbu * dbu))
                inst.dbReplaceProp("c", 1e-15 * c)
                print("The length value is smaller then minimal, adjusting. The new capactiance value is: c=", end="")
                print(1e-15 * c)
            if (w * l > int(5625 * dbu * dbu)) :
                l = int(int(5625 * dbu * dbu) / w)
                c = float(w * l * 1.5 / (dbu * dbu))
                inst.dbReplaceProp("c", 1e-15 * c)
                print("The area is larger than maximal, adjusting length. The new capactiance value is: c=", end="")
                print(1e-15 * c)
            if l%xygrid!=0 :
                l = int(xygrid * int(l / xygrid))
                c = float(w * l * 1.5 / (dbu * dbu))
                inst.dbReplaceProp("c", 1e-15 * c)
                print("The derived value is of grid, adjusting values. The new capactiance value is: c=", end="")
                print(1e-15 * c)
            inst.dbReplaceProp("l", 1e-6 * l / dbu)
            print("The derived length value is: l=", end="")
            print(1e-6 * l / dbu)
            print()
        if (select == "C") :
            l = max(int(inst.dbGetFloatProp("l", True) * 1e6 * dbu), int(inst.dbGetFloatProp("l", True) * 1e9))
            if (l < int(1.14 * dbu)) :
                l = int(1.14 * dbu)
                print("The length value is smaller then minimal, adjusting. The new length value is: l=", end="")
                print(1e-6 * w / dbu)
            if (w * l > int(5625 * dbu * dbu)) :
                l = int(int(5625 * dbu * dbu) / w)
                print("The area is larger than maximal, adjusting. The new length value is: l=", end="")
                print(1e-6 * l / dbu)
            if l%xygrid!=0 :
                l = int(xygrid * int(l / xygrid))
                print("The length value is of grid, adjusting. The new length value is: l=", end="")
                print(1e-6 * l / dbu)
            inst.dbReplaceProp("l", 1e-6 * l / dbu)
            c = float(w * l * 1.5 / (dbu * dbu))
            inst.dbReplaceProp("c", 1e-15 * c)
            print("The derived capacitance value is: c=", end="")
            print(1e-15 * c)
            print()
    #
    if (name == "rsil") :
        select = inst.dbGetListProp("calculate", True)
        if (not select) :
            inst.dbAddProp("calculate", "L", "[L, R]")
            select = inst.dbGetListProp("calculate", True)
        print("Calculation mode: ", end="")
        print(select)
        w = max(int(inst.dbGetFloatProp("w", True) * 1e6 * dbu), int(inst.dbGetFloatProp("w", True) * 1e9))
        if (w < int(0.5 * dbu)) :
            w = int(0.5 * dbu)
            print("The width value is smaller then minimal, adjusting. The new width value is: w=", end="")
            print(1e-6 * w / dbu)
        if w%xygrid!=0 :
            w = int(xygrid * int(w / xygrid))
            print("The width value is of grid, adjusting. The new width value is: w=", end="")
            print(1e-6 * w / dbu)
        inst.dbReplaceProp("w", 1e-6 * w / dbu)
        if (select == "L") :
            r = int(inst.dbGetFloatProp("r", True) * dbu)
            l = int(r * w / (7 * dbu))
            if (l < int(0.5 * dbu)) :
                l = int(0.5 * dbu)
                r = float(7 * l / w )
                inst.dbReplaceProp("r", r)
                print("The length value is smaller then minimal, adjusting. The new resistance value is: r=", end="")
                print(r)
            if l%xygrid!=0 :
                l = int(xygrid * int(l / xygrid))
                r = float(7 * l / w )
                print("The derived value is of grid, adjusting values. The new resistance value is: r=", end="")
                print(r)
            inst.dbReplaceProp("l", 1e-6 * l / dbu)
            print("The derived length value is: l=", end="")
            print(1e-6 * l / dbu)
            print()
        if (select == "R") :
            l = max(int(inst.dbGetFloatProp("l", True) * 1e6 * dbu), int(inst.dbGetFloatProp("l", True) * 1e9))
            if (l < int(0.5 * dbu)) :
                l = int(0.5 * dbu)
                print("The length value is smaller then minimal, adjusting. The new length value is: l=", end="")
                print(1e-6 * w / dbu)
            if l%xygrid!=0 :
                l = int(xygrid * int(l / xygrid))
                print("The length value is of grid, adjusting. The new length value is: l=", end="")
                print(1e-6 * l / dbu)
            inst.dbReplaceProp("l", 1e-6 * l / dbu)
            r = float(7 * l / w )
            inst.dbReplaceProp("r", r)
            print("The derived resistance value is: r=", end="")
            print(r)
            print()
    #
    if (name == "rppd") :
        select = inst.dbGetListProp("calculate", True)
        if (not select) :
            inst.dbAddProp("calculate", "L", "[L, R]")
            select = inst.dbGetListProp("calculate", True)
        print("Calculation mode: ", end="")
        print(select)
        w = max(int(inst.dbGetFloatProp("w", True) * 1e6 * dbu), int(inst.dbGetFloatProp("w", True) * 1e9))
        if (w < int(0.5 * dbu)) :
            w = int(0.5 * dbu)
            print("The width value is smaller then minimal, adjusting. The new width value is: w=", end="")
            print(1e-6 * w / dbu)
        if w%xygrid!=0 :
            w = int(xygrid * int(w / xygrid))
            print("The width value is of grid, adjusting. The new width value is: w=", end="")
            print(1e-6 * w / dbu)
        inst.dbReplaceProp("w", 1e-6 * w / dbu)
        if (select == "L") :
            r = int(inst.dbGetFloatProp("r", True) * dbu)
            l = int(r * w / (0.26e3 * dbu))
            if (l < int(0.5 * dbu)) :
                l = int(0.5 * dbu)
                r = float(7 * l / w )
                inst.dbReplaceProp("r", r)
                print("The length value is smaller then minimal, adjusting. The new resistance value is: r=", end="")
                print(r)
            if l%xygrid!=0 :
                l = int(xygrid * int(l / xygrid))
                r = float(7 * l / w )
                print("The derived value is of grid, adjusting values. The new resistance value is: r=", end="")
                print(r)
            inst.dbReplaceProp("l", 1e-6 * l / dbu)
            print("The derived length value is: l=", end="")
            print(1e-6 * l / dbu)
            print()
        if (select == "R") :
            l = max(int(inst.dbGetFloatProp("l", True) * 1e6 * dbu), int(inst.dbGetFloatProp("l", True) * 1e9))
            if (l < int(0.5 * dbu)) :
                l = int(0.5 * dbu)
                print("The length value is smaller then minimal, adjusting. The new length value is: l=", end="")
                print(1e-6 * w / dbu)
            if l%xygrid!=0 :
                l = int(xygrid * int(l / xygrid))
                print("The length value is of grid, adjusting. The new length value is: l=", end="")
                print(1e-6 * l / dbu)
            inst.dbReplaceProp("l", 1e-6 * l / dbu)
            r = float(0.26e3 * l / w )
            inst.dbReplaceProp("r", r)
            print("The derived resistance value is: r=", end="")
            print(r)
            print()
    #
    if (name == "rhigh") :
        select = inst.dbGetListProp("calculate", True)
        if (not select) :
            inst.dbAddProp("calculate", "L", "[L, R]")
            select = inst.dbGetListProp("calculate", True)
        print("Calculation mode: ", end="")
        print(select)
        w = max(int(inst.dbGetFloatProp("w", True) * 1e6 * dbu), int(inst.dbGetFloatProp("w", True) * 1e9))
        if (w < int(0.5 * dbu)) :
            w = int(0.5 * dbu)
            print("The width value is smaller then minimal, adjusting. The new width value is: w=", end="")
            print(1e-6 * w / dbu)
        if w%xygrid!=0 :
            w = int(xygrid * int(w / xygrid))
            print("The width value is of grid, adjusting. The new width value is: w=", end="")
            print(1e-6 * w / dbu)
        inst.dbReplaceProp("w", 1e-6 * w / dbu)
        if (select == "L") :
            r = int(inst.dbGetFloatProp("r", True) * dbu)
            l = int(r * w / (1.36e3 * dbu))
            if (l < int(0.5 * dbu)) :
                l = int(0.5 * dbu)
                r = float(7 * l / w )
                inst.dbReplaceProp("r", r)
                print("The length value is smaller then minimal, adjusting. The new resistance value is: r=", end="")
                print(r)
            if l%xygrid!=0 :
                l = int(xygrid * int(l / xygrid))
                r = float(7 * l / w )
                print("The derived value is of grid, adjusting values. The new resistance value is: r=", end="")
                print(r)
            inst.dbReplaceProp("l", 1e-6 * l / dbu)
            print("The derived length value is: l=", end="")
            print(1e-6 * l / dbu)
            print()
        if (select == "R") :
            l = max(int(inst.dbGetFloatProp("l", True) * 1e6 * dbu), int(inst.dbGetFloatProp("l", True) * 1e9))
            if (l < int(0.5 * dbu)) :
                l = int(0.5 * dbu)
                print("The length value is smaller then minimal, adjusting. The new length value is: l=", end="")
                print(1e-6 * w / dbu)
            if l%xygrid!=0 :
                l = int(xygrid * int(l / xygrid))
                print("The length value is of grid, adjusting. The new length value is: l=", end="")
                print(1e-6 * l / dbu)
            r = float(1.36e3 * l / w )
            inst.dbReplaceProp("l", 1e-6 * l / dbu)
            inst.dbReplaceProp("r", r)
            print("The derived resistance value is: r=", end="")
            print(r)
            print()
    #
    if (name == "via") :
        select = inst.dbGetListProp("selection_type", True)
        if (select == "x&y") :
            x = inst.dbGetIntProp("Columns", True)
            y = inst.dbGetIntProp("Rows", True)
            if (x < 1) :
                x = 1
                inst.dbReplaceProp("Columns", x)
                print("You can't have VIAs without VIAs")
                print("_    ////   _")
                print(" \_( O_o')_/")
            if (y < 1) :
                y = 1
                inst.dbReplaceProp("Rows", y)
                print("You can't have VIAs without VIAs")
                print("_    ////   _")
                print(" \_( O_o')_/")
            bottom = inst.dbGetListProp("Bottom", True)
            if (bottom == "Activ") :
                enclose = int(0.07 * dbu)
                size = int(0.16 * dbu)
                space = int(0.18 * dbu)
                if ((x > 4) or (y > 4)) :
                    space = int(0.2 * dbu)
                l = int(x * (size + space) - space + 2 * enclose)
                w = int(y * (size + space) - space + 2 * enclose)
                if l%xygrid!=0 :
                    l = int(xygrid * int(l / xygrid))
                if w%xygrid!=0 :
                    w = int(xygrid * int(w / xygrid))
                inst.dbReplaceProp("l", 1e-6 * l / dbu)
                inst.dbReplaceProp("w", 1e-6 * w / dbu)
                print("The derived parameters are: l=", end="")
                print(1e-6 * l / dbu, end=", w=")
                print(1e-6 * w / dbu)
                print()
            if (bottom == "GatPoly") :
                enclose = int(0.07 * dbu)
                size = int(0.16 * dbu)
                space = int(0.18 * dbu)
                if ((x > 4) or (y > 4)) :
                    space = int(0.2 * dbu)
                l = int(x * (size + space) - space + 2 * enclose)
                w = int(y * (size + space) - space + 2 * enclose)
                if l%xygrid!=0 :
                    l = int(xygrid * int(l / xygrid))
                if w%xygrid!=0 :
                    w = int(xygrid * int(w / xygrid))
                inst.dbReplaceProp("l", 1e-6 * l / dbu)
                inst.dbReplaceProp("w", 1e-6 * w / dbu)
                print("The derived parameters are: l=", end="")
                print(1e-6 * l / dbu, end=", w=")
                print(1e-6 * w / dbu)
                print()
            if ((bottom == "Metal1") or (bottom == "Metal2") or (bottom == "Metal3") or (bottom == "Metal4")) :
                enclose = int(0.05 * dbu)
                size = int(0.19 * dbu)
                space = int(0.22 * dbu)
                if ((x > 3) or (y > 3)) :
                    space = int(0.29 * dbu)
                l = int(x * (size + space) - space + 2 * enclose)
                w = int(y * (size + space) - space + 2 * enclose)
                if l%xygrid!=0 :
                    l = int(xygrid * int(l / xygrid))
                if w%xygrid!=0 :
                    w = int(xygrid * int(w / xygrid))
                inst.dbReplaceProp("l", 1e-6 * l / dbu)
                inst.dbReplaceProp("w", 1e-6 * w / dbu)
                print("The derived parameters are: l=", end="")
                print(1e-6 * l / dbu, end=", w=")
                print(1e-6 * w / dbu)
                print()
            if (bottom == "Metal5") :
                enclose = int(0.42 * dbu)
                size = int(0.42 * dbu)
                space = int(0.42 * dbu)
                l = int(x * (size + space) - space + 2 * enclose)
                w = int(y * (size + space) - space + 2 * enclose)
                if l%xygrid!=0 :
                    l = int(xygrid * int(l / xygrid))
                if w%xygrid!=0 :
                    w = int(xygrid * int(w / xygrid))
                inst.dbReplaceProp("l", 1e-6 * l / dbu)
                inst.dbReplaceProp("w", 1e-6 * w / dbu)
                print("The derived parameters are: l=", end="")
                print(1e-6 * l / dbu, end=", w=")
                print(1e-6 * w / dbu)
                print()
            if (bottom == "TopMetal1") :
                enclose = int(0.5 * dbu)
                size = int(0.9 * dbu)
                space = int(1.06 * dbu)
                l = int(x * (size + space) - space + 2 * enclose)
                w = int(y * (size + space) - space + 2 * enclose)
                if l%xygrid!=0 :
                    l = int(xygrid * int(l / xygrid))
                if w%xygrid!=0 :
                    w = int(xygrid * int(w / xygrid))
                inst.dbReplaceProp("l", 1e-6 * l / dbu)
                inst.dbReplaceProp("w", 1e-6 * w / dbu)
                print("The derived parameters are: l=", end="")
                print(1e-6 * l / dbu, end=", w=")
                print(1e-6 * w / dbu)
                print()
        if (select == "w&l") :
            w = max(int(inst.dbGetFloatProp("w", True) * 1e6 * dbu), int(inst.dbGetFloatProp("w", True) * 1e9))
            if w%xygrid!=0 :
                w = int(xygrid * int(w / xygrid))
                print("The width value is of grid, adjusting. The new width value is: w=", end="")
                print(1e-6 * w / dbu)
            inst.dbReplaceProp("w", 1e-6 * w / dbu)
            l = max(int(inst.dbGetFloatProp("l", True) * 1e6 * dbu), int(inst.dbGetFloatProp("l", True) * 1e9))
            if l%xygrid!=0 :
                l = int(xygrid * int(l / xygrid))
                print("The length value is of grid, adjusting. The new length value is: l=", end="")
                print(1e-6 * l / dbu)
            inst.dbReplaceProp("l", 1e-6 * l / dbu)
            bottom = inst.dbGetListProp("Bottom", True)
            if (bottom == "Activ") :
                enclose = int(0.07 * dbu)
                size = int(0.16 * dbu)
                space = int(0.18 * dbu)
                if (w < int(2 * enclose + size)) :
                    w = int(2 * enclose + size)
                    inst.dbReplaceProp("w", 1e-6 * w / dbu)
                    print("The width value is smaller than minimal, adjusting. The new width value is: w=", end="")
                    print(1e-6 * w / dbu)
                if (l < int(2 * enclose + size)) :
                    l = int(2 * enclose + size)
                    inst.dbReplaceProp("l", 1e-6 * l / dbu)
                    print("The length value is smaller than minimal, adjusting. The new length value is: l=", end="")
                    print(1e-6 * l / dbu)
                x = int((l - 2 * enclose + space) / (size + space))
                y = int((w - 2 * enclose + space) / (size + space))
                if ((x > 4) or (y > 4)) :
                    space = int(0.2 * dbu)
                    x = int((l - 2 * enclose + space) / (size + space))
                    y = int((w - 2 * enclose + space) / (size + space))
                inst.dbReplaceProp("Columns", x)
                inst.dbReplaceProp("Rows", y)
                print("The derived parameters are: Columns=", end="")
                print(x, end=", Rows=")
                print(y)
                print()
            if (bottom == "GatPoly") :
                enclose = int(0.07 * dbu)
                size = int(0.16 * dbu)
                space = int(0.18 * dbu)
                if (w < int(2 * enclose + size)) :
                    w = int(2 * enclose + size)
                    inst.dbReplaceProp("w", 1e-6 * w / dbu)
                    print("The width value is smaller than minimal, adjusting. The new width value is: w=", end="")
                    print(1e-6 * w / dbu)
                if (l < int(2 * enclose + size)) :
                    l = int(2 * enclose + size)
                    inst.dbReplaceProp("l", 1e-6 * l / dbu)
                    print("The length value is smaller than minimal, adjusting. The new length value is: l=", end="")
                    print(1e-6 * l / dbu)
                x = int((l - 2 * enclose + space) / (size + space))
                y = int((w - 2 * enclose + space) / (size + space))
                if ((x > 4) or (y > 4)) :
                    space = int(0.2 * dbu)
                    x = int((l - 2 * enclose + space) / (size + space))
                    y = int((w - 2 * enclose + space) / (size + space))
                inst.dbReplaceProp("Columns", x)
                inst.dbReplaceProp("Rows", y)
                print("The derived parameters are: Columns=", end="")
                print(x, end=", Rows=")
                print(y)
                print()
            if ((bottom == "Metal1") or (bottom == "Metal2") or (bottom == "Metal3") or (bottom == "Metal4")) :
                enclose = int(0.05 * dbu)
                size = int(0.19 * dbu)
                space = int(0.22 * dbu)
                if (w < int(2 * enclose + size)) :
                    w = int(2 * enclose + size)
                    inst.dbReplaceProp("w", 1e-6 * w / dbu)
                    print("The width value is smaller than minimal, adjusting. The new width value is: w=", end="")
                    print(1e-6 * w / dbu)
                if (l < int(2 * enclose + size)) :
                    l = int(2 * enclose + size)
                    inst.dbReplaceProp("l", 1e-6 * l / dbu)
                    print("The length value is smaller than minimal, adjusting. The new length value is: l=", end="")
                    print(1e-6 * l / dbu)
                x = int((l - 2 * enclose + space) / (size + space))
                y = int((w - 2 * enclose + space) / (size + space))
                if ((x > 3) or (y > 3)) :
                    space = int(0.29 * dbu)
                    x = int((l - 2 * enclose + space) / (size + space))
                    y = int((w - 2 * enclose + space) / (size + space))
                inst.dbReplaceProp("Columns", x)
                inst.dbReplaceProp("Rows", y)
                print("The derived parameters are: Columns=", end="")
                print(x, end=", Rows=")
                print(y)
                print()
            if (bottom == "Metal5") :
                enclose = int(0.42 * dbu)
                size = int(0.42 * dbu)
                space = int(0.42 * dbu)
                if (w < int(2 * enclose + size)) :
                    w = int(2 * enclose + size)
                    inst.dbReplaceProp("w", 1e-6 * w / dbu)
                    print("The width value is smaller than minimal, adjusting. The new width value is: w=", end="")
                    print(1e-6 * w / dbu)
                if (l < int(2 * enclose + size)) :
                    l = int(2 * enclose + size)
                    inst.dbReplaceProp("l", 1e-6 * l / dbu)
                    print("The length value is smaller than minimal, adjusting. The new length value is: l=", end="")
                    print(1e-6 * l / dbu)
                x = int((l - 2 * enclose + space) / (size + space))
                y = int((w - 2 * enclose + space) / (size + space))
                inst.dbReplaceProp("Columns", x)
                inst.dbReplaceProp("Rows", y)
                print("The derived parameters are: Columns=", end="")
                print(x, end=", Rows=")
                print(y)
                print()
            if (bottom == "TopMetal1") :
                enclose = int(0.5 * dbu)
                size = int(0.9 * dbu)
                space = int(1.06 * dbu)
                if (w < int(2 * enclose + size)) :
                    w = int(2 * enclose + size)
                    inst.dbReplaceProp("w", 1e-6 * w / dbu)
                    print("The width value is smaller than minimal, adjusting. The new width value is: w=", end="")
                    print(1e-6 * w / dbu)
                if (l < int(2 * enclose + size)) :
                    l = int(2 * enclose + size)
                    inst.dbReplaceProp("l", 1e-6 * l / dbu)
                    print("The length value is smaller than minimal, adjusting. The new length value is: l=", end="")
                    print(1e-6 * l / dbu)
                x = int((l - 2 * enclose + space) / (size + space))
                y = int((w - 2 * enclose + space) / (size + space))
                inst.dbReplaceProp("Columns", x)
                inst.dbReplaceProp("Rows", y)
                print("The derived parameters are: Columns=", end="")
                print(x, end=", Rows=")
                print(y)
                print()
    #
    if (name == "mos") :
        select = inst.dbGetListProp("calculate", True)
        if (not select) :
            inst.dbAddProp("calculate", "finger_width", "[finger_width, total_width]")
            select = inst.dbGetListProp("calculate", True)  
        print("Calculation mode: ", end="")
        print(select)
        l = max(int(inst.dbGetFloatProp("l", True) * 1e6 * dbu), int(inst.dbGetFloatProp("l", True) * 1e9))
        if (cell_name.find("nmosHV") >= 0) :
            if (l < int(0.45 * dbu)) :
                l = int(0.45 * dbu)
                print("The length value is smaller then minimal, adjusting. The new width length is: l=", end="")
                print(1e-6 * l / dbu)
        elif (cell_name.find("pmosHV") >= 0) :
            if (l < int(0.4 * dbu)) :
                l = int(0.4 * dbu)
                print("The length value is smaller then minimal, adjusting. The new length value is: l=", end="")
                print(1e-6 * l / dbu)
        else :
            if (l < int(0.13 * dbu)) :
                l = int(0.13 * dbu)
                print("The length value is smaller then minimal, adjusting. The new length value is: l=", end="")
                print(1e-6 * w / dbu)
                print("This is 130nm technology after all.")
                print("_    ////   _")
                print(" \_( O_o')_/")
        if l%xygrid!=0 :
            l = int(xygrid * int(l / xygrid))
            print("The length value is of grid, adjusting. The new length value is: l=", end="")
            print(1e-6 * l / dbu)
        inst.dbReplaceProp("l", 1e-6 * l / dbu)
        nf = int(inst.dbGetIntProp("ng", True))
        if (nf < 1):
            nf = 1
            inst.dbReplaceProp("ng", nf)
            print("Do you actually want a transistor? Have one anyway: ng=1")
            print("_    ////   _")
            print(" \_( O_o')_/")
        if (select == "finger_width") :
            w = max(int(inst.dbGetFloatProp("w", True) * 1e6 * dbu), int(inst.dbGetFloatProp("w", True) * 1e9))
            if (w < int(0.15 * dbu)) :
                w = int(0.15 * dbu)
                print("The width value is smaller then minimal, adjusting. The new width value is: w=", end="")
                print(1e-6 * w / dbu)
            if w%xygrid!=0 :
                w = int(xygrid * int(w / xygrid))
                print("The width value is of grid, adjusting. The new width value is: w=", end="")
                print(1e-6 * w / dbu)
            fw = int(w / nf)
            if (fw < int(0.15 * dbu)) :
                fw = int(0.15 * dbu)
                w = int(fw * nf)
                print("The finger width value is smaller then minimal, adjusting. The new finger width value is: fw=", end="")
                print(1e-6 * fw / dbu)
                print("The new width value, based on selected number of fingers and derived finger width: w=", end="")
                print(1e-6 * w / dbu)
            if fw%xygrid!=0 :
                fw = int(xygrid * int(fw / xygrid))
                w = int(fw * nf)
                print("The finger width value is of grid, adjusting. The new finger width value is: fw=", end="")
                print(1e-6 * fw / dbu)
                print("The new width value, based on selected number of fingers and derived finger width: w=", end="")
                print(1e-6 * w / dbu)
            inst.dbReplaceProp("w", 1e-6 * w / dbu)
            inst.dbReplaceProp("fw", 1e-6 * fw / dbu)
            print("The finger width value is: fw=", end="")
            print(1e-6 * fw / dbu)
        if (select == "total_width") :
            fw = max(int(inst.dbGetFloatProp("fw", True) * 1e6 * dbu), int(inst.dbGetFloatProp("fw", True) * 1e9))
            if (fw < int(0.15 * dbu)) :
                fw = int(0.15 * dbu)
                print("The finger width value is smaller then minimal, adjusting. The new finger width value is: fw=", end="")
                print(1e-6 * fw / dbu)
            if fw%xygrid!=0 :
                fw = int(xygrid * int(fw / xygrid))
                print("The finger width value is of grid, adjusting. The new finger width value is: fw=", end="")
                print(1e-6 * fw / dbu)
            inst.dbReplaceProp("fw", 1e-6 * fw / dbu)
            w = int(fw * nf)
            inst.dbReplaceProp("w", 1e-6 * w / dbu)
            print("The total width value is: w=", end="")
            print(1e-6 * w / dbu)
    #
    if (name == "isolbox") :
        w = max(int(inst.dbGetFloatProp("w", True) * 1e6 * dbu), int(inst.dbGetFloatProp("w", True) * 1e9))
        if (w < int(3.17 * dbu)) :
            w = int(3.17 * dbu)
            print("The width value is smaller then minimal, adjusting. The new width value is: w=", end="")
            print(1e-6 * w / dbu)
        if w%xygrid!=0 :
            w = int(xygrid * int(w / xygrid))
            print("The width value is of grid, adjusting. The new width value is: w=", end="")
            print(1e-6 * w / dbu)
        inst.dbReplaceProp("w", 1e-6 * w / dbu)
        l = max(int(inst.dbGetFloatProp("l", True) * 1e6 * dbu), int(inst.dbGetFloatProp("l", True) * 1e9))
        if (l < int(3.17 * dbu)) :
            l = int(3.17 * dbu)
            print("The length value is smaller then minimal, adjusting. The new length value is: l=", end="")
            print(1e-6 * l / dbu)
        if l%xygrid!=0 :
            l = int(xygrid * int(l / xygrid))
            print("The length value is of grid, adjusting. The new length value is: l=", end="")
            print(1e-6 * l / dbu)
        inst.dbReplaceProp("l", 1e-6 * l / dbu)
    #
    if (name == "pad") :
        w = max(int(inst.dbGetFloatProp("w", True) * 1e6 * dbu), int(inst.dbGetFloatProp("w", True) * 1e9))
        if (w < int(2.1 * dbu)) :
            w = int(2.1 * dbu)
            print("The width value is smaller then minimal, adjusting. The new width value is: w=", end="")
            print(1e-6 * w / dbu)
        if (w > int(150 * dbu)) :
            w = int(150 * dbu)
            print("The width value is larger then maximal, adjusting. The new width value is: w=", end="")
            print(1e-6 * w / dbu)
        if w%xygrid!=0 :
            w = int(xygrid * int(w / xygrid))
            print("The width value is of grid, adjusting. The new width value is: w=", end="")
            print(1e-6 * w / dbu)
        inst.dbReplaceProp("w", 1e-6 * w / dbu)
    #
    if (name == "sealring") :
        w = max(int(inst.dbGetFloatProp("w", True) * 1e6 * dbu), int(inst.dbGetFloatProp("w", True) * 1e9))
        if (w < int(50 * dbu)) :
            w = int(50 * dbu)
            print("The width value is smaller then minimal, adjusting. The new width value is: w=", end="")
            print(1e-6 * w / dbu)
        if w%xygrid!=0 :
            w = int(xygrid * int(w / xygrid))
            print("The width value is of grid, adjusting. The new width value is: w=", end="")
            print(1e-6 * w / dbu)
        inst.dbReplaceProp("w", 1e-6 * w / dbu)
        l = max(int(inst.dbGetFloatProp("l", True) * 1e6 * dbu), int(inst.dbGetFloatProp("l", True) * 1e9))
        if (l < int(50 * dbu)) :
            l = int(50 * dbu)
            print("The length value is smaller then minimal, adjusting. The new length value is: l=", end="")
            print(1e-6 * l / dbu)
        if l%xygrid!=0 :
            l = int(xygrid * int(l / xygrid))
            print("The length value is of grid, adjusting. The new length value is: l=", end="")
            print(1e-6 * l / dbu)
        inst.dbReplaceProp("l", 1e-6 * l / dbu)
        d = max(int(inst.dbGetFloatProp("d", True) * 1e6 * dbu), int(inst.dbGetFloatProp("d", True) * 1e9))
        if (d < int(7 * dbu)) :
            d = int(7 * dbu)
            print("The distance value is smaller then minimal, adjusting. The new distance value is: d=", end="")
            print(1e-6 * d / dbu)
        if d%xygrid!=0 :
            d = int(xygrid * int(d / xygrid))
            print("The distance value is of grid, adjusting. The new distance value is: d=", end="")
            print(1e-6 * d / dbu)
        inst.dbReplaceProp("d", 1e-6 * d / dbu)
    #
    if (name == "npn13G2") :
        ne = int(inst.dbGetIntProp("NE", True))
        if (ne < 1):
            ne = 1
            inst.dbReplaceProp("NE", ne)
            print("Do you actually want a transistor? Have one anyway: NE=1")
            print("_    ////   _")
            print(" \_( O_o')_/")
        if (ne > 10):
            ne = 10
            inst.dbReplaceProp("NE", ne)
            print("Max number of emitters is 10: NE=10")
    #
    if (name == "SVaricap") :
        model = inst.dbGetStringProp("model", True)
        if(not model) :
            inst.dbAddProp("model", "sg13_hv_svaricap")
        type = inst.dbGetStringProp("type", True)
        if(not type) :
            inst.dbAddProp("type", "cap")
        nx = int(inst.dbGetIntProp("Nx", True))
        if (nx < 1):
            nx = 1
            inst.dbReplaceProp("Nx", nx)
            print("Do you actually want a varactor? Have one anyway: Nx=1")
            print("_    ////   _")
            print(" \_( O_o')_/")
        if (nx > 10):
            nx = 10
            inst.dbReplaceProp("Nx", nx)
            print("Max number of \"fingers\" is 10: Nx=10")
        width = inst.dbGetListProp("Width", True)
        if (not width) :
            inst.dbAddProp("Width", "3.74u", "[3.74u , 9.74u]")
            width = inst.dbGetListProp("Width", True)  
        length = inst.dbGetListProp("Length", True)
        if (not length) :
            inst.dbAddProp("Length", "0.3u", "[0.3u, 0.8u]")  
            length = inst.dbGetListProp("Length", True)  
        w = inst.dbGetFloatProp("w", True)
        l = inst.dbGetFloatProp("l", True)
        if (width == "3.74u"):
            w = 3.74e-6
            inst.dbReplaceProp("w", w)
        else :
            w = 9.74e-6
            inst.dbReplaceProp("w", w)
        if (length == "0.3u"):
            l = 0.3e-6
            inst.dbReplaceProp("l", l)
        else :
            l = 0.8e-6
            inst.dbReplaceProp("l", l)
    #
    if (name == "nmoscl_2") :
        model = inst.dbGetStringProp("model", True)
        if(not model) :
            inst.dbAddProp("model", "nmoscl_2")
        type = inst.dbGetStringProp("type", True)
        if(not type) :
            inst.dbAddProp("type", "dio")
   #
    if (name == "nmoscl_4") :
        model = inst.dbGetStringProp("model", True)
        if(not model) :
            inst.dbAddProp("model", "nmoscl_4")
        type = inst.dbGetStringProp("type", True)
        if(not type) :
            inst.dbAddProp("type", "dio")
    #
    if (name == "dantenna") :
        model = inst.dbGetStringProp("model", True)
        if(not model) :
            inst.dbAddProp("model", "dantenna")
        type = inst.dbGetStringProp("type", True)
        if(not type) :
            inst.dbAddProp("type", "dio")
        w = max(int(inst.dbGetFloatProp("Width", True) * 1e6 * dbu), int(inst.dbGetFloatProp("Width", True) * 1e9))
        if (w < int(0.78 * dbu)) :
            w = int(0.78 * dbu)
            print("The width value is smaller then minimal, adjusting. The new width value is: w=", end="")
            print(1e-6 * w / dbu)
        if (w%xygrid) :
            w = int(xygrid * int(w / xygrid))
            print("The width value is of grid, adjusting. The new width value is: w=", end="")
            print(1e-6 * w / dbu)   
        inst.dbReplaceProp("Width", 1e-6 * (w / dbu))
        l = max(int(inst.dbGetFloatProp("Length", True) * 1e6 * dbu), int(inst.dbGetFloatProp("Length", True) * 1e9))
        if (l < int(0.78 * dbu)) :
            l = int(0.78 * dbu)
            print("The length value is smaller then minimal, adjusting. The new width value is: l=", end="")
            print(1e-6 * l / dbu)
        if (l%xygrid) :
            l = int(xygrid * int(l / xygrid))
            print("The length value is of grid, adjusting. The new width value is: l=", end="")
            print(1e-6 * l / dbu)   
        inst.dbReplaceProp("Length", 1e-6 * (l / dbu))
    #
    if (name == "dpantenna") :
        model = inst.dbGetStringProp("model", True)
        if(not model) :
            inst.dbAddProp("model", "dpantenna")
        type = inst.dbGetStringProp("type", True)
        if(not type) :
            inst.dbAddProp("type", "dio")
        w = max(int(inst.dbGetFloatProp("Width", True) * 1e6 * dbu), int(inst.dbGetFloatProp("Width", True) * 1e9))
        if (w < int(0.78 * dbu)) :
            w = int(0.78 * dbu)
            print("The width value is smaller then minimal, adjusting. The new width value is: w=", end="")
            print(1e-6 * w / dbu)
        if (w%xygrid) :
            w = int(xygrid * int(w / xygrid))
            print("The width value is of grid, adjusting. The new width value is: w=", end="")
            print(1e-6 * w / dbu)   
        inst.dbReplaceProp("Width", 1e-6 * (w / dbu))
        l = max(int(inst.dbGetFloatProp("Length", True) * 1e6 * dbu), int(inst.dbGetFloatProp("Length", True) * 1e9))
        if (l < int(0.78 * dbu)) :
            l = int(0.78 * dbu)
            print("The length value is smaller then minimal, adjusting. The new width value is: l=", end="")
            print(1e-6 * l / dbu)
        if (l%xygrid) :
            l = int(xygrid * int(l / xygrid))
            print("The length value is of grid, adjusting. The new width value is: l=", end="")
            print(1e-6 * w / dbu)   
        inst.dbReplaceProp("Length", 1e-6 * (l / dbu))
    #