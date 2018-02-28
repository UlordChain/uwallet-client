# 在此处输入标题

标签（空格分隔）： 关于Qt中使用Awesome图标字体以及Elusive Icons图标

---

`qtawesome`依赖于qtpy(这个一个兼容pyqt4,5,pyside1,2的抽象层接口)

使用`qtawesome`时, 本地UI代码的qt导入也需要使用qtpy,如:
`from qtpy.QtCore import `而不能使用`from PyQt4.QtCore import `,否则`qtawesome`使用不了会报错, 因为`qtawesome`里面使用了`qtpy`导入.

然而, 本地ui代码使用`qtpy`导入时有很多问题不兼容,比如找不到`QChar`. 所以放弃此种方式而改写`qtawesome`源码.

将`qtawesome`中的`qtpy`导入,改写为本地的qt版本的导入就行了, 然后将`qtawesome`源码复制到项目中使用,不要使用安装库.

使用方式:[GitHub主页][1]


```import qtawesome as qta```
- Use Font Awesome and Elusive Icons.
```   
    fa_icon = qta.icon('fa.flag')
    fa_button = QtGui.QPushButton(fa_icon, 'Font Awesome!')
    
    asl_icon = qta.icon('ei.asl')
    elusive_button = QtGui.QPushButton(asl_icon, 'Elusive Icons!')
```
- Apply some styling
```
    # Styling icons
    styling_icon = qta.icon('fa.music',
                            active='fa.legal',
                            color='blue',
                            color_active='orange')
    music_button = QtGui.QPushButton(styling_icon, 'Styling')
```
- Stack multiple icons
```
    # Stacking icons
    camera_ban = qta.icon('fa.camera', 'fa.ban',
                          options=[{'scale_factor': 0.5,
                                    'active': 'fa.legal'},
                                   {'color': 'red'}])
    stack_button = QtGui.QPushButton(camera_ban, 'Stack')
    stack_button.setIconSize(QtCore.QSize(32, 32))
```
- Animations
```
    # Spining icons
    spin_button = QtGui.QPushButton(' Spinning icon')
    spin_icon = qta.icon('fa.spinner', color='red',
                         animation=qta.Spin(spin_button))
    spin_button.setIcon(spin_icon)
```
- Screenshot
![此处输入图片的描述][2]


在`iconic_font.py`文件249行, 有检查字体文件的md5值, 如果想更新字体文件, 则需要更新此md5值(直接打印qtawesome计算出来的然后复制就行).以及字体文件夹下的映射文件`fontawesome-webfont-charmap.json`

  [1]: https://github.com/spyder-ide/qtawesome
  [2]: https://github.com/spyder-ide/qtawesome/raw/master/qtawesome-screenshot.gif
  
  