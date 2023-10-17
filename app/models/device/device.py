import os
import shlex
import subprocess

from typing import Optional

from sqlalchemy import Column, Integer, BigInteger, String, or_

from app import db
from app.libs.enums import DeviceStatus, DeviceRemote
from app.models import Base
from app.view_model.device.device import DeviceMessage
message = DeviceMessage()


class Device(Base):
    __tablename__ = 'device'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sn = Column(String(50), nullable=False)
    type = Column(String(50), nullable=False)
    storage = Column(String(50), nullable=False)
    owner = Column(String(50), nullable=False)
    description = Column(String(255), nullable=False)
    stage = Column(String(50), nullable=False)
    ip = Column(String(50), nullable=True)
    address = Column(String(100), nullable=True)
    _use = Column('use', Integer, nullable=False, default=1)
    _remote = Column('remote', Integer, nullable=False, default=0)

    @property
    def use(self):
        return self._use

    @use.setter
    def use(self):
        return DeviceStatus.value

    @property
    def remote(self):
        return self._remote

    @remote.setter
    def remote(self):
        return DeviceRemote.value

    @staticmethod
    def search_device(condition: dict = {}):
        if not condition.pop('status'):
            condition['use'] = ''
        if condition.get('owner') == '全部':
            condition['owner'] = ''
        content = bool()
        for key, value in condition.items():
            if value:
                content = True
        if condition.get('sn'):
            return Device.query.filter(Device.sn == condition.get('sn')).all()
        if content:
            return (Device.query.filter(
                                      or_((Device.type.in_(condition.get('type'))), condition.get('type') == []),
                                      or_(Device.storage.in_(condition.get('storage')), condition.get('storage') == []),
                                      or_(Device.stage.in_(condition.get('stage')), condition.get('stage') == []),
                                      or_(Device.owner == condition.get('owner'), condition.get('owner') == ''),
                                      ).all())
        else:
            return Device.query.all()

    @staticmethod
    def update_device(condition: {}):
        if condition.get('status'):
            condition['use'] = ''
        up_content = {}
        for key, value in condition.items():
            if value or key == 'description':
                up_content.update({key: value})
        try:
            Device.query.filter(Device.sn == condition.get('sn')).update(up_content)
            db.session.commit()
            message.success()
        except Exception as e:
            message.fail(str(e))
        return message.message

    @staticmethod
    def delete_device(condition: {}):
        try:
            Device.query.filter(Device.sn == condition.get('sn')).delete()
            db.session.commit()
            message.success()
        except Exception as e:
            print(str(e))
            message.fail(str(e))
        return message.message

    @staticmethod
    def yun_connect(condition: {}):
        print(condition)
        cmd = '/home/apps/android-sdk/platform-tools/adb connect  %s:5555' % condition.get('ip')
        try:
            Device.query.filter(Device.sn == condition.get('sn')).update(condition)
            db.session.commit()
            status = os.popen(cmd).read()
            if 'connected' in status:
                Device.update_device(condition.update({'_remote': '1'}))
                message.success()
            else:
                message.fail(data='连接失败')
        except Exception as e:
            print(e)
            message.fail(e)
        return message.message

    @staticmethod
    def yun_remove(condition: {}):
        try:
            Device.query.filter(Device.sn == condition.get('sn')).update({'_remote': '0', 'ip': ''})
            db.session.commit()
            message.success()
        except Exception as e:
            print(e)
            message.fail(e)
        return message.message

    @staticmethod
    def yun_install(condition: {}):
        from app.manage import app
        print(condition)
        if condition.get('remote') == "1":
            cmd = '/home/apps/android-sdk/platform-tools/adb -s %s:5555 install %s' % (condition.get('ip'), app.config['REMOTE_ADDR'])
            status = os.system(cmd)
            if status == 0:
                message.success()
            else:
                message.fail('安装失败')
        elif condition.get('remote') == "2":
            cmd = '/home/apps/android-sdk/platform-tools/adb -s %s install %s' % (condition.get('sn'), app.config['REMOTE_ADDR'])
            status = os.system(cmd)
            if status == 0:
                message.success()
            else:
                message.fail('安装失败')
        return message.message

    @staticmethod
    def yun_log(condition: {}):
        cmd = ''
        if condition.get('remote') == "1":
            cmd = 'rm -rf /var/www/html/device/log/ && rm -rf /var/www/html/device/log.zip  && adb -s  %s:5555 pull  /sdcard/zlog   /var/www/html/device/log/' % condition.get('ip')
        elif condition.get('remote') == "2":
            cmd = 'rm -rf /var/www/html/device/log/ && rm -rf /var/www/html/device/log.zip &&  adb -s  %s pull  /sdcard/zlog   /var/www/html/device/log/' % condition.get('sn')
        status = os.system(cmd)
        if status == 0:
            cmd = 'cd /var/www/html/device && zip -r log.zip log/'
            status = os.system(cmd)
            if status == 0:
                message.success()
            else:
                message.fail('导出失败')
        else:
            message.fail('导出失败')
        return message.message

    @staticmethod
    def yun_list(remote_addr: str = '10.254.12.55'):
        cmd = shlex.split('adb devices -l')
        yun_list = []
        usb_list = []
        wifi_list = []
        if subprocess.call(cmd) == 0:
            if subprocess.check_output(cmd).decode('UTF-8').strip() == 'List of devices attached':
                message.fail(data='没有找到设备')
                return message.message
            for i in subprocess.check_output(cmd).decode('UTF-8').splitlines()[1:-1]:
                if 'usb' in i:
                    device_append(usb_list, i)
                    yun_list.extend(usb_list)
                else:
                    device_append(wifi_list, i)
            for wifi in wifi_list:
                for usb in usb_list:
                    if wifi['uid'] == usb['uid']:
                        pass
                    else:
                        yun_list.append(wifi)
        yun = {'cloud': yun_list}
        # usb = {'usb': usb_list}
        # wifi = {'wifi': wifi_list}
        # message.success(data='获取设备成功', device=yun)
        # print()
        message.success(data='获取设备成功', device_list=yun)
        return message.message



def device_append(yun_list, device):
    dic = {}
    dic.update({'device': device.split(' ')[0],
                'model': device.split(' ')[-3],
                'uid': device.split(' ')[-2]})
    yun_list.append(dic)


def add_device(condition: {}):
    print(condition)
    device = Device()
    device.sn = condition.get('sn')
    device.owner = condition.get('owner')
    device.stage = condition.get('stage')
    device.storage = condition.get('storage')
    device.type = condition.get('type')
    device.description = condition.get('description')

    try:
        db.session.add(device)
        db.session.commit()
        message.success()
    except Exception as e:
        message.fail(str(e))
    return message.message






if __name__ == '__main__':
    # add_device()
    Device().yun_list()







