#-*- coding: utf-8 -*-
from lib.apiLib.myShop import MyShop
from lib.apiLib.login import Login
import pytest
from tools.getExcelData import get_excelData2
class TestMyShop:#测试类---逻辑关系
    def setup_class(self):#每一个类下面所有的方法调用只运行一次
        self.token = Login().login({'username':'sq0001','password':'123456'},getToken=True)
    #定义测试方法
    @pytest.mark.parametrize('inData,respData',get_excelData2('我的商铺','listshopping'))
    def test_shop_list(self,inData,respData):#列出商铺
        res = MyShop(self.token).shop_list(inData)#商铺列出方法
        # print('body：--->', inData)
        print('实际响应结果：--->',res)
        if 'code' in res:#判断反映里是否有code这个键
            assert res['code'] == respData['code']
        else:#没有code这个键，
            assert res['error'] == respData['error']


'''
pytest 输出的信息
    .    用例通过
    F    用例失败--没有语法报错
    E    语法错误

'''
if __name__ == '__main__':
   pytest.main(['test_myShop.py','-s'])
