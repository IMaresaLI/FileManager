################################################
################################################
################################################
#########*******###*******####**********########
########**#####**#**#####**###**######**########
########**#####**#**#####**###**######**########
########**#####**#**#####**###**********########
########**#####**#**#####**###**################
########**#####**#**#####**###**################
########**######***######**###**################
########**###############**###**################
########**###############**###**################
################################################
########Copyright © Maresal Programming#########
################################################

from PyQt5 import QtWidgets,QtCore,QtGui
import os,sys,re,psutil,time,datetime,GPUtil
from fileManagerDesigner import Ui_MainWindow

class discordApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(discordApp,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet(open("style.css","r").read())
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.firstPage()

        self.ui.exitBtn.clicked.connect(self.close)
        self.ui.minimizeBtn.clicked.connect(self.minimize)
        self.ui.fullScreenBtn.clicked.connect(self.fullscreen)
        self.ui.treeView.doubleClicked.connect(self.fileNameUpdated)
        self.ui.createFile.clicked.connect(self.fileCreated)
        self.ui.deleteFile.clicked.connect(self.deleteFile)
        self.ui.HomeBtn.pressed.connect(self.PageClicked)
        self.ui.fileManagerBtn.pressed.connect(self.PageClicked)
        self.ui.AdvancedSearchBtn.pressed.connect(self.PageClicked)
        self.ui.searchBtn.clicked.connect(self.startSearchFile)
        self.ui.FileListWidget.currentItemChanged.connect(self.fileDescription)

        zamanlayıcı = QtCore.QTimer(self)
        zamanlayıcı.timeout.connect(self.sysStatus)
        zamanlayıcı.start(1000)   


    def fileNames(self):
        index = self.model.index(self.ui.treeView.currentIndex().row(),0,self.ui.treeView.currentIndex().parent())
        fileName = self.model.fileName(index)
        filePath = self.model.filePath(index)
        pathName = fileName+"@"+ filePath
        return pathName

    def fileNameUpdated(self):
        try:
            file = self.fileNames().split("@")
            newName,ok = QtWidgets.QInputDialog.getText(self,"Isim Değiştirme",f"Değiştirelecek dosya : {file[0]}\n")
            if newName and ok:
                if os.path.isfile(file[1]) == True:
                    filepath = file[1].split(file[0])[0]
                    uzantı = file[0].split(".")
                    print(uzantı)
                    os.chdir(filepath)
                    os.rename(file[0],newName+"."+uzantı[1])
                else:
                    filepath = file[1].split(file[0])[0]
                    os.chdir(filepath)
                    os.rename(file[0],newName)
        except :
            pass

    def fileCreated(self):
        try:
            file = self.fileNames().split("@")
            if os.path.isfile(file[1]) == False:
                newName,ok = QtWidgets.QInputDialog.getText(self,"Dosya veya Dizin Oluşturma",f"Isim belirtiniz : ")
                if newName and ok:
                    if newName.find('.') == -1:
                        os.chdir(file[1])
                        os.mkdir(newName)
                    else :
                        os.chdir(file[1])
                        open(newName,"a")
        except :
            pass

    def deleteFile(self):
        try:
            file = self.fileNames().split("@")
            filepath = file[1].split(file[0])[0]
            os.chdir(filepath)
            if os.path.isfile(file[1]) == False :
                onay = QtWidgets.QMessageBox.question(self,"Silme İşlemi",f"{file[0]} isimli klasör silinecek onaylıyor musunuz?",QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
                if onay == QtWidgets.QMessageBox.Ok:
                    os.rmdir(file[0])   
            else :
                onay = QtWidgets.QMessageBox.question(self,"Silme İşlemi",f"{file[0]} isimli dosya silinecek onaylıyor musunuz?",QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
                if onay == QtWidgets.QMessageBox.Ok:
                    os.remove(file[0])    
        except :
            pass           

    def startSearchFile(self):
        global list
        list = []
        list.append(self.ui.searchtbx.text())
        self.evt_btn_clicked()

    def fileDescription(self):
        try: 
            url = self.ui.FileListWidget.currentItem()
            information = os.stat(url.text())
            createDate = datetime.datetime.fromtimestamp(information.st_ctime)
            lastAccess = datetime.datetime.fromtimestamp(information.st_atime)
            lastReplace = datetime.datetime.fromtimestamp(information.st_mtime)
            fileSize = (information.st_size/1024) / 1024

            self.ui.FileDescription.setText(
                f"Dosya path : {url.text()}\n"
                f"Oluşturulma Tarihi : {createDate}\n"
                f"Son Erişim Tarihi : {lastAccess}\n"
                f"Son Değişim Tarihi : {lastReplace}\n"
                f"Dosya Boyutu : {round(fileSize,2)} MB\n")
        except Exception as err :
            print(err)


    def evt_btn_clicked(self):
        self.worker = WorkerThread()
        self.worker.start()
        self.worker.finished.connect(self.evt_worker_finished)
        self.worker.update_val.connect(self.textUpdate)
        self.ui.searchBtn.setEnabled(False)
        self.ui.searchtbx.setEnabled(False)

    def evt_worker_finished(self):
        QtWidgets.QMessageBox.information(self,"Dosya Tarama","Tarama sonlandı.<br>Tüm dosyalar listeye eklendi.")
        self.ui.searchBtn.setEnabled(True)
        self.ui.searchtbx.setEnabled(True)

    def textUpdate(self,update_val):
        self.ui.FileListWidget.addItem(update_val)
        self.ui.fileCountTbx.setText(str(self.ui.FileListWidget.count()))


# AnaMenu Setting

    def firstPage(self):
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath("")
        self.ui.treeView.setModel(self.model)
        self.ui.treeView.setAnimated(False)
        self.ui.treeView.setIndentation(50)
        self.ui.treeView.setSortingEnabled(True)
        self.ui.treeView.setAllColumnsShowFocus(True)
        self.ui.treeView.setColumnWidth(0,250)
        
    def PageClicked(self):
        if self.ui.HomeBtn.isDown() == True:
            self.ui.stackedWidget.setCurrentIndex(0)
        if self.ui.fileManagerBtn.isDown() == True:
            self.ui.stackedWidget.setCurrentIndex(1)
        if self.ui.AdvancedSearchBtn.isDown() == True:
            self.ui.stackedWidget.setCurrentIndex(2)

    def mousePressEvent(self, event):

        if event.buttons() == QtCore.Qt.LeftButton:
            self.dragPos = event.globalPos()
            event.accept()

    def mouseMoveEvent(self, event):

        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
        else :
            self.showFullScreen()

    def minimize(self):
        main.showMinimized()
        
    def close(self):
        app.exit()

    def sysStatus(self):
        cpuStatus = psutil.cpu_percent()
        self.ui.cpuPercent.setValue(int(cpuStatus))
        ramStatus = psutil.virtual_memory().percent
        self.ui.ramPercent.setValue(int(ramStatus))
        gpuStatus = GPUtil.getGPUs()
        for i in gpuStatus:
            self.ui.gpuPercent.setValue(int(i.load*100))




class WorkerThread(QtCore.QThread):
    update_val = QtCore.pyqtSignal(str)
    def run(self):
        psutil.disk_partitions()
        for i in range(1):
            n=0
            for i in range(len(psutil.disk_partitions())):
                dir_path = os.path.dirname(os.path.realpath(psutil.disk_partitions()[n].device))
                for root,dirs,files in os.walk(dir_path): 
                    for file in files:
                        if file.endswith(list[0]): 
                            text =root+'/'+str(file)
                            self.update_val.emit(text)
                n+=1
                time.sleep(1)





if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    main = discordApp()
    main.show()
    app.exit(app.exec_())

