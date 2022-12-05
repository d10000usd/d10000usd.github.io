import os, sys, time, re
import shutil
import json
import pandas as pd
from datetime import datetime


class ProjectSettiongs ():
    def __init__(self):
        self.검색어 = '검색어'
    def root(self):
        return os.path.dirname(self.getRealPath())
    def getRealPath(self):
        return os.path.realpath(__file__)
    def prRed(self,skk): print("\033[91m {}\033[00m" .format(skk))
    def prGreen(self,skk): print("\033[92m {}\033[00m" .format(skk))
    def prYellow(self,skk): print("\033[93m {}\033[00m" .format(skk))
    def prLightPurple(self,skk): print("\033[94m {}\033[00m" .format(skk))
    def prPurple(self,skk): print("\033[95m {}\033[00m" .format(skk))
    def prCyan(self,skk): print("\033[96m {}\033[00m" .format(skk))
    def prLightGray(self,skk): print("\033[97m {}\033[00m" .format(skk))
    def prBlack(self,skk): print("\033[98m {}\033[00m" .format(skk))
    def LOGMODULE(self,fname):
        ##LOGMODULE(sys._getframe().f_code.co_name) 함수내부에서 다른함수를 참조하면 사용
        ## print(LOGMODULE(sys._getframe().f_code.co_name)) 외부함수 참조가 없으면 사용
        lenth = len(fname)
        self.prCyan(" - ["+str(fname).ljust(lenth)+"]")
        return "-"

    def timeFunction(self,type_):
        now = datetime.now()
        if type_ == '년월일':
            return datetime.today().strftime("%Y%m%d")
        if type_ == '년월일시분초':
            return now.strftime("%Y%m%d-%H:%M:%S")
        if type_ == '년월일시':
            return now.strftime("%Y%m%d-%H")
        if type_ == '코인타입':
            return now.strftime("%Y-%m-%d %H:%M:%S")
        if type_ == '주식타입':
            return now.strftime("%Y-%m-%d")

class DirectorySettings():
    def __init__(self) -> None:
        pass
    def getFileList(dir):
        return os.listdir(dir)

    #현재 파일 실제 경로
    def root(self):
        return os.path.dirname(self.getRealPath())


    def getRealPath(self):
        return os.path.realpath(__file__)


    def createFolder(self,directory):

        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print ('Error: Creating directory. ' +  directory)

    def deleteFolder(self,directory):
        try:
            if os.path.exists(directory):
                # shutil.rmtree(directory)
                os.rmdir(directory)
        except OSError:
            print ('Error: Deleting directory. ' +  directory)

    def deleteFolderAll(self,directory):
        try:
            if os.path.exists(directory):
                shutil.rmtree(directory)
        except OSError:
            print ('Error: Deleting directory. ' +  directory)
    # createFolder('/Users/aaron/Desktop/test')

    def Dev_Folder_setting(self):
        self.createFolder(self.root() + '/src/data') #output 폴더 생성
        self.createFolder(self.root() + '/src/data') #output 폴더 생성
        self.createFolder(self.root() + '/src/data/csv') #output 폴더 생성
        self.createFolder(self.root() + '/src/data/json') #output 폴더 생성
        self.createFolder(self.root() + '/src/data/image') #output 폴더 생성
        self.createFolder(self.root() + '/src/data/temp') #output 폴더 생성

        self.createFolder(self.root() + '/src/') #output 폴더 생성
        # createFolder(root() + '/public/')
        # createFolder(root() + '/util/')
        self.createFolder(self.root() + '/temp/')



    def Dev_Folder_delete(self):
        #deleteFolder(getRealDir() + 'src/data') #output 폴더 생성
        self.deleteFolder(self.root() + 'src/data/cvs') #output 폴더 생성
        self.deleteFolder(self.root() + 'src/data/json') #output 폴더 생성
        self.deleteFolder(self.root() + 'src/data/image') #output 폴더 생성
        self.deleteFolder(self.root() + 'src/data/tmp') #output 폴더 생성

    def Dev_Folder_deleteAll(self):
        self.deleteFolderAll(self.root() + 'src/data') #하위 폴더까지 모두 삭제




