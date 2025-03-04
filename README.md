# MiBand Heart Rate Monitor | 小米手环心率监控

A simple heart rate monitoring desktop application for Mi Band devices, inspired by Tnze's Rust implementation [MiBand Heart Rate Demo](https://github.com/Tnze/miband-heart-rate) but with Python implementation and a tkinter GUI.

小米手环的简单心率监测桌面应用，参考自[Tnze的Rust实现](https://github.com/Tnze/miband-heart-rate)，采用Python实现并添加图形界面。

## Features | 功能特点

### Core Features | 核心功能
- Bluetooth Scan via **Bleak** 
  通过 **Bleak** 实现蓝牙信息扫描
- heart rate visualization 
  心率可视化
- CSV data logging with timestamps  
  带时间戳的CSV数据记录
- Middle-click drag to move window
  中键拖拽移动窗口

### Requirements | 环境要求
- Bluetooth 4.0+ adapter
- Mi Band 4/5/6/7 device

### Setup | 配置步骤
```bash
# Install dependencies
pip install -r requirements.txt
```

## Usage | 使用说明

### Basic Operation | 基本操作
1. **Connect Device**  
   **连接设备**
   Wear your Mi Band and ensure Bluetooth is enabled  
   佩戴手环并确保蓝牙已开启(建议在手环上启用运动模式)

2. **Start Application**  
   **启动应用**  
   ```bash
   python main.py
   ```

3. **Window Control**  
   **窗口控制**  
   - Middle-click drag to move window  
     中键拖拽移动窗口
   - Heart animation syncs with real-time data  
     心形动画随实时数据同步

4. **Data Logging**  
   **数据记录**  
   - Automatically saves to `heart.csv`(If you are using exe packaged version,it may save in %tmp%\\_MEI****** Folder)
     自动保存至`heart.csv`(如果用打包版本的话，文件可能被创建在名字是 %tmp%\\_MEI***** 的文件夹下)
   - Format: `timestamp, heart_rate`
     格式：`时间戳, 心率值`

### Data Sample | 数据示例
```csv
timestamp,heart_rate
2025-03-04T22:57:56.049355,77
2025-03-04T22:58:10.088993,74
```

## Acknowledgements | 致谢

- **Original Rust Implementation**  
  Tnze's MiBand Heart Rate Demo
  [https://github.com/Tnze/miband-heart-rate](https://github.com/Tnze/miband-heart-rate)

- **Bleak Library**  
  Bluetooth Low Energy platform Agnostic Klient  
  [https://github.com/hbldh/bleak](https://github.com/hbldh/bleak)

## License | 许可证
MIT License © 2025 Mitocdex

##  | 踩坑
~~pybluez is not support new version bluetooth protocol~~
~~## install pybluez on windows~~
~~if you use 'pip install'command you may recive error like : use_2to3 is invalid.<br>~~
~~Install the same version of your Windows Kernel DevelopKit in VS Installer.<br>~~
~~use sourcecode of [pybluez](https://github.com/pybluez/pybluez) project and install it with :~~
```cmd
cd pybluezPath
python setup.py install
```
~~if you recived error: LINK : fatal error LNK1181: cant open io file “Irprops.lib” <br>~~
~~Windows10SDK removed this file in some [reason](https://devblogs.microsoft.com/oldnewthing/20190516-00/?p=102498)~~
~~<br>so you can find your Windows SDK path and make a file link:~~
```cmd
cd C:\pathToYourWDK\Lib\10.0.22621.0\um\x64
mklink IRPROPS.LIB bthprops.lib
```
