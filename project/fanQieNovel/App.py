# -*- encoding: utf-8 -*-
# verified time: 2024/5/30
from __future__ import annotations

from config import *
from requests import Session


class FanQie:
    def __init__(self) -> None:
        # 初始化函数，定义基本参数
        super().__init__()  # 调用父类的初始化函数
        self.session = Session()  # 创建一个Session对象，并赋值给self.session

    def search(self, keywords: str) -> list[dict] | str:
        """
        搜索书籍信息

        参数:
        keywords (str): 关键字

        返回:
        list: 书籍信息列表
        """
        # 获得书本基本信息
        params = {
            'aid': 1967,
            'q': keywords
        }
        book_list_info = self.session.get(search_url, params=params, headers=headers).json()
        return book_list_info['data']['ret_data'] if 'ret_data' in book_list_info[
            'data'].keys() else '未配置cookie或者cookie失效'

    def direct(self, book_id: str) -> list[str] | str:
        # 获取书本目录
        params = {
            'book_id': book_id,  # 书本ID
            'device_platform': 'android',  # 设备平台
            'version_code': 600,  # 版本码
            'novel_version': None,  # 小说版本
            'app_name': 'news_article',  # 应用名称
            'version_name': '6.0.0',  # 应用版本名
            'app_version': '6.0.0aid=520',  # 应用版本号
            'channel': '1',  # 渠道
            'device_type': 'landseer',  # 设备类型
            'os_api': '25',  # 操作系统API
            'os_version': '10',  # 操作系统版本
        }
        direc_list_info = self.session.get(directory_url, params=params, headers=headers).json()
        return direc_list_info['data']['item_list'] if 'item_list' in direc_list_info[
            'data'].keys() else '未配置cookie或者cookie失效'

    def content(self, item_id: str):
        """
        获取当前章节正文内容

        Args:
            item_id (str): 章节ID

        Returns:
            str: 章节正文内容

        Raises:
            str: '未配置cookie或者cookie失效'
        """
        # 定义参数
        params = {
            'item_id': item_id
        }
        # 发送GET请求并解析响应内容为JSON格式
        content_info = self.session.get(content_url, params=params, headers=headers).json()

        content = self.get_content(content_info, "content")
        title = self.get_content(content_info, "title")
        return {
            "content": content,
            "title": title
        }


    def get_content(self, content_info, key):
        return content_info['data'].keys() and content_info['data'][key] or '未配置cookie或者cookie失效'
