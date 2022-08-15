#-*- coding: utf-8 -*-
import pytest
from lib.apiLib.login import Login
from tools.getExcelData import get_excelData2
import allure
import json,os
#1- 封装测试类
class TestLogin:
    #[({},{}),({},{})]
    @pytest.mark.parametrize('inData,respData',get_excelData2('登录模块','Login'))  # parametrize('变量'，值)
    def test_login(self,inData,respData):
        #1- 调用--封装模块
        res=Login().login(inData,getToken=False)
        print(res)
        #2- 断言  实际结果与预期的结果进行比较
        assert res['msg'] == respData['msg']


if __name__ == '__main__':
    #-s:输出打印信息； -q  简化输出
    #--alluredir =../report/tmp---生成allure报告需要的源数据
    pytest.main(['test_login.py','-s','--alluredir','../report/tmp'])
    #allure generate---生成报告
    #方案二：allure serve---起服务----自动打开浏览器---一般设置默认浏览器
    os.system('allure serve ../report/tmp')
    #生成报告