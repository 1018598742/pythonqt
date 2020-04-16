import subprocess
import re
import zipfile
import demjson
import os


def obtainApkInfo(apk_path):
    p = subprocess.Popen('aapt2 dump badging ' + apk_path, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    outputDecode = output.decode()
    # print(outputDecode)

    spilt = outputDecode.split("\n")
    d = {}
    list = []
    for item in spilt:
        # print("截取字段=", item)
        if item.startswith('package'):
            packageNameRegex = "package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'"
            groups = re.compile(packageNameRegex).match(item)
            if not groups:
                raise Exception("can't get packageinfo")
            package_name = groups.group(1)
            version_code = groups.group(2)
            version_name = groups.group(3)
            # print('包名：', package_name)
            # print('版本号：', version_code)
            # print('版本名：', version_name)
            d["package_name"] = package_name
            d["version_code"] = int(version_code)
            d["version_name"] = version_name
        if item.startswith('launchable-activity'):
            match = re.compile("launchable-activity: name='(\S+)'").search(item)
            if match is not None:
                launcher_activity = match.group(1)
                # print("启动activity：", launcher_activity)
                d["launcher_activity"] = launcher_activity
        if item.startswith('sdkVersion'):
            match = re.compile("sdkVersion:'(\S+)'").search(item)
            if match is not None:
                sdk_version = match.group(1)
                # print("sdkVersion：", sdk_version)
                d["sdk_version"] = int(sdk_version)
        if item.startswith('targetSdkVersion'):
            match = re.compile("targetSdkVersion:'(\S+)'").search(item)
            if match is not None:
                target_version = match.group(1)
                # print("targetVersion：", target_version)
                d["target_version"] = int(target_version)
        if item.startswith('uses-permission'):
            match = re.compile("uses-permission: name='(\S+)'").match(item)
            if match is not None:
                uses_permission = match.group(1)
                # print("用户权限：", uses_permission)
                list.append(uses_permission)
        if item.startswith('application-label:'):
            match = re.compile("application-label:'(.*)'").match(item)
            if match is not None:
                app_name = match.group(1)
                # print("应用名：", app_name)
                d["app_name"] = app_name
        if item.startswith('application-label-zh:'):
            match = re.compile("application-label-zh:'(\S+)'").match(item)
            if match is not None:
                app_name_zh = match.group(1)
                # print("应用名(中文)：", app_name_zh)
                d["app_name"] = app_name_zh
        if item.startswith('application:'):
            match = re.compile("icon='(\S+)'").search(item)
            if match is not None:
                app_icon = match.group(1)
                # print("应用图标位置：", app_icon)
                d["app_icon_path"] = app_icon
    if len(list) > 0:
        d["uses_permissions"] = list
    return d


def obtainIcon(apk_path, app_icon_path, dir_path=os.path.dirname(os.path.abspath(__file__))):
    try:
        apk_path_group = apk_path.split('/')
        save_icon_name = apk_path_group[len(apk_path_group) - 1].split('.')[0] + '.png'
        if not app_icon_path.endswith('.png'):
            groups = app_icon_path.split('/')
            app_icon_name = groups[len(groups) - 1]
            app_icon_name = app_icon_name.split('.')[0] + '.png'
            app_icon_path = 'res/drawable/' + app_icon_name
        zip = zipfile.ZipFile(apk_path)
        iconData = zip.read(app_icon_path)
        save_icon_path = os.path.join(dir_path, save_icon_name)
        with open(save_icon_path, 'w+b') as saveIconFile:
            saveIconFile.write(iconData)
        return save_icon_path
    except Exception:
        return "获取icon失败"

def obtainApkInfoForJson(apk_path):
    info = obtainApkInfo(apk_path)
    json = demjson.encode(info)
    return json

if __name__ == '__main__':
    # subprocess.check_call('aapt2 dump badging wifi.apk', shell=True)
    # apk_name = 'wifi.apk'
    apk_name = 'alipay_wap_main.apk'
    info = obtainApkInfo(apk_name)
    print(info)
    json = demjson.encode(info)
    print(json)
    app_icon_path = info['app_icon_path']
    saveIconPath = obtainIcon(apk_name, app_icon_path)
    print('saveIconPath', saveIconPath)
