#!/bin/python

# baseOsCsv = "/home/hachi/Desktop/Work/PLCT-Working/Note/OERV-软件包分级-baseOS.csv"
baseOsTxt = "/home/hachi/Desktop/Work/PLCT-Working/Note/oe.txt"
logCsv = "/home/hachi/Desktop/Work/mugen/res_list/failureCause.csv"

baseOsTestedCsv = "/home/hachi/Desktop/Work/PLCT-Working/Done/Week8/csv/baseOS_tested.csv"
# baseOsUntestedCsv = "/home/hachi/Desktop/Work/PLCT-Working/Done/Week8/csv/baseOS_untested.csv"

filteredLogCsv = "/home/hachi/Desktop/Work/PLCT-Working/Done/Week8/csv/baseOS.csv"
filteredLogCsvN = "/home/hachi/Desktop/Work/PLCT-Working/Done/Week8/csv/not_baseOS.csv"
filteredFailLogCsv = "/home/hachi/Desktop/Work/PLCT-Working/Done/Week8/csv/baseOS_fail.csv"
filteredX86FailLogCsv = "/home/hachi/Desktop/Work/PLCT-Working/Done/Week8/csv/baseOS_x86_fail.csv"

splitter = ","  # csv splitter
baseOSList = []  # baseOS package name list
pkg2suite = {"openjdk-1.8.0": ["java-1.8.0-openjdk"],
             "PyYAML": ["pyyaml"],
             "libX11": ["libx11"],
             "tpm-tools": ["tpm-tools_20.03"],
             "rhash": ["rhash_1.4.2"],
             "hwloc": ["hwloc_1.11.9", "hwloc_2.7.1"],
             "enchant2": ["enchant2_2.2.15", "enchant2_2.3.3"]}

suite2pkg = {}
for k in pkg2suite.keys():
    for p in pkg2suite[k]:
        suite2pkg[p] = k

baseOSTested = {}

# read baseOS package list
with open(baseOsTxt, "r", encoding="utf-8") as baseOsFile:

    while True:
        pkg = baseOsFile.readline()
        if pkg == "":
            break
        if pkg.strip() == "":
            continue

        key = pkg.strip()
        baseOSList.append(key)
        baseOSTested[key] = []

# split failureCause.csv and output baseOS fail only
with open(logCsv, "r", encoding="utf-8") as logFile:
    title = logFile.readline()  # read title
    with open(filteredLogCsv, "w", encoding="utf-8") as outFile, \
            open(filteredLogCsvN, "w", encoding="utf-8") as dropFile, \
            open(filteredFailLogCsv, "w", encoding="utf-8") as failFile, \
            open(filteredX86FailLogCsv, "w", encoding="utf-8") as x86FailFile:
        outFile.write(title)
        dropFile.write(title)

        suiteName = ""
        firstFail = True
        firstX86Fail = True
        while True:
            line = logFile.readline()
            if line == "":
                break
            if line.strip() == "":
                print("Empty line ?")
                continue

            # edit link
            outline = line.replace("./mugen-riscv", "https://github.com/KotorinMinami/res_list/tree/master/mugen-riscv")

            lineSplit = outline.split(splitter, 1)
            if len(lineSplit) < 2:
                print("Wrong splitter ?")
                break

            if lineSplit[0].strip() != "":
                suiteName = lineSplit[0].strip()  # use new pkg name
                firstFail = True
                firstX86Fail = True

            # baseOS
            if suiteName in baseOSList:
                outFile.write(outline)
                if suiteName not in baseOSTested[suiteName]:
                    baseOSTested[suiteName].append(suiteName)

                # fail only
                if lineSplit[1].split(splitter)[1].strip() == "fail":
                    if firstFail:
                        firstFail = False
                        failFile.write(suiteName + splitter + lineSplit[1])
                    else:
                        failFile.write(splitter + lineSplit[1])

                # x86 fail only
                if lineSplit[1].split(splitter)[1].strip() == "x86 fail":
                    if firstX86Fail:
                        firstX86Fail = False
                        x86FailFile.write(suiteName + splitter + lineSplit[1])
                    else:
                        x86FailFile.write(splitter + lineSplit[1])
            elif suiteName in suite2pkg and suite2pkg[suiteName] in baseOSList:
                outFile.write(outline)
                if suiteName not in baseOSTested[suite2pkg[suiteName]]:
                    baseOSTested[suite2pkg[suiteName]].append(suiteName)

                # fail only
                if lineSplit[1].split(splitter)[1].strip() == "fail":
                    if firstFail:
                        firstFail = False
                        failFile.write(suiteName + splitter + lineSplit[1])
                    else:
                        failFile.write(splitter + lineSplit[1])

                # x86 fail only
                if lineSplit[1].split(splitter)[1].strip() == "x86 fail":
                    if firstX86Fail:
                        firstX86Fail = False
                        x86FailFile.write(suiteName + splitter + lineSplit[1])
                    else:
                        x86FailFile.write(splitter + lineSplit[1])
            else:
                dropFile.write(outline)

            # baseOS fail only

# tested baseOS packages
with open(baseOsTestedCsv, "w", encoding="utf-8") as testedFile:
    testedFile.write("BaseOS-Name" + splitter + "Mugen-Tests\n")

    for k in baseOSTested.keys():
        if len(baseOSTested[k]) != 0:
            testedFile.write(k + splitter + str(baseOSTested[k])[1:-1].replace("'", "").replace(",", " ") + "\n")
