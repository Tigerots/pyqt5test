本项目是用pyqt5+pyserial写的一款串口调试软件
 =
1.具备时间显示，定时发送，hex发送，发送编码转变等功能，还有自动保存数据和手动保存功能<br>
2.绝不卡死，发送和接收都是两个线程处理，实现完全的UI与数据处理分离<br>
3.pyqt5test文件夹里是源码和qt写的ui文件，可以单独提取出来<br>
   * pyqt_main.py 是主程序，负责把其他页面的参数进行实例化调用
   * pyqt_mainwindow_window.py主程序窗口事件，负责处理所有信号响应事件
   * moudle_pysierial.py我自己整合的串口模块，里面有一些串口的处理
   * serial_conf_window.py串口额外的设置，我做成了一个页面这是调度那个设置页面的响应事件
   * auto_save_window.py自己做来玩的自动保存功能
   * automation_test_window.py同样是做来的测试功能
   * ui为后缀名的皆为qtdesinger保存的文件
   * 带有setting的是ui格式转为py格式的文件
   
### 由于程序是用vs2017写的，需要整个项目的朋友可以下载所有文件放到文件夹里用vs2017打开pyqt5test.sln即可

界面预览
 =



![头像](https://img-blog.csdnimg.cn/20181227150324143.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyNjY4NTI3,size_16,color_FFFFFF,t_70)


#### 应老板要求打个小广告！！！！！！！！！！！！！
#### 伦图科技（广州）———物联网无线通讯解决方案专家
#### 我们公司的无线数传模块
![头像](https://img-blog.csdnimg.cn/20181227153644173.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyNjY4NTI3,size_16,color_FFFFFF,t_70)
![头像](https://img-blog.csdnimg.cn/20181227152943934.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyNjY4NTI3,size_16,color_FFFFFF,t_70)
![头像](https://img-blog.csdnimg.cn/20181227153111289.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyNjY4NTI3,size_16,color_FFFFFF,t_70)


#### 详情可以点击网站或加微信了解
http://www.logi-iot.com/
![头像](https://img-blog.csdnimg.cn/20181227164738523.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQyNjY4NTI3,size_16,color_FFFFFF,t_70)













