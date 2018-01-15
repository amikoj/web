# !/usr/bin/env python
# -*-encoding:utf-8 -*-


class PageConfig(object):
    u"""
    用于配置html界面的基本元素变量：url,显示字串等.

    """
    # 主页跳转界面
    HOME_DOMAIN = u"http://www.enjoytoday.cn"
    JOURNAL_DOMAIN = u"http://journal.enjoytoday.cn"
    HOBBY_DOMAIN = u"http://hobby.enjoytoday.cn"
    BLOG_DOMAIN = u"http://blog.enjoytoday.cn"
    COURSEWARE_DOMAIN = u"http://www.enjoytoday.cn/courseware.html"
    CONTACT_DOMAIN = u"http://www.enjoytoday.cn/contact.html"
    WEB_BRAND = u"EnjoyToday"
    HOME_TEXT = u"主页"
    JOURNAL_TEXT = u"日志"
    HOBBY_TEXT = u"爱好"
    BLOG_TEXT = u"博客"
    COURSEWARE_TEXT = u"课件"
    CONTACT_TEXT = u"联系"
    KEYWORDS =["",""]


class PageDebugConfig(object):
    # 主页跳转界面
    HOME_DOMAIN = u"/"
    JOURNAL_DOMAIN = u"/journal"
    HOBBY_DOMAIN = u"/hobby"
    BLOG_DOMAIN = u"/blog"
    COURSEWARE_DOMAIN = u"/courseware.html"
    CONTACT_DOMAIN = u"/contact.html"
    WEB_BRAND = u"EnjoyToday"
    HOME_TEXT = u"主页"
    JOURNAL_TEXT = u"日志"
    HOBBY_TEXT = u"爱好"
    BLOG_TEXT = u"博客"
    COURSEWARE_TEXT = u"课件"
    CONTACT_TEXT = u"联系"
    KEYWORDS = ["", ""]

# context ={'page':PageConfig}
context ={'page':PageDebugConfig}