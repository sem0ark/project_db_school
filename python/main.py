from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow

import sys

import tag_main
from app_context import AppContext

if __name__ == '__main__':
    appctxt = AppContext()       # 1. Instantiate ApplicationContext
    tag_main.main(appctxt)
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)