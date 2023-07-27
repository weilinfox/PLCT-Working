
cf1 = "./class1.csv"
cf2 = "./class2.csv"
cf3 = "./class3.csv"
cfd = "./drop.csv"

with open("./baseOS_x86_fail.csv", "r", encoding="utf-8") as inf:
    title = inf.readline()

    with open(cf1, "w", encoding="utf-8") as cff1, \
            open(cf2, "w", encoding="utf-8") as cff2, \
            open(cf3, "w", encoding="utf-8") as cff3, \
            open(cfd, "w", encoding="utf-8") as cffd:
        cff1.write(title)
        cff2.write(title)
        cff3.write(title)

        pkg = ""
        flg1, flg2, flg3 = False, False, False
        while True:
            inline = inf.readline()
            if inline == "":
                break
            elif inline.strip() == "":
                print("Empty line ?")
                continue

            newPkg, pkgInf = inline.split(",", 1)

            if newPkg.strip() != "" and newPkg != pkg:
                pkg = newPkg
                flg1, flg2, flg3 = False, False, False

            if "基本一致" in pkgInf:
                outPkg = "" if flg1 else pkg
                flg1 = True
                cff2.write(outPkg+","+pkgInf)
            elif "一致" in pkgInf:
                outPkg = "" if flg2 else pkg
                flg2 = True
                cff1.write(outPkg+","+pkgInf)
            elif "不同" in pkgInf:
                outPkg = "" if flg3 else pkg
                flg3 = True
                cff3.write(outPkg+","+pkgInf)
            else:
                cffd.write(pkg+","+pkgInf)

