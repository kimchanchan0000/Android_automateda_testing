API 接口

类 uiautomator2.Device（ host='127.0.0.1' ， port=7912 ）

    adb_shell（ *args ） [源代码]

        例：
            adb_shell（'pwd'）adb_shell（'ls'， '-l'）adb_shell（'ls -l'） 
        返回：
            string，用于 stdout 与 stderr 合并，在整个 shell 命令完成后。 

    app_clear（ pkg_name ） [源代码]

        停止并清除应用数据：pm clear

    app_current（ ） [源代码]

        返回：
            dict（包、活动、pid？ 
        抛出异常：
            EnvironementError （环境错误） 
        对于开发人员：
            函数 reset_uiautomator 需要这个函数，所以这里不能用 jsonrpc。 

    app_icon（ package_name： str ） [源代码]

        返回：
            必。 图像 
        抛出异常：
            Uia错误 

    app_info（ pkg_name ） [源代码]

        获取应用信息

        参数：
            pkg_name （str）：包名称 
        返回示例：

            {
                “mainActivity”： “com.github.uiautomator.MainActivity”， 1760809 1001007/ 

            }
        抛出异常：
            Uia错误 

    app_install（ url ， installing_callback=None ， server=None ） [源代码]

        {u'message'： u'downloading'， “progress”： {u'totalSize'： 407992690， u'copiedSize'： 49152}}

        返回：
            packageName （包名称） 
        抛出异常：
            RuntimeError （运行时错误） 

    app_list（ filter： str = None ） → list [源代码]

        参数：
            过滤器： [-f] [-d] [-e] [-s] [-3] [-i] [-u] [–用户USER_ID] [过滤器] 
        返回：
            按筛选条件列出的应用程序列表 

    app_list_running（ ） → list [源代码]

        返回：
            正在运行的应用程序列表 

    app_start（ package_name ， activity=None ， extras={} ， wait=False ， stop=False ， unlock=False ， launch_timeout=None ， use_monkey=False ） [源代码]

        启动应用程序参数：

            package_name （str）：包名称activity （str）：应用活动stop （bool）：在启动 activity 之前停止 app。（需要 activity）use_monkey （bool）：当 activity 未给出时，使用 monkey 命令启动 appwait （bool）：等待 app 启动。default False 

        抛出异常：
            SessionBrokenError （会话中断错误） 

    app_stop（ pkg_name ） [源代码]

        停止一个应用程序：am force-stop

    app_stop_all（ excludes=[] ） [源代码]

        停止所有第三方应用程序参数：

            excludes （list）：现在想要终止的应用程序 

        返回：
            已终止的应用程序列表 

    app_uninstall（ pkg_name ） → bool [源代码]

        卸载应用程序

        返回：
            bool： 成功 

    app_uninstall_all（ excludes=[] ， verbose=False ） [源代码]

        卸载所有应用程序

    app_wait（ package_name： str ， timeout： float = 20.0 ， front=False ） → int [源代码]

        等待应用程序启动参数：

            package_name （str）：包名称timeout （float）：最大等待时间front （bool）：等待 app 成为当前应用 

        返回：
            如果启动失败，则为 pid （int） 0 

    disable_popups（ enable=True ） [源代码]

        自动点击所有弹出窗口TODO： 需要修复

    healthcheck（ ） [源代码]

        将设备重置为健康状态

        抛出异常：
            RuntimeError （运行时错误） 

    hooks_apply（ stage ， func_name ， args=（） ， kwargs={} ， ret=None ） [源代码]

        参数：
            stage（str）：“before”或“after”之一 

    hooks_register（ func ） [源代码]

        参数：
            func：应接受 3 个参数。func_name：string、args：tuple、kwargs：dict 

    jsonrpc

        让 jsonrpc 调用更轻松 例如：

            self.jsonrpc.pressKey（“主页”） 

    jsonrpc_call（ method ， params=[] ， http_timeout=60 ） [源代码]

        jsonrpc2 调用 裁判：

                http://www.jsonrpc.org/specification

    open_identify（ theme='black' ） [源代码]

        参数：
            主题 （STR）：黑色或红色 

    pull（ src： str ， dst： str ） [源代码]

        将文件从设备拉取到本地

        抛出异常：
            FileNotFoundError（py3） OSError（py2） 

        需要 atx-agent >= 0.0.9

    pull_content（ src： str ） →字节 [源代码]

        读取远程文件内容

        抛出异常：
            FileNotFoundError 

    push（ src ， dst ， mode=420 ） [源代码]

        参数：
            src （path 或 fileobj）：源文件dst （str）：目标可以是文件夹或文件路径 
        返回：

            dict 对象，例如：

                {“mode”： “0660”， “size”： 63， “target”： “/sdcard/ABOUT.rst”} 

            由于 chmod 在 android 中可能会失败，因此结果 “mode” 可能与输入 args（mode） 不同
        抛出异常：
            IOError（如果 push 出错） 

    push_url（ url ， dst ， mode=420 ） [源代码]

        参数：
            url （str）：http url 地址dst （str）：目标mode （str）：文件模式 
        抛出异常：
            FileNotFoundError（py3） OSError（py2） 

    request_agent（ relative_url： str ， method='get' ， timeout=60.0 ） [源代码]

        向 ATX-Agent 发送 http-request

    reset_uiautomator（ reason='unknown' ） [源代码]

        重置 uiautomator

        抛出异常：
            RuntimeError （运行时错误） 
        订单：

                停止 UIAtmator Keeper
                am force-stop com.github.uiautomator
                启动 UIAtautomator Keeper（am instrument -w ...）
                等待 UIAtomator 服务准备就绪

    screenshot（ *args ， **kwargs ） [源代码]

        截取设备的屏幕截图

        返回：
            必。 图像 

    service（ name ） [源代码]

        管理服务启动或停止

        例：
            d.service（“uiautomator”）.start（） （）d.service（“uiautomator”）.stop（） 

    session（ pkg_name=无 ， attach=False ， launch_timeout=无 ， strict=False ） [源代码]

        创建新会话

        参数：

            pkg_name （str）：Android 包名称attach （bool）：附加到已经运行的应用程序launch_timeout （int）：启动超时strict （bool）：与 attach 一起使用，

                当 attach 和 strict 都为 true 时，如果应用程序未运行，则会引发 SessionBrokenError 

        抛出异常：
            请求。 HTTPError、SessionBrokenError 

    set_new_command_timeout（ timeout： int ） [源代码]

        默认 3 分钟参数：

            timeout （int）：秒 

    setup_jsonrpc（ jsonrpc_url=无 ） [源代码]

        将 jsonrpc 调用包装到对象中使用示例：

            self.setup_jsonrpc（）.pressKey（“主页”） 

    shell（ cmdargs ， stream=False ， timeout=60 ） [源代码]

        运行带参数的 adb shell 命令并返回其输出。需要 atx-agent >=0.3.3

        参数：
            cmdargs： str 或 list，示例： “ls -l” 或 [“ls”， “-l”]timeout： 命令运行的秒数，当 stream 为 False 时有效stream： 用于长时间运行的进程的 bool。 
        返回：
            （output， exit_code） 当 stream 为 False 时 请求。 response当 stream 为 True 时，您必须在使用 
        抛出异常：
            RuntimeError （运行时错误） 

        对于 atx-agent 现在不支持返回退出代码。当命令出错时，exit_code 始终为 1，否则 exit_code 始终为 0

    unlock（ ） [源代码]

        解锁屏幕

    wait_activity（ activity ， timeout=10 ） [源代码]

        等待活动参数：

            activity （str）：活动名称timeout （float）：最大等待时间 

        返回：
            活动 bool 

    window_size（ ） [源代码]

        return （宽度、高度）

