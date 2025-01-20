# uiautomator2 API 接口

### adb_shell(*args) [源代码]

例：

```python
adb_shell('pwd')
adb_shell('ls', '-l')
adb_shell('ls -l')
返回：
字符串，包含 stdout 与 stderr 合并，在整个 shell 命令完成后。

app_clear(pkg_name) [源代码]
停止并清除应用数据：pm clear

app_current() [源代码]
返回：

dict（包、活动、pid？）
抛出异常：
EnvironmentError（环境错误）
对于开发人员：函数 reset_uiautomator 需要这个函数，所以这里不能用 jsonrpc。
app_icon(package_name: str) [源代码]
返回：

必须返回图像

app_info(pkg_name) [源代码]
获取应用信息

参数：

pkg_name（str）：包名称
返回示例：

{
  "mainActivity": "com.github.uiautomator.MainActivity",
  "pid": 1760809,
  "uid": 1001007
}

UiaError
app_install(url, installing_callback=None, server=None) [源代码]
返回：

packageName（包名称）
抛出异常：
RuntimeError（运行时错误）
app_list(filter: str = None) → list [源代码]
参数：

filter：筛选条件，例如：-f, -d, -e, -s, -3, -i, -u, [过滤器]
返回：

按筛选条件列出的应用程序列表
app_list_running() → list [源代码]
返回：

正在运行的应用程序列表
app_start(package_name, activity=None, extras={}, wait=False, stop=False, unlock=False, launch_timeout=None, use_monkey=False) [源代码]
启动应用程序

参数：

package_name（str）：包名称
activity（str）：应用活动
stop（bool）：在启动 activity 之前停止 app。
use_monkey（bool）：当 activity 未给出时，使用 monkey 命令启动 app
wait（bool）：等待 app 启动，默认为 False
抛出异常：

SessionBrokenError（会话中断错误）
app_stop(pkg_name) [源代码]
停止一个应用程序：am force-stop

app_stop_all(excludes=[]) [源代码]
停止所有第三方应用程序

参数：

excludes（list）：现在想要终止的应用程序
返回：

已终止的应用程序列表
app_uninstall(pkg_name) → bool [源代码]
卸载应用程序

返回：

bool：表示卸载是否成功
app_uninstall_all(excludes=[], verbose=False) [源代码]
卸载所有应用程序

app_wait(package_name: str, timeout: float = 20.0, front=False) → int [源代码]
等待应用程序启动

参数：

package_name（str）：包名称
timeout（float）：最大等待时间
front（bool）：等待 app 成为当前活动应用
返回：

如果启动失败，则返回 pid（int）为 0
disable_popups(enable=True) [源代码]
自动点击所有弹出窗口 (TODO: 需要修复)

healthcheck() [源代码]
将设备重置为健康状态
抛出异常：

RuntimeError（运行时错误）
hooks_apply(stage, func_name, args=(), kwargs={}, ret=None) [源代码]
参数：

stage（str）：可以是 "before" 或 "after"
hooks_register(func) [源代码]
参数：

func：应接受 3 个参数（func_name：string、args：tuple、kwargs：dict）
jsonrpc
让 jsonrpc 调用更轻松
例如：

python
复制
编辑
self.jsonrpc.pressKey("主页")
jsonrpc_call(method, params=[], http_timeout=60) [源代码]
jsonrpc2 调用参考：
http://www.jsonrpc.org/specification

open_identify(theme='black') [源代码]
参数：

theme（str）：黑色或红色
pull(src: str, dst: str) [源代码]
将文件从设备拉取到本地

抛出异常：

FileNotFoundError（py3）
OSError（py2）
需要 atx-agent >= 0.0.9

pull_content(src: str) → bytes [源代码]
读取远程文件内容

抛出异常：

FileNotFoundError
push(src, dst, mode=420) [源代码]
参数：

src（path 或 fileobj）：源文件
dst（str）：目标文件或文件夹路径
返回：

json
复制
编辑
{
  "mode": "0660",
  "size": 63,
  "target": "/sdcard/ABOUT.rst"
}
抛出异常：

IOError（如果 push 出错）
push_url(url, dst, mode=420) [源代码]
参数：

url（str）：http url 地址
dst（str）：目标路径
mode（int）：文件模式
抛出异常：

FileNotFoundError（py3）
OSError（py2）
request_agent(relative_url: str, method='get', timeout=60.0) [源代码]
向 ATX-Agent 发送 HTTP 请求

reset_uiautomator(reason='unknown') [源代码]
重置 uiautomator

抛出异常：

RuntimeError（运行时错误）
screenshot(*args, **kwargs) [源代码]
截取设备的屏幕截图
返回：

图像
service(name) [源代码]
管理服务的启动或停止
例：

python
复制
编辑
d.service("uiautomator").start()
d.service("uiautomator").stop()
session(pkg_name=None, attach=False, launch_timeout=None, strict=False) [源代码]
创建新会话

参数：

pkg_name（str）：Android 包名称
attach（bool）：附加到已经运行的应用程序
launch_timeout（int）：启动超时
strict（bool）：与 attach 一起使用，attach 和 strict 都为 True 时，如果应用程序未运行，会引发 SessionBrokenError
抛出异常：

HTTPError
SessionBrokenError
set_new_command_timeout(timeout: int) [源代码]
设置新的命令超时时间，默认 3 分钟

参数：

timeout（int）：秒
setup_jsonrpc(jsonrpc_url=None) [源代码]
将 jsonrpc 调用包装到对象中

示例：

python
复制
编辑
self.setup_jsonrpc().pressKey("主页")
shell(cmdargs, stream=False, timeout=60) [源代码]
运行带参数的 adb shell 命令并返回其输出。需要 atx-agent >=0.3.3

参数：

cmdargs：str 或 list（示例："ls -l" 或 ["ls", "-l"]）
timeout：命令运行的秒数，当 stream 为 False 时有效
stream：用于长时间运行的进程的 bool。
返回：

（output, exit_code）
抛出异常：

RuntimeError（运行时错误）
unlock() [源代码]
解锁屏幕

wait_activity(activity, timeout=10) [源代码]
等待活动启动

参数：

activity（str）：活动名称
timeout（float）：最大等待时间
返回：

活动是否启动成功的 bool 值
window_size() [源代码]
返回设备屏幕的宽度和高度

类 uiautomator2.Session（server, pkg_name=None, pid=None）
clear_text() [源代码]
清除文本
抛出异常：

EnvironmentError（环境错误）
clear_traversed_text() [源代码]
清除最后遍历的文本。

click(x, y) [源代码]
单击指定位置

close() [源代码]
关闭应用

current_ime() [源代码]
获取当前输入法
返回：

（method_id（str），显示（bool））
示例输出：

python
复制
编辑
("com.github.uiautomator/.FastInputIME", True)
double_click(x, y, duration=0.1) [源代码]
双击指定位置

drag(sx, sy, ex, ey,





您说：
继续
ChatGPT 说：

继续描述接口和方法：

类 uiautomator2.Session（续）：
clear_text
描述：清除当前文本输入框中的内容。
抛出异常：EnvironmentError（环境错误）
clear_traversed_text
描述：清除最后遍历的文本。在某些情况下，UI的最后被访问的文本会保留，此方法将其清除。
click（x, y）
描述：单击设备屏幕上的指定位置（x, y坐标）。
参数：
x：屏幕上的x坐标
y：屏幕上的y坐标
close
描述：关闭当前会话中的应用程序。
current_ime
描述：返回当前使用的输入法信息。
返回：包含 method_id（输入法的包名）和 is_shown（布尔值，指示输入法是否显示）的元组。
示例：("com.github.uiautomator/.FastInputIME", True)
double_click（x, y, duration=0.1）
描述：双击指定坐标位置（x, y）。
参数：
x：屏幕上的x坐标
y：屏幕上的y坐标
duration：双击之间的间隔时间（秒）
drag（sx, sy, ex, ey, duration=0.5）
描述：在屏幕上从一个点滑动到另一个点。
参数：
sx、sy：起始位置的x、y坐标
ex、ey：目标位置的x、y坐标
duration：滑动持续时间（秒）
dump_hierarchy（compressed=False, pretty=False）
描述：获取当前屏幕的层次结构，通常用于调试。
参数：
compressed：是否将输出压缩
pretty：是否以格式化方式输出（XML格式）
freeze_rotation（freeze=True）
描述：冻结或解冻设备的旋转。冻结时设备不会旋转，解冻后设备旋转恢复。
参数：
freeze：布尔值，True表示冻结，False表示解冻
implicitly_wait（seconds=None）
描述：设置全局默认的等待超时。通常用于等待UI元素出现。
参数：
seconds：指定等待的时间（秒）
last_traversed_text
描述：获取最后遍历的文本，通常用于WebView中高亮显示的文本。
long_click（x, y, duration=None）
描述：在指定位置进行长按。
参数：
x、y：长按的坐标
duration：长按持续的时间（秒）
make_toast（text, duration=1.0）
描述：在设备上显示一个Toast消息。
参数：
text：要显示的文本
duration：显示持续时间（秒）
orientation
描述：获取或设置设备的屏幕方向。
返回：
l：左旋，旋转90度
r：右旋，旋转270度
n：自然方向，0度
u：颠倒，旋转180度
press（key, meta=None）
描述：模拟按下设备上的一个物理按钮。
参数：
key：按钮的名称或键码（例如："home", "back", "volume_up"）
meta：可选的附加信息，通常为键的修饰符（如shift）
restart（use_monkey=False）
描述：重启应用程序，停止并重新启动指定应用。
参数：
use_monkey：如果为True，则使用monkey命令重启应用。
running
描述：检查会话是否仍在运行。
返回：布尔值，表示会话是否正在运行。
screenshot（filename=None, format='pillow'）
描述：截取设备屏幕的截图。
参数：
filename：保存截图的文件名（如果为None，则不会保存到文件）
format：图片的保存格式，支持"pillow"和"opencv"
send_action（code）
描述：模拟输入法编辑器（IME）的操作。
参数：
code：输入法编辑器的操作代码，可以是字符串或整数
send_keys（text, clear=False）
描述：设置文本到输入框中。
参数：
text：要输入的文本
clear：是否在输入之前清除输入框中的内容（布尔值）
set_clipboard（text, label=None）
描述：将文本设置到剪贴板。
参数：
text：要设置的剪贴板文本
label：剪贴板数据的标签（可选）
set_fastinput_ime（enable=True）
描述：启用或禁用快速输入IME。
参数：
enable：布尔值，True表示启用，False表示禁用
set_orientation（value）
描述：设置设备的屏幕方向。
参数：
value：方向值，通常为"l"（左），"r"（右），"n"（自然），"u"（颠倒）
swipe（fx, fy, tx, ty, duration=0.1, steps=None）
描述：在屏幕上滑动，从一个点到另一个点。
参数：
fx、fy：起始坐标
tx、ty：目标坐标
duration：滑动的持续时间
steps：滑动步数，如果设置了，duration参数将会被忽略
swipe_points（points, duration=0.5）
描述：通过多个点滑动屏幕。
参数：
points：包含一系列点的数组，例如[[200, 300], [210, 320]]
duration：滑动的持续时间
tap（x, y）
描述：单击指定位置（x, y）的别名。
touch
描述：模拟触摸事件，支持按下、移动和抬起的操作。
touch.down(x, y)：触摸屏幕某个位置。
touch.move(x, y)：移动触摸位置。
touch.up()：抬起触摸。
wait_fastinput_ime（timeout=5.0）
描述：等待快速输入IME准备就绪。
参数：
timeout：最大等待时间（秒）