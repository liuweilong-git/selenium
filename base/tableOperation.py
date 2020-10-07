from time import sleep
from .elementIsExist import ElementIsExist


class TableOperation:
    """表格操作"""
    def __init__(self, driver):
        self.driver = driver

    def get_table(self):
        """获取table
        返回table的headers,body_rows 和 body_rows_column
        """
        sleep(1)
        # 列表顺序： table, header, body_rows, body_rows_columns
        tables_header_body = [["table #dataArea>table",
                               "table #dataArea>table>.header>td",
                               "table #dataArea>table>tr:not(.header)",
                               "table #dataArea>table>tr:not(.herder)>td"],
                              ]
        # 获取画面显示的table
        for table_header_body in tables_header_body:
            # 如果找到的父节点为空，则父节点不存在，则查找的table不匹配，在页面中不存在
            if ElementIsExist(self.driver).is_exist(table_header_body[0]):
                table = self.driver.find_element_by_css_selector(table_header_body[0])
                headers = table.find_elements_by_css_selector(table_header_body[1])
                body_rows = table.find_elements_by_css_selector(table_header_body[2])
                rows = []
                for body_row in body_rows:
                    body_row_column = body_row.find_elements_by_css_selector(table_header_body[3])
                    rows.append(body_row_column)
                return headers, rows
            else:
                print("table 定位失败")
                return

    def select_row(self, header_text, row_text):
        """
        根据header中的列获取对应的body中的行
        :param header_text: header 中列内容
        :param row_text: leader 列对应的body列内容
        :return: 返回body中的行
        """
        headers, rows = self.get_table()
        # 获取传入的header的index
        idx = int()
        for header in headers:
            if header.text == header_text:
                idx = headers.index(header)
        # 通过index在body中寻找相应index的内容
        for row in rows:
            if row[idx].text == row_text:
                return row

    def row_click(self, header_text, row_text):
        """选择表格中行并且单击"""
        row = self.select_row(header_text, row_text)
        # 返回的row是一个list，driver不能进行单击操作，所以需要给具体的值
        # 如果返回的row中有button，可以给出button的index实现row中button单击
        return row[0].click()
