from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl
import sys


class SimpleWebViewer(QMainWindow):
    def __init__(self, url="https://www.baidu.com"):
        super().__init__()
        self.setWindowTitle("简单网页查看器")
        self.resize(1000, 800)  # 设置窗口大小

        # 创建网页组件并加载固定URL
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(url))

        # 将网页组件设为中央部件
        self.setCentralWidget(self.browser)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 可修改此处URL为你想要固定查看的网页
    viewer = SimpleWebViewer(url="https://www.youtube.com")
    viewer.show()
    sys.exit(app.exec_())