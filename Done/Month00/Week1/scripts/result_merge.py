import os
import json
import csv

class TestResults(object):
    def __init__(self,workingDir):
        self.workingDir = workingDir
        self.logsDir = workingDir + '/logs'
        self.failedLogsDir = workingDir + '/logs_failed'
        self.suite2casesDir = 'suite2cases'
        self.testResult = []
        self.totalCaseNum, self.totalPassedCaseNum, self.totalFailedCaseNum = 0, 0, 0
        self.logClassifier = classifier("catalog.json")

    def parseResults(self):
        self.testedSuites = os.listdir(self.logsDir)
        failedSuites = os.listdir(self.failedLogsDir)
        for suite in self.testedSuites:
            testedCases = os.listdir(self.logsDir+'/'+suite)
            allFailedCases = []
            failedCaseNum = 0
            if suite in failedSuites:
                allFailedCases = os.listdir(self.failedLogsDir+'/'+suite)

            suite2casesJsonFile = open(self.suite2casesDir+'/'+suite+'.json','r')
            suite2casesRaw = suite2casesJsonFile.read()
            suite2casesJsonFile.close()
            suite2casesData = json.loads(suite2casesRaw)

            passedCases = []
            failedCases = []
            for testedCase in testedCases:
                addDisk, multiMachine, addNic = 0, 0, 0
                for casedat in suite2casesData['cases']:
                    if not(casedat['name'] == testedCase):
                        continue
                    if casedat.__contains__('add disk'):
                        addDisk = 1
                    if casedat.__contains__('machine num'):
                        multiMachine = 1
                    if casedat.__contains__('add network interface'):
                        addNic = 1
                logname = os.listdir(self.logsDir+'/'+suite+'/'+testedCase)
                if type(logname) == list:
                    logname.sort()
                    logname = logname[-1]
                if (suite in failedSuites) and (testedCase in allFailedCases):
                    failedCases.append({'name':testedCase,'logname':logname,'cause':[],'trim':0,'addDisk':addDisk,'multiMachine':multiMachine,'addNic':addNic})
                    failedCaseNum = failedCaseNum + 1
                else:
                    passedCases.append({'name':testedCase,'logname':logname,'trim':0,'addDisk':addDisk,'multiMachine':multiMachine,'addNic':addNic})
            
            caseNum = len(testedCases)
            passedCaseNum = caseNum - failedCaseNum
            self.testResult.append({'name':suite,'caseNum':caseNum,'passedCaseNum':passedCaseNum,'failedCaseNum':failedCaseNum,'passedCases':passedCases,'failedCases':failedCases})
        
    def writeJson(self):
        if self.testResult is None:
            return
        jsonfile = open(self.workingDir+'/'+'results.json','w')
        jsonfile.write(json.dumps(self.testResult,indent=4))
        jsonfile.close()


    def exportResults(self):
        self.totalCaseNum, self.totalPassedCaseNum, self.totalFailedCaseNum = 0, 0, 0
        for suite in self.testResult:
            self.totalCaseNum = self.totalCaseNum + suite['caseNum']
            self.totalFailedCaseNum = self.totalFailedCaseNum + suite['failedCaseNum']
            self.totalPassedCaseNum = self.totalPassedCaseNum + suite['passedCaseNum']
        #csvfile = open(self.workingDir+'/'+'result.csv','w')
        #cw = csv.writer(csvfile,lineterminator = '\n')
        #title = ['测试套/软件包名','测试用例总数','通过','未通过','备注','总测试套数','总测试用例数','总通过用例数','总未通过用例数']
        if len(self.testResult) == 0:
            return
        #row1 = [self.testResult[0]['name'],self.testResult[0]['caseNum'],self.testResult[0]['passedCaseNum'],self.testResult[0]['failedCaseNum'],'',len(self.testResult),self.totalCaseNum,self.totalPassedCaseNum,self.totalFailedCaseNum]
        #row = []
        #row.append(title)
        #row.append(row1)
        #for i in range(len(self.testResult) - 1):
        #    row.append([self.testResult[i+1]['name'],self.testResult[i+1]['caseNum'],self.testResult[i+1]['passedCaseNum'],self.testResult[i+1]['failedCaseNum']])
        #cw.writerows(row)
        

    def parseUnsupportedCase(self,addDisk = False,multiMachine = False,addNic = False):
        for i in range(len(self.testResult)):
            for j in range(self.testResult[i]['passedCaseNum']):
                if (not addDisk) and (self.testResult[i]['passedCases'][j]['addDisk']):
                    self.testResult[i]['passedCases'][j]['trim'] = 1
                if (not multiMachine) and (self.testResult[i]['passedCases'][j]['multiMachine']):
                    self.testResult[i]['passedCases'][j]['trim'] = 1
                if (not addNic) and (self.testResult[i]['passedCases'][j]['addNic']):
                    self.testResult[i]['passedCases'][j]['trim'] = 1
            
            for j in range(self.testResult[i]['failedCaseNum']):
                if (not addDisk) and (self.testResult[i]['failedCases'][j]['addDisk']):
                    self.testResult[i]['failedCases'][j]['trim'] = 1
                if (not multiMachine) and (self.testResult[i]['failedCases'][j]['multiMachine']):
                    self.testResult[i]['failedCases'][j]['trim'] = 1
                if (not addNic) and (self.testResult[i]['failedCases'][j]['addNic']):
                    self.testResult[i]['failedCases'][j]['trim'] = 1

    def analyzeCause(self):
        pass

    def trimResults(self):
        pass

    def classifyResults(self):
        for i in range(len(self.testResult)):
            for j in range(len(self.testResult[i]['failedCases'])):
                logPath = self.workingDir+'/logs_failed/'+self.testResult[i]['name']+'/'+self.testResult[i]['failedCases'][j]['name']+'/'+self.testResult[i]['failedCases'][j]['logname']
                logfile = open(logPath,'r',encoding="ISO-8859-1")
                logdata = logfile.read().split('\n')
                logfile.close()
                self.testResult[i]['failedCases'][j]['cause'] = self.logClassifier.checkErrorType(logdata)

    def exportFailureCause(self):
        csvfile = open(self.workingDir+'/'+'failureCause.csv','w')
        cw = csv.writer(csvfile,lineterminator = '\n')
        #title = ['测试套/软件包名','测试用例名','日志文件','原因']
        errorTypes = []
        for errortype in self.logClassifier.errorType:
            errorTypes.append(errortype['name'])
            title.append(errortype['name'])
        if len(self.testResult) == 0:
            return
        row = []
        row.append(title)

        #mergeCsv = open(self.workingDir+'/'+'mergeCause.csv','w')
        #mergeCw = csv.writer(mergeCsv,lineterminator = '\n')
        #mergeTitle = ['测试套/软件包名','测试用例名','状态','日志文件','原因']
        #mergeRow = []
        #mergeRow.append(mergeTitle)

        for i in range(len(self.testResult)):
            #for j in range(len(self.testResult[i]['passedCases'])):
            #    content = [self.testResult[i]['name'],self.testResult[i]['passedCases'][j]['name'],'success',self.testResult[i]['passedCases'][j]['logname'],'']
            #    mergeRow.append(content)

            for j in range(len(self.testResult[i]['failedCases'])):
                causestr = ""
                for cause in self.testResult[i]['failedCases'][j]['cause']:
                    causestr = causestr + cause + '\n'
                content = [self.testResult[i]['name'],self.testResult[i]['failedCases'][j]['name'],self.testResult[i]['failedCases'][j]['logname'],causestr]
                for errortype in errorTypes:
                    if errortype in self.testResult[i]['failedCases'][j]['cause']:
                        content.append(1)
                    else:
                        content.append(0)
                row.append(content)

                #content = [self.testResult[i]['name'],self.testResult[i]['failedCases'][j]['name'],'fail',self.testResult[i]['failedCases'][j]['logname'],causestr]
                #mergeRow.append(content)
        cw.writerows(row)
        #mergeCw.writerows(mergeRow)



