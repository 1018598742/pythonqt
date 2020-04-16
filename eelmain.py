from __future__ import print_function  # For Py2/3 compatibility
import eel
import os
import obtainapkinfo

# 定义html文件所在文件夹名称
eel.init('web')


@eel.expose  # 使用装饰器,类似flask里面对路由的定义
def py_obtain_app_info_fun(file):
    isfile = os.path.isfile(file)
    print('是文件吗？'+isfile)
    # print('apk_path=',apk_path)
    # json = obtainapkinfo.obtainApkInfoForJson(apk_path)
    # print('json=',json)
    return "json"


# 启动的函数调用放在最后,port=0表示使用随机端口,size=(宽,高)
eel.start('main.html', port=0, size=(800, 600))
