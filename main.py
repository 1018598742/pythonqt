import sys
import parseapk
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial
from PyQt5.QtWidgets import *
from PyQt5 import QtCore
import obtainapkinfo
import json
from PyQt5.QtGui import QPixmap


def openFile(ui):
    print("打开文件")
    _translate = QtCore.QCoreApplication.translate
    openfile_path, file_type = QFileDialog.getOpenFileName(None, '选择文件', '','APK Files (*.apk)')
    if openfile_path is not None:
        ui.lineEdit.setText(_translate("Form", openfile_path))
    print('文件路径：', openfile_path)
    print('文件类型：', file_type)


def parseFile(ui):
    filePath = ui.lineEdit.text()
    if filePath != '':
        ui.parse_button.setEnabled(False)
        apk_info = obtainapkinfo.obtainApkInfo(filePath)
        print(apk_info)
        # show_json = json.dumps(apk_info, indent=4)
        # print(show_json)
        if  len(apk_info) > 0:
            show_apk_info = "应用名：%s \n包名：%s " % (apk_info['app_name'], apk_info['package_name'])
            ui.plainTextEdit.setPlainText(show_apk_info)
            app_icon_path = apk_info['app_icon_path']
            icon_path = obtainapkinfo.obtainIcon(filePath, app_icon_path)
            if icon_path != '获取icon失败':
                pixmap = QPixmap(icon_path)
                ui.pic_label.setPixmap(pixmap)
                ui.pic_label.setScaledContents(True)
        else:
            ui.plainTextEdit.setPlainText("解析失败")
        ui.parse_button.setEnabled(True)
    else:
        print('路径是空')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = parseapk.Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.select_button.clicked.connect(partial(openFile, ui))
    ui.parse_button.clicked.connect(partial(parseFile, ui))
    sys.exit(app.exec_())