class classifier(object):
    def __init__(self,configFileName):
        self.errorType = []
        configFile = open(configFileName,'r')
        configraw = configFile.read()
        configFile.close()
        config = json.loads(configraw)
        self.errorType = config['catalog']

    def checkErrorType(self,logData):
        ErrorType = []
        for error in self.errorType:
            if self.checkSections(logData,error['pattern']):
                ErrorType.append(error['name'])
        return ErrorType

    def checkKeys(self,sections,pattern):
        value = False
        for section in sections:
            for orpattern in pattern:
                andvalue = True
                for andpattern in orpattern:
                    andvalue = andvalue & ~(andpattern['type'] ^ (section.find(andpattern['key']) != -1))
                value = value | andvalue
        return value

    def checkSections(self,sections,pattern):
        value = False
        for orpattern in pattern:
            andvalue = True
            for andpattern in orpattern:
                andvalue = andvalue & ~(andpattern['type'] ^ (self.checkKeys(sections,andpattern['section'])))
            value = value | andvalue
        return value

def convertfile(dir):
    suites = os.listdir(dir)
    for suite in suites:
        testcases = os.listdir(dir+'/'+suite)
        for testcase in testcases:
            logs = os.listdir(dir+'/'+suite+'/'+testcase)
            for log in logs:
                if log.find(':') == -1:
                    continue
                newlog = log.replace(':','_')
                oldpath = dir+'/'+suite+'/'+testcase+'/'+log
                newpath = dir+'/'+suite+'/'+testcase+'/'+newlog
                os.system('cp '+oldpath+' '+newpath)
                os.system('rm -f '+oldpath)

