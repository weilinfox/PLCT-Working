#!/bin/python

baseOsCsv = "/home/hachi/Desktop/Work/PLCT-Working/Note/OERV-软件包分级-baseOS.csv"
logCsv = "/home/hachi/Desktop/Work/mugen/res_list/failureCause.csv"

baseOsTestedCsv = "/home/hachi/Desktop/Work/PLCT-Working/Done/Week8/baseOS_tested.csv"
baseOsUntestedCsv = "/home/hachi/Desktop/Work/PLCT-Working/Done/Week8/baseOS_untested.csv"

filteredLogCsv = "/home/hachi/Desktop/Work/PLCT-Working/Done/Week8/baseOS.csv"
filteredLogCsvN = "/home/hachi/Desktop/Work/PLCT-Working/Done/Week8/not_baseOS.csv"
filteredFailLogCsv = "/home/hachi/Desktop/Work/PLCT-Working/Done/Week8/baseOS_fail.csv"

splitter = ","  # csv splitter
baseOSList = ["os-basic", "os-storage",
              "smoke-basic-os", "smoke-iSulad", "smoke-baseinfo",
              "embedded_application_develop_tests", "embedded_os_basic_test", "embedded_tiny_image_test", "embedded_third_party_packages_test",
              "FS_Device", "FS_Directory", "FS_Negative", "FS_Raw", "FS_iSula"]  # baseOS package name list
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

with open(logCsv, "r", encoding="utf-8") as logFile:
    title = logFile.readline()  # read title
    with open(filteredLogCsv, "w", encoding="utf-8") as outFile, \
            open(filteredLogCsvN, "w", encoding="utf-8") as dropFile:
        outFile.write(title)
        dropFile.write(title)

        suiteName = ""
        while True:
            line = logFile.readline()
            if line == "":
                break
            if line.strip() == "":
                print("Empty line ?")
                continue

            # baseOS
            lineSplit = line.split(splitter, 1)
            if len(lineSplit) < 2:
                print("Wrong splitter ?")
                break

            if lineSplit[0].strip() != "":
                suiteName = lineSplit[0].strip()  # use new pkg name

            if suiteName.lower() in baseOSList:
                outFile.write(line)
                if suiteName not in baseOSTested[suiteName.lower()][1]:
                    baseOSTested[suiteName.lower()][1].append(suiteName)
            elif suiteName.lower() in suite2pkg and suite2pkg[suiteName] in baseOSList:
                outFile.write(line)
                if suiteName not in baseOSTested[suite2pkg[suiteName]][1]:
                    baseOSTested[suite2pkg[suiteName]][1].append(suiteName)
            else:
                dropFile.write(line)

with open(baseOsTestedCsv, "w", encoding="utf-8") as testedFile, \
        open(baseOsUntestedCsv, "w", encoding="utf-8") as untestedFile:
    untestedFile.write("BaseOS-Name\n")
    testedFile.write("BaseOS-Name" + splitter + "Mugen-tests\n")

    for v in baseOSTested.values():
        if len(v[1]) == 0:
            untestedFile.write(v[0] + "\n")
        else:
            testedFile.write(v[0] + splitter + str(v[1])[1:-1].replace("'", "").replace(",", " ") + "\n")