class SaveControl():
    def __init__(self) -> None:
        pass
    def saveFile(self,fileName, data):
        f = open(fileName, 'w')
        f.write(data)
        f.close()

    def saveFileAppend(self,fileName, data):
        f = open(fileName, 'a')
        f.write(data)
        f.close()

    def saveFileAppendLine(self,fileName, data):
        f = open(fileName, 'a')
        f.write(data + '  ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) )
        f.close()



    def prefairingJson(self,df):
        ##allowed values are: {} records, index, columns, values, table}. Default: split.
        json_1=df.to_json(date_format='iso',orient='records',force_ascii=True,indent=4)
        parsed = json.loads(json_1)

        return parsed
    def dataframeToJsonfile(self,df,savepath,fname): #특수문자가 깨져서 따로 만들어줌
        path = f"{savepath}/{fname}.json"
        path = path.replace(" ","_")

        json_1=df.to_json(date_format='iso',orient='records',force_ascii=True,indent=4)
        parsed = json.loads(json_1)

        with open(path, 'w') as json_file:
            json_file.write(json.dumps(parsed, indent=4, ensure_ascii=False,))
            # json_file.write(json.dumps({"fulldata": parsed}, indent=4, ensure_ascii=False,))

    def dictTodataframeToJsonfile(self,dictionaryd,savepath,fname): #특수문자가 깨져서 따로 만들어줌
        path = f"{savepath}/{fname}.json"

        df = pd.DataFrame([dictionaryd])
        json_1=df.to_json(date_format='iso',orient='records',force_ascii=True,indent=4)
        parsed = json.loads(json_1)

        with open(path, 'w') as json_file:
            json_file.write(json.dumps(parsed, indent=4, ensure_ascii=False,))
            # json_file.write(json.dumps({"fulldata": parsed}, indent=4, ensure_ascii=False,))
    def dictionaryToDataframe(self,adddicdata):
        dictdata = adddicdata
        df = pd.DataFrame([dictdata])
        # df.loc[len(df)] = dictdata # dataframe에 dictdata 를 행추가, 행으로 추가
        return df
    def listToJsonfile(self,datalist,savepath,fname):
        df = pd.DataFrame(datalist)
        path = f"{savepath}/{fname}.json"
        json_1=df.to_json(date_format='iso',orient='records',force_ascii=True,indent=4)
        parsed = json.loads(json_1)

        with open(path, 'w') as json_file:
            json_file.write(json.dumps(parsed, indent=4, ensure_ascii=False,))
            # json_file.write(json.dumps({"fulldata": parsed}, indent=4, ensure_ascii=False,))


    def dataframeToJsonfile_md(self,df,savepath,fname): #특수문자가 깨져서 따로 만들어줌

        savepath=savepath.replace(' ','_')
        fname= fname.replace(' ','_')
        path = f"{savepath}/{fname}.md"
        json_1=df.to_json(date_format='iso',orient='records',force_ascii=True,indent=2)
        parsed = json.loads(json_1)
        with open(path, 'w') as json_file:
            json_file.write(json.dumps(parsed, indent=2, ensure_ascii=False,))
            # json_file.write(json.dumps({"fulldata": parsed}, indent=4, ensure_ascii=False,))

    def jsonfileread(self,filepath):
        with open(filepath, 'r') as f:
            json_data = json.load(f)
        return json_data

    def copySheelfile(self,filepath,savepath):
        filepath= "/Users/hg/DEVELOP/app/naverblog_async_newspapper.sh"
        # savepath= "/Users/hg/DEVELOP/app/naverblog_async_newspapper_copy.sh"

        shutil.copy(filepath, savepath)