def mergeCause(dir,pre,pre86,rv, x86):

    csvfile = open(dir+'/'+'mergeCause.csv','w')
    cw = csv.writer(csvfile,lineterminator = '\n')
    title = ['测试套/软件包名','测试用例名','状态','日志文件','原因','x86 日志文件','x86 原因']
    row = []
    row.append(title)

    # x86 result to map
    result86 = {}
    for i in range(len(x86.testResult)):
        cases = {}
        for j in range(len(x86.testResult[i]['failedCases'])):
            cases[x86.testResult[i]['failedCases'][j]['name']] = False
            cases[x86.testResult[i]['failedCases'][j]['name']+"_log"] = x86.testResult[i]['failedCases'][j]['logname']
            cases[x86.testResult[i]['failedCases'][j]['name']+"_cause"] = x86.testResult[i]['failedCases'][j]['cause']
        for j in range(len(x86.testResult[i]['passedCases'])):
            cases[x86.testResult[i]['passedCases'][j]['name']] = True
        result86[x86.testResult[i]['name']] = cases

    for i in range(len(rv.testResult)):
        case86 = result86.get(rv.testResult[i]['name'])

        for j in range(len(rv.testResult[i]['passedCases'])):
            logPath = pre+'/logs/'+rv.testResult[i]['name']+'/'+rv.testResult[i]['passedCases'][j]['name']+'/'+rv.testResult[i]['passedCases'][j]['logname']
            content = [rv.testResult[i]['name'],rv.testResult[i]['passedCases'][j]['name'],'success',logPath,'','','']
            row.append(content)

        for j in range(len(rv.testResult[i]['failedCases'])):
            causestr = ""
            for cause in rv.testResult[i]['failedCases'][j]['cause']:
                causestr = causestr + cause + '\n'
            if causestr == "":
                causestr = "unknown"

            logPath = pre+'/logs_failed/'+rv.testResult[i]['name']+'/'+rv.testResult[i]['failedCases'][j]['name']+'/'+rv.testResult[i]['failedCases'][j]['logname']
            logPath86 = pre86+'/logs_failed/'+rv.testResult[i]['name']+'/'+rv.testResult[i]['failedCases'][j]['name']+'/'
            content = [rv.testResult[i]['name'],rv.testResult[i]['failedCases'][j]['name'],'fail',logPath,causestr,'','']

            if case86 is None:
                print(rv.testResult[i]['name'] + " not test on x86 ?")
            else:
                ret86 = case86.get(rv.testResult[i]['failedCases'][j]['name'])
                log86 = case86.get(rv.testResult[i]['failedCases'][j]['name']+"_log")
                cause86 = case86.get(rv.testResult[i]['failedCases'][j]['name']+"_cause")
                if ret86 is None:
                    print(rv.testResult[i]['failedCases'][j]['name'] + "not test on x86 ?")
                else:
                    if not ret86:
                        causestr = ""
                        for cause in cause86:
                            causestr = causestr + cause + '\n'
                        if causestr == "":
                            causestr = "unknown"

                        content[2] = 'x86 fail'
                        content[5] = logPath86+log86
                        content[6] = causestr

            row.append(content)

    cw.writerows(row)


workingDir="/home/hachi/Desktop/Work/PLCT-Working/Done/Week1/cli0/riscv/"
workingDir86="/home/hachi/Desktop/Work/PLCT-Working/Done/Week1/cli0/x86/"

outputDir=workingDir+"/../"
pathPre="./riscv"
pathPre86="./x86"

if __name__ == "__main__":
    #convertfile(workingDir+'/logs')
    #convertfile(workingDir+'/logs_failed')
    result = TestResults(workingDir)
    result.parseResults()
    result.parseUnsupportedCase(addDisk=True)
    result.classifyResults()
    #result.writeJson()
    result.exportResults()
    #result.exportFailureCause()


    result86 = TestResults(workingDir86)
    result86.parseResults()
    result86.parseUnsupportedCase(addDisk=True)
    result86.classifyResults()
    result.exportResults()


    mergeCause(outputDir, pathPre, pathPre86, result, result86)

