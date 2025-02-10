def callback(pyDBObject) :
    lib = pyDBObject.lib()
    tech = lib.tech()
    dbu = lib.dbuPerUU()
    xygrid = int(0.005 * dbu)
    inst = pyDBObject.toInst()
    cell_name = pyDBObject.cellName()
    if (cell_name.find("mim") >= 0) :
        name = "mim"
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
    print()
    print("The device model is: ", end="")
    print(name)
    if (name == "mim") :
        select = inst.dbGetListProp("calculate", True)
        if (not select) :
            inst.dbAddProp("calculate", "L", "[L, C]")
            select = inst.dbGetListProp("calculate", True)  
        print("Calculation mode: ", end="")
        print(select)
        w = max(int(inst.dbGetFloatProp("w", True) * 1e6 * dbu), int(inst.dbGetFloatProp("w", True) * 1e9))
        if (w < int(1.14 * dbu)) :
            w = int(1.14 * dbu)
            inst.dbReplaceProp("w", 1e-6 * w / dbu)
            print("The width value is smaller then minimal, adjusting. The new width value is: w=", end="")
            print(1e-6 * w / dbu)
        if w%xygrid!=0 :
                w = int(xygrid * int(w / xygrid))
                inst.dbReplaceProp("w", 1e-6 * w / dbu)
                print("The width value is of grid, adjusting. The new width value is: w=", end="")
                print(1e-6 * w / dbu)
        if (select == "L") :
            c = max(int(inst.dbGetFloatProp("c", True) * 1e15 * dbu), int(inst.dbGetFloatProp("c", True) * 1e18))
            if (c < int(1.95 * dbu)) :
                c = int(1.95 * dbu)
                inst.dbReplaceProp("c", 1e-15 * c / dbu)
                print("The capacitance is smaller than minimal, adjusting capacitance. The new capactiance value is: c=", end="")
                print(1e-15 * c / dbu)
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
                inst.dbReplaceProp("l", 1e-6 * l / dbu)
                print("The length value is smaller then minimal, adjusting. The new length value is: l=", end="")
                print(1e-6 * w / dbu)
            if (w * l > int(5625 * dbu * dbu)) :
                l = int(int(5625 * dbu * dbu) / w)
                inst.dbReplaceProp("l", 1e-6 * l / dbu)
                print("The area is larger than maximal, adjusting. The new length value is: l=", end="")
                print(1e-6 * l / dbu)
            if l%xygrid!=0 :
                l = int(xygrid * int(l / xygrid))
                inst.dbReplaceProp("l", 1e-6 * l / dbu)
                print("The length value is of grid, adjusting. The new length value is: l=", end="")
                print(1e-6 * l / dbu)
            c = float(w * l * 1.5 / (dbu * dbu))
            inst.dbReplaceProp("c", 1e-15 * c)
            print("The derived capacitance value is: c=", end="")
            print(1e-15 * c)
            print()
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
            inst.dbReplaceProp("w", 1e-6 * w / dbu)
            print("The width value is smaller then minimal, adjusting. The new width value is: w=", end="")
            print(1e-6 * w / dbu)
        if w%xygrid!=0 :
                w = int(xygrid * int(w / xygrid))
                inst.dbReplaceProp("w", 1e-6 * w / dbu)
                print("The width value is of grid, adjusting. The new width value is: w=", end="")
                print(1e-6 * w / dbu)
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
                inst.dbReplaceProp("l", 1e-6 * l / dbu)
                print("The length value is smaller then minimal, adjusting. The new length value is: l=", end="")
                print(1e-6 * w / dbu)
            if l%xygrid!=0 :
                l = int(xygrid * int(l / xygrid))
                inst.dbReplaceProp("l", 1e-6 * l / dbu)
                print("The length value is of grid, adjusting. The new length value is: l=", end="")
                print(1e-6 * l / dbu)
            r = float(7 * l / w )
            inst.dbReplaceProp("r", r)
            print("The derived resistance value is: r=", end="")
            print(r)
            print()
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
            inst.dbReplaceProp("w", 1e-6 * w / dbu)
            print("The width value is smaller then minimal, adjusting. The new width value is: w=", end="")
            print(1e-6 * w / dbu)
        if w%xygrid!=0 :
                w = int(xygrid * int(w / xygrid))
                inst.dbReplaceProp("w", 1e-6 * w / dbu)
                print("The width value is of grid, adjusting. The new width value is: w=", end="")
                print(1e-6 * w / dbu)
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
                inst.dbReplaceProp("l", 1e-6 * l / dbu)
                print("The length value is smaller then minimal, adjusting. The new length value is: l=", end="")
                print(1e-6 * w / dbu)
            if l%xygrid!=0 :
                l = int(xygrid * int(l / xygrid))
                inst.dbReplaceProp("l", 1e-6 * l / dbu)
                print("The length value is of grid, adjusting. The new length value is: l=", end="")
                print(1e-6 * l / dbu)
            r = float(0.26e3 * l / w )
            inst.dbReplaceProp("r", r)
            print("The derived resistance value is: r=", end="")
            print(r)
            print()
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
            inst.dbReplaceProp("w", 1e-6 * w / dbu)
            print("The width value is smaller then minimal, adjusting. The new width value is: w=", end="")
            print(1e-6 * w / dbu)
        if w%xygrid!=0 :
                w = int(xygrid * int(w / xygrid))
                inst.dbReplaceProp("w", 1e-6 * w / dbu)
                print("The width value is of grid, adjusting. The new width value is: w=", end="")
                print(1e-6 * w / dbu)
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
                inst.dbReplaceProp("l", 1e-6 * l / dbu)
                print("The length value is smaller then minimal, adjusting. The new length value is: l=", end="")
                print(1e-6 * w / dbu)
            if l%xygrid!=0 :
                l = int(xygrid * int(l / xygrid))
                inst.dbReplaceProp("l", 1e-6 * l / dbu)
                print("The length value is of grid, adjusting. The new length value is: l=", end="")
                print(1e-6 * l / dbu)
            r = float(1.36e3 * l / w )
            inst.dbReplaceProp("r", r)
            print("The derived resistance value is: r=", end="")
            print(r)
            print()
    if (name == "via") :
        select = inst.dbGetListProp("selection_type", True)
        if (select == "x&y") :
            x = inst.dbGetIntProp("x", True)
            y = inst.dbGetIntProp("y", True)
            if (x < 1) :
                x = 1
                inst.dbReplaceProp("x", x)
                print("You can't have VIAs without VIAs")
                print("_    ////   _")
                print(" \_( O_o')_/")
            if (y < 1) :
                y = 1
                inst.dbReplaceProp("y", y)
                print("You can't have VIAs without VIAs")
                print("_    ////   _")
                print(" \_( O_o')_/")
            via = inst.dbGetListProp("via", True)
            if (via == "am1") :
                enclose = int(0.07 * dbu)
                size = int(0.16 * dbu)
                space = int(0.18 * dbu)
                if ((x > 4) and (y > 4)) :
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
            if (via == "pm1") :
                enclose = int(0.07 * dbu)
                size = int(0.16 * dbu)
                space = int(0.18 * dbu)
                if ((x > 4) and (y > 4)) :
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
            if ((via == "m1m2") or (via == "m2m3") or (via == "m3m4") or (via == "m4m5")) :
                enclose = int(0.05 * dbu)
                size = int(0.19 * dbu)
                space = int(0.22 * dbu)
                if ((x > 3) and (y > 3)) :
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
            if (via == "m5tm1") :
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
            if (via == "tm1tm2") :
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
                inst.dbReplaceProp("w", 1e-6 * w / dbu)
                print("The width value is of grid, adjusting. The new width value is: w=", end="")
                print(1e-6 * w / dbu)
            l = max(int(inst.dbGetFloatProp("l", True) * 1e6 * dbu), int(inst.dbGetFloatProp("l", True) * 1e9))
            if l%xygrid!=0 :
                l = int(xygrid * int(l / xygrid))
                inst.dbReplaceProp("l", 1e-6 * l / dbu)
                print("The length value is of grid, adjusting. The new length value is: l=", end="")
                print(1e-6 * l / dbu)
            via = inst.dbGetListProp("via", True)
            if (via == "am1") :
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
                if ((x > 4) and (y > 4)) :
                    space = int(0.2 * dbu)
                    x = int((l - 2 * enclose + space) / (size + space))
                    y = int((w - 2 * enclose + space) / (size + space))
                inst.dbReplaceProp("x", x)
                inst.dbReplaceProp("y", y)
                print("The derived parameters are: x=", end="")
                print(x, end=", y=")
                print(y)
                print()
            if (via == "pm1") :
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
                if ((x > 4) and (y > 4)) :
                    space = int(0.2 * dbu)
                    x = int((l - 2 * enclose + space) / (size + space))
                    y = int((w - 2 * enclose + space) / (size + space))
                inst.dbReplaceProp("x", x)
                inst.dbReplaceProp("y", y)
                print("The derived parameters are: x=", end="")
                print(x, end=", y=")
                print(y)
                print()
            if ((via == "m1m2") or (via == "m2m3") or (via == "m3m4") or (via == "m4m5")) :
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
                if ((x > 3) and (y > 3)) :
                    space = int(0.29 * dbu)
                    x = int((l - 2 * enclose + space) / (size + space))
                    y = int((w - 2 * enclose + space) / (size + space))
                inst.dbReplaceProp("x", x)
                inst.dbReplaceProp("y", y)
                print("The derived parameters are: x=", end="")
                print(x, end=", y=")
                print(y)
                print()
            if (via == "m5tm1") :
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
                inst.dbReplaceProp("x", x)
                inst.dbReplaceProp("y", y)
                print("The derived parameters are: x=", end="")
                print(x, end=", y=")
                print(y)
                print()
            if (via == "tm1tm2") :
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
                inst.dbReplaceProp("x", x)
                inst.dbReplaceProp("y", y)
                print("The derived parameters are: x=", end="")
                print(x, end=", y=")
                print(y)
                print()
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
                inst.dbReplaceProp("l", 1e-6 * l / dbu)
                print("The length value is smaller then minimal, adjusting. The new width length is: l=", end="")
                print(1e-6 * l / dbu)
        elif (cell_name.find("pmosHV") >= 0) :
            if (l < int(0.4 * dbu)) :
                l = int(0.4 * dbu)
                inst.dbReplaceProp("l", 1e-6 * l / dbu)
                print("The length value is smaller then minimal, adjusting. The new length value is: l=", end="")
                print(1e-6 * l / dbu)
        else :
            if (l < int(0.13 * dbu)) :
                l = int(0.13 * dbu)
                inst.dbReplaceProp("l", 1e-6 * l / dbu)
                print("The length value is smaller then minimal, adjusting. The new length value is: l=", end="")
                print(1e-6 * w / dbu)
                print("This is 130nm technology after all.")
                print("_    ////   _")
                print(" \_( O_o')_/")
        if l%xygrid!=0 :
            l = int(xygrid * int(l / xygrid))
            inst.dbReplaceProp("l", 1e-6 * l / dbu)
            print("The length value is of grid, adjusting. The new length value is: l=", end="")
            print(1e-6 * l / dbu)
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
                inst.dbReplaceProp("w", 1e-6 * w / dbu)
                print("The width value is smaller then minimal, adjusting. The new width value is: w=", end="")
                print(1e-6 * w / dbu)
            if w%xygrid!=0 :
                w = int(xygrid * int(w / xygrid))
                inst.dbReplaceProp("w", 1e-6 * w / dbu)
                print("The width value is of grid, adjusting. The new width value is: w=", end="")
                print(1e-6 * w / dbu)
            fw = int(w / nf)
            if (fw < int(0.15 * dbu)) :
                fw = int(0.15 * dbu)
                w = int(fw * nf)
                inst.dbReplaceProp("fw", 1e-6 * fw / dbu)
                inst.dbReplaceProp("w", 1e-6 * w / dbu)
                print("The finger width value is smaller then minimal, adjusting. The new finger width value is: fw=", end="")
                print(1e-6 * fw / dbu)
                print("The new width value, based on selected number of fingers and derived finger width: w=", end="")
                print(1e-6 * w / dbu)
            elif fw%xygrid!=0 :
                fw = int(xygrid * int(fw / xygrid))
                w = int(fw * nf)
                inst.dbReplaceProp("fw", 1e-6 * fw / dbu)
                inst.dbReplaceProp("w", 1e-6 * w / dbu)
                print("The finger width value is of grid, adjusting. The new finger width value is: fw=", end="")
                print(1e-6 * fw / dbu)
                print("The new width value, based on selected number of fingers and derived finger width: w=", end="")
                print(1e-6 * w / dbu)
            else :
                inst.dbReplaceProp("fw", 1e-6 * fw / dbu)
                print("The finger width value is: fw=", end="")
                print(1e-6 * fw / dbu)
        if (select == "total_width") :
            fw = max(int(inst.dbGetFloatProp("fw", True) * 1e6 * dbu), int(inst.dbGetFloatProp("fw", True) * 1e9))
            if (fw < int(0.15 * dbu)) :
                fw = int(0.15 * dbu)
                inst.dbReplaceProp("fw", 1e-6 * fw / dbu)
                print("The finger width value is smaller then minimal, adjusting. The new finger width value is: fw=", end="")
                print(1e-6 * fw / dbu)
            if fw%xygrid!=0 :
                fw = int(xygrid * int(fw / xygrid))
                inst.dbReplaceProp("fw", 1e-6 * fw / dbu)
                print("The finger width value is of grid, adjusting. The new finger width value is: fw=", end="")
                print(1e-6 * fw / dbu)
            w = int(fw * nf)
            inst.dbReplaceProp("w", 1e-6 * w / dbu)
            print("The total width value is: w=", end="")
            print(1e-6 * w / dbu)
    if (name == "isolbox") :
        w = max(int(inst.dbGetFloatProp("w", True) * 1e6 * dbu), int(inst.dbGetFloatProp("w", True) * 1e9))
        if w%xygrid!=0 :
                w = int(xygrid * int(w / xygrid))
                inst.dbReplaceProp("w", 1e-6 * w / dbu)
                print("The width value is of grid, adjusting. The new width value is: w=", end="")
                print(1e-6 * w / dbu)
        if (w < int(3.17 * dbu)) :
                w = int(3.17 * dbu)
                inst.dbReplaceProp("w", 1e-6 * w / dbu)
                print("The width value is smaller then minimal, adjusting. The new width value is: w=", end="")
                print(1e-6 * w / dbu)
        l = max(int(inst.dbGetFloatProp("l", True) * 1e6 * dbu), int(inst.dbGetFloatProp("l", True) * 1e9))
        if l%xygrid!=0 :
            l = int(xygrid * int(l / xygrid))
            inst.dbReplaceProp("l", 1e-6 * l / dbu)
            print("The length value is of grid, adjusting. The new length value is: l=", end="")
            print(1e-6 * l / dbu)
        if (l < int(3.17 * dbu)) :
                l = int(3.17 * dbu)
                inst.dbReplaceProp("l", 1e-6 * l / dbu)
                print("The length value is smaller then minimal, adjusting. The new length value is: l=", end="")
                print(1e-6 * l / dbu)
    if (name == "pad") :
        w = max(int(inst.dbGetFloatProp("w", True) * 1e6 * dbu), int(inst.dbGetFloatProp("w", True) * 1e9))
        if w%xygrid!=0 :
                w = int(xygrid * int(w / xygrid))
                inst.dbReplaceProp("w", 1e-6 * w / dbu)
                print("The width value is of grid, adjusting. The new width value is: w=", end="")
                print(1e-6 * w / dbu)
        if (w < int(30 * dbu)) :
                w = int(30 * dbu)
                inst.dbReplaceProp("w", 1e-6 * w / dbu)
                print("The width value is smaller then minimal, adjusting. The new width value is: w=", end="")
                print(1e-6 * w / dbu)
        if (w > int(150 * dbu)) :
                w = int(150 * dbu)
                inst.dbReplaceProp("w", 1e-6 * w / dbu)
                print("The width value is larger then maximal, adjusting. The new width value is: w=", end="")
                print(1e-6 * w / dbu)
    if (name == "sealring") :
        w = max(int(inst.dbGetFloatProp("w", True) * 1e6 * dbu), int(inst.dbGetFloatProp("w", True) * 1e9))
        if w%xygrid!=0 :
                w = int(xygrid * int(w / xygrid))
                inst.dbReplaceProp("w", 1e-6 * w / dbu)
                print("The width value is of grid, adjusting. The new width value is: w=", end="")
                print(1e-6 * w / dbu)
        if (w < int(50 * dbu)) :
                w = int(50 * dbu)
                inst.dbReplaceProp("w", 1e-6 * w / dbu)
                print("The width value is smaller then minimal, adjusting. The new width value is: w=", end="")
                print(1e-6 * w / dbu)
        l = max(int(inst.dbGetFloatProp("l", True) * 1e6 * dbu), int(inst.dbGetFloatProp("l", True) * 1e9))
        if l%xygrid!=0 :
            l = int(xygrid * int(l / xygrid))
            inst.dbReplaceProp("l", 1e-6 * l / dbu)
            print("The length value is of grid, adjusting. The new length value is: l=", end="")
            print(1e-6 * l / dbu)
        if (l < int(50 * dbu)) :
                l = int(50 * dbu)
                inst.dbReplaceProp("l", 1e-6 * l / dbu)
                print("The length value is smaller then minimal, adjusting. The new length value is: l=", end="")
                print(1e-6 * l / dbu)
        d = max(int(inst.dbGetFloatProp("d", True) * 1e6 * dbu), int(inst.dbGetFloatProp("d", True) * 1e9))
        if d%xygrid!=0 :
            d = int(xygrid * int(d / xygrid))
            inst.dbReplaceProp("d", 1e-6 * d / dbu)
            print("The distance value is of grid, adjusting. The new distance value is: d=", end="")
            print(1e-6 * d / dbu)
        if (d < int(7 * dbu)) :
                d = int(7 * dbu)
                inst.dbReplaceProp("d", 1e-6 * d / dbu)
                print("The distance value is smaller then minimal, adjusting. The new distance value is: d=", end="")
                print(1e-6 * d / dbu)