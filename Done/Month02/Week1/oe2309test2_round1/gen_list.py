import os

failureCause2303 = "/home/hachi/Desktop/Work/PLCT-Working/Done/Month02/Week1/oe2309test2_round1/failureCause_2303.csv"
failureCause2309 = "/home/hachi/Desktop/Work/PLCT-Working/Done/Month02/Week1/oe2309test2_round1/failureCause_2309.csv"
log2309dir = "/home/hachi/Desktop/Work/PLCT-Working/Done/Month02/Week1/oe2309test2_round1/"


if __name__ == "__main__":

    logTree = os.listdir(log2309dir+"/logs")
    logFailTree = os.listdir(log2309dir+"/logs_failed")
    logTree.sort()
    logFailTree.sort()

    if len(logTree) == 0:
        print("Empty log dir")
        exit(0)

    res2303 = {}
    with open(failureCause2303, "r") as f2303:
        f2303.readline()

        pkgName = ""
        while True:
            rec = f2303.readline()
            if rec == "":
                break
            if rec.strip() == "":
                print("Enpty line ?")
                continue

            recl = rec.split(',', 3)
            recl[0] = recl[0].strip()
            if recl[0] != "" and recl[0] != pkgName:
                pkgName = recl[0]
                res2303[pkgName] = {recl[1].strip(): recl[2].strip()}
            else:
                res2303[pkgName][recl[1].strip()] = recl[2].strip()

    with open(failureCause2309, "w") as f2309:
        f2309.write("测试套/软件包名,测试用例名,状态,与2303对比,日志文件,原因\n")

        for suite in logTree:
            cases = os.listdir(log2309dir+"/logs/"+suite)
            cases.sort()
            failedCases = []
            if suite in logFailTree:
                failedCases = os.listdir(log2309dir+"/logs_failed/"+suite)

            for i in range(len(cases)):
                note = "None"
                status = cases[i] not in failedCases
                if suite not in res2303.keys():
                    oldStatus = True
                    note = "2303 未测试该测试套"
                elif cases[i] not in res2303[suite].keys():
                    oldStatus = True
                    note = "2303 未测试该测试用例"
                else:
                    oldStatus = res2303[suite][cases[i]] == "success"
                if status == oldStatus:
                    diff = "same"
                elif status and not oldStatus:
                    diff = "03fail"
                else:
                    diff = "09fail"
                status = "success" if status else "fail"

                logName = ""
                logs = os.listdir(log2309dir+"/logs/"+suite+"/"+cases[i])
                logs.sort()
                for p in range(len(logs)):
                    if ord(logs[-1-p][0]) > ord('9'):
                        continue
                    logName = logs[-1-p]
                    break
                if logName == "":
                    print("Cannot find log for test "+suite+" case "+cases[i])

                if i == 0:
                    f2309.write(suite+","+cases[i]+","+status+","+diff+",./mugen-riscv/logs/"+suite+"/"+cases[i]+"/"+logName+","+note+"\n")
                else:
                    f2309.write(","+cases[i]+","+status+","+diff+",./mugen-riscv/logs/"+suite+"/"+cases[i]+"/"+logName+","+note+"\n")
