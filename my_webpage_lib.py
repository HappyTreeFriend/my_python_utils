#!/usr/bin/env python
#-*-coding:utf-8-*-
#Created by happytree on 28/3/17.
#Description :

import bs4

class MyWebpage(object):

    def __init__(self, content):
        self.content = content
        self.soup = bs4.BeautifulSoup(self.content, "html.parser")

    def format_print(self):
        return self.soup.prettify()

    def find_element_id(self, id_name):
        return self.soup.find_all(id=id_name)[0]

    def find_element_tag(self, tag, tag_name):
        return tag.find_all(tag_name)

    def get_list_info(self, tag_list, attr_name, re_str):
        list_info = []
        for tag in tag_list:
            list_info.append(tag.get(attr_name).replace(re_str, "").encode("utf-8"))
        return list_info


if __name__ == "__main__":
    init_html = """"""
    my_webpage = MyWebpage(init_html)
    task_link = my_webpage.find_element_id("task_link")
    tag_li = my_webpage.find_element_tag(task_link, "li")
    list_task_id = my_webpage.get_list_info(tag_li, "id", "task_item_")