import os, time
import unittest
from queue import Queue
from tool.HTMLTestReportCN import HTMLTestRunner
import threading
import multiprocessing


class Main:
    def get_all_case(self):
        """导入所有的用例"""
        current_path = os.path.abspath(os.path.dirname(__file__))
        case_path = current_path + "/../scripts/"
        discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py")
        for i in discover:

            print(i)
        return discover

    def set_name(self, report_path=None):
        if report_path is None:
            current_path = os.path.abspath(os.path.dirname(__file__))
            report_path = current_path + "/../report/"
        else:
            report_path = report_path

        # 获取当前时间
        now = time.strftime("%Y{y}%m{m}%d{d}%H{h}%M{M}%S{s}").format(y="年", m="月",
                             d="日", h="时", M="分", s="秒")
        # 标题
        title = u"TYNAM后台管理系统"
        # 设置报告存放路径和命名
        report_abspath = os.path.join(report_path, title + now + ".html")
        return report_abspath, title

    def set_report(self, all_case, report_abspath, title):# , all_case, report_abspath, title, lock_html):
        """设置生成报告"""
        # lock_html.acquire()
        fp = open(report_abspath, "ab+")
        runner = HTMLTestRunner(stream=fp, title=title)
        runner.run(all_case)
        fp.close()
        # lock_html.release()
        return

    def run_case_multiprocessing(self):
        """57s"""
        # 多进程
        queue = multiprocessing.Queue()
        # lock_multiprocessing_html = multiprocessing.Lock()
        all_case = self.get_all_case()
        report_abspath, title = self.set_name()
        for i in all_case:
            queue.put(i)
        p = multiprocessing.Pool(4)
        for i in range(4):
            item = queue.get()
            p.apply_async(self.set_report, args=(item, report_abspath, title,))
        p.close()
        p.join()

    def run_case_threading(self):
        """100s"""
        # 多线程
        queue = Queue()
        # lock_html = threading.Lock()
        report_abspath, title = self.set_name()
        all_case = self.get_all_case()
        for i in all_case:
            queue.put(i)
        while queue.qsize() > 0:
            for i in range(4):
                item = queue.get()
                thread = threading.Thread(target=self.set_report, args=(item, report_abspath, title,))# lock_html))
                thread.start()
                thread.join()
            if queue.qsize() == 0:
                break

    def run_case_ordinary(self, all_case):
        """99s"""
        report_abspath, title = self.set_name()
        fp = open(report_abspath, "wb")
        runner = HTMLTestRunner(stream=fp, title=title)
        runner.run(all_case)
        fp.close()
        return

    def run(self, type):
        """选择运行模式 """
        if type == "threading":
            return self.run_case_threading()
        if type == "multiprocessing":
            return self.run_case_multiprocessing()
        if type == "ordinary":
            all_case = self.get_all_case()
            return self.run_case_ordinary(all_case)


if __name__ == '__main__':
    star = time.time()
    Main().run("threading")
    print(time.time()-star)