类 uiautomator2.Session（ server ， pkg_name=None ， pid=None ） [源代码]

    clear_text（ ） [源代码]

        明文 抛出异常：

            环境错误 

    clear_traversed_text（ ） [源代码]

        清除最后遍历的文本。

    click（ x ， y ） [源代码]

        单击位置

    close（ ） [源代码]

        关闭应用

    current_ime（ ） [源代码]

        电流输入法 返回：

            （method_id（str），显示（bool） 

        输出示例：
            （“com.github.uiautomator/.FastInputIME”，真） 

    double_click（ x ， y ， duration=0.1 ） [源代码]

        双击 Position

    drag（ sx ， sy ， ex ， ey ， duration=0.5 ） [来源]

        从一个点滑动到另一个点。

    dump_hierarchy（ compressed=False ， pretty=False ） → str [源代码]

        参数：
            shell （bool）：使用“adb shell uiautomator dump”获取层次结构pretty （bool）：格式 xml 
        等同
            内容 = self.jsonrpc.dumpWindowHierarchy（压缩，无） 

        但是通过 GET /dump/hierarchy 会更健壮当 dumpHierarchy 失败时，atx-agent 会再次重启 uiautomator，然后重试

        v-1.3.4 改回 jsonrpc.dumpWindowHierarchy

    freeze_rotation（ freeze=True ） [源代码]

        冻结或解冻当前状态下的设备旋转。

    implicitly_wait（ seconds=None ） [源代码]

        设置默认等待超时 （Set Default Wait Timeout）参数 （Args）：

            seconds（float）：等待元素出现 

        荒废的：
            推荐使用：d.settings['wait_timeout'] = 10 

    last_traversed_text

        获取最后遍历的文本。在 WebView 中用于突出显示的文本。

    long_click（ x ， y ， duration=None ） [源代码]

        长按任意坐标。参数：

            duration （float）：按下的秒数 

    make_toast（ text ， duration=1.0 ） [源代码]

        显示 toast参数：

            text （str）：要显示的文本duration （float）：显示的秒数 

    orientation

        将设备定向到左/右或自然。左/l：旋转=90，displayRotation=1右/r：旋转=270，displayRotation=3自然/n：rotation=0，displayRotation=0颠倒/u：旋转=180，displayRotation=2

    press（ key ， meta=None ） [源代码]

        通过 Name 或 Key Code 按 Key。支持的 Key Name 包括：
            主页、返回、左、右、上、下、中心、菜单、搜索、输入、删除（或 del）、最近（最近的应用程序）、volume_up、volume_down、volume_mute、相机、电源。 

    restart（ use_monkey=False ） [源代码]

        停止应用并启动

        抛出异常：
            RuntimeError （运行时错误） 

    running（ ） [源代码]

        检查会话是否正在运行。return bool

    screenshot（ filename=None ， format='pillow' ） [源代码]

        图像格式为 JPEG

        参数：
            filename （str）：保存的文件名format （string）：当 filename 为空时使用。“pillow” 或 “opencv” 之一 
        抛出异常：
            IOError、SyntaxError 
        例子：
            screenshot（“saved.jpg”）screenshot（）.save（“saved.png”）cv2.imwrite（'saved.jpg'， screenshot（format='opencv'）） 

    send_action（ code ） [源代码]

        模拟输入法 edito 代码

        参数：
            code （str 或 int）：输入法编辑器代码 
        例子：
            send_action（“搜索”）， send_action（3） 
        裁判：
            https://developer.android.com/reference/android/view/inputmethod/EditorInfo 

    send_keys（ text： str ， clear： bool = False ） [源代码]

        参数：
            text （str）：要设置的文本clear （bool）：在设置文本之前清除 
        抛出异常：
            环境错误 

    set_clipboard（ text ， label=None ） [源代码]

        参数：
            text：剪辑中的实际文本。label：剪辑数据的用户可见标签。 

    set_fastinput_ime（ enable=True ） [源代码]

        Enable （启用） 或 Disable FastInputIME （禁用 FastInputIME）

    set_orientation（ value ） [源代码]

        orientation 属性的 setter 中。

    swipe（ fx ， fy ， tx ， ty ， duration=0.1 ， steps=None ） [源代码]

        参数：
            fx， fy： 起始位置tx， ty： 起始位置duration （float）： 持续时间steps： 1 步长约为 5ms，如果设置，持续时间将被忽略 
        文件：
            UIAtomator 使用步骤而不是持续时间正如文档所说：每个步骤执行被限制在每步 5 毫秒。 
        链接：
            https://developer.android.com/reference/android/support/test/uiautomator/UiDevice.html#swipe%28int,%20int,%20int,%20int,%20int%29 

    swipe_points（ points ， duration=0.5 ） [源代码]

        参数：
            points： 是包含至少一个点对象的点数组。例如 [[200， 300]， [210， 320]]duration： 在两点之间注入的持续时间 
        链接：
            https://developer.android.com/reference/android/support/test/uiautomator/UiDevice.html#swipe（android.graphics .点[]， int） 

    tap（ x ， y ） [源代码]

        单击的别名

    touch

        ACTION_DOWN：0 ACTION_MOVE：2touch.down（x，y）touch.move（x，y）touch.up（）

    wait_fastinput_ime（ timeout=5.0 ） [源代码]

        等待FastInputIME 已准备就绪参数：

            timeout（float）：最大等待时间 

        抛出异常：
            环境错误 

