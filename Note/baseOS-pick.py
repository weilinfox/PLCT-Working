#!/bin/python

baseOsCsv = "/home/hachi/Desktop/Work/PLCT-Working/Note/OERV-软件包分级-baseOS.csv"
logCsv = "/home/hachi/Desktop/Work/mugen/res_list/Pagerd_failureCause.csv"

baseOsTestedCsv = "/home/hachi/Desktop/Work/PLCT-Working/Done/Week8/csv/baseOS_tested.csv"
# baseOsUntestedCsv = "/home/hachi/Desktop/Work/PLCT-Working/Done/Week8/csv/baseOS_untested.csv"

filteredLogCsv = "/home/hachi/Desktop/Work/PLCT-Working/Done/Week8/csv/baseOS.csv"
filteredLogCsvN = "/home/hachi/Desktop/Work/PLCT-Working/Done/Week8/csv/not_baseOS.csv"
filteredFailLogCsv = "/home/hachi/Desktop/Work/PLCT-Working/Done/Week8/csv/baseOS_fail.csv"

splitter = ","  # csv splitter
baseOSList = ["os-basic", "os-storage",
              "smoke-basic-os", "smoke-baseinfo",
              "embedded_application_develop_tests", "embedded_os_basic_test", "embedded_tiny_image_test", "embedded_third_party_packages_test",
              "FS_Device", "FS_Directory", "FS_Negative", "FS_Raw"]  # baseOS package name list
notBaseOSList = ["AT"]
pkg2suite = {"openjdk-1.8.0": ["java-1.8.0-openjdk"],
             "tpm-tools": ["tpm-tools_20.03"],
             "rhash": ["rhash_1.4.2"],
             "hwloc": ["hwloc_1.11.9", "hwloc_2.7.1"],
             "enchant2": ["enchant2_2.2.15", "enchant2_2.3.3"]}

suite2pkg = {}
for k in pkg2suite.keys():
    for p in pkg2suite[k]:
        suite2pkg[p.lower()] = k.lower()

baseOSTested = {}
for i in range(len(baseOSList)):
    baseOSTested[baseOSList[i].lower()] = (baseOSList[i], [])  # (origin_name, mugen_suites)
    baseOSList[i] = baseOSList[i].lower()

# read baseOS package list
with open(baseOsCsv, "r", encoding="utf-8") as baseOsFile:
    baseOsFile.readline()  # drop title

    while True:
        pkg = baseOsFile.readline()
        if pkg == "":
            break
        if pkg.strip() == "":
            continue

        pkgSplit = pkg.split(splitter)
        if len(pkgSplit) == 0:
            continue

        key = pkgSplit[0].strip()
        baseOSList.append(key.lower())  # store pkg name in lowercase
        baseOSTested[key.lower()] = (key, [])

# split failureCause.csv and output baseOS fail only
with open(logCsv, "r", encoding="utf-8") as logFile:
    title = logFile.readline()  # read title
    with open(filteredLogCsv, "w", encoding="utf-8") as outFile, \
            open(filteredLogCsvN, "w", encoding="utf-8") as dropFile, \
            open(filteredFailLogCsv, "w", encoding="utf-8") as failFile:
        outFile.write(title)
        dropFile.write(title)

        suiteName = ""
        firstFail = True
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

            # baseOS
            if suiteName not in notBaseOSList and suiteName.lower() in baseOSList:
                outFile.write(outline)
                if suiteName not in baseOSTested[suiteName.lower()][1]:
                    baseOSTested[suiteName.lower()][1].append(suiteName)

                # fail only
                if lineSplit[1].split(splitter)[1].strip() == "fail":
                    if firstFail:
                        firstFail = False
                        failFile.write(suiteName + splitter + lineSplit[1])
                    else:
                        failFile.write(splitter + lineSplit[1])
            elif suiteName not in notBaseOSList and suiteName.lower() in suite2pkg and suite2pkg[suiteName] in baseOSList:
                outFile.write(outline)
                if suiteName not in baseOSTested[suite2pkg[suiteName]][1]:
                    baseOSTested[suite2pkg[suiteName]][1].append(suiteName)

                # fail only
                if lineSplit[1].split(splitter)[1].strip() == "fail":
                    if firstFail:
                        firstFail = False
                        failFile.write(suiteName + splitter + lineSplit[1])
                    else:
                        failFile.write(splitter + lineSplit[1])
            else:
                dropFile.write(outline)

            # baseOS fail only

# tested baseOS packages
with open(baseOsTestedCsv, "w", encoding="utf-8") as testedFile:
    testedFile.write("BaseOS-Name" + splitter + "Mugen-Tests\n")

    for v in baseOSTested.values():
        if len(v[1]) != 0:
            testedFile.write(v[0] + splitter + str(v[1])[1:-1].replace("'", "").replace(",", " ") + "\n")
