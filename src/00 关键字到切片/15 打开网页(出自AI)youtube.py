from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class WebWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 设置窗口标题和大小
        self.setWindowTitle("youtube")
        self.resize(1024, 768)  # 宽度x高度

        # 创建浏览器组件
        self.browser = QWebEngineView()
        # 设置要打开的固定网页URL
        self.browser.setUrl(QUrl("https://www.youtube.com"))
        # 将浏览器组件设置为主窗口的中央部件
        self.setCentralWidget(self.browser)

if __name__ == "__main__":
    # 创建应用实例
    app = QApplication([])
    # 创建并显示窗口
    window = WebWindow()
    window.show()
    # 启动应用主循环
    app.exec_()