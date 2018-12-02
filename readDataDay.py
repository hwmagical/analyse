# -*- coding:utf8 -*-  
# hwmagical

import binascii   
import struct
'''
struct StockDay
{
    unsigned long  Date;       //日期
    unsigned long  OpenPrice;  //开
    unsigned long  MaxPrice;   //高
    unsigned long  MinPrice;   //低
    unsigned long  ClosePrice; //收
    float          Money;      //成交金额
    unsigned long  Total;      //成交量   单位：百股（手）
    unsigned long  NoUse1;     //未使用
};
'''

#print("----------------------------------")
#f = open(r'D:\Developer\GitHub\analyse\data\sh601688.day', 'rb')  
#while True:
#    try:
#        a = f.read(32)
#        if a != b'':
#            date, openPrice, MaxPrice, MinPrice, ClosePrice, Money, Total, other  = struct.unpack("LLLLLfLL",a)
#            print(date, openPrice, MaxPrice, MinPrice, ClosePrice, Money, Total, other)
#        else:
#            break
#    except:
#        break
#f.close()
#print("----------------------------------")


#   00 ~ 01 字节：日期，整型，设其值为num，则日期计算方法为：
#                 year=floor(num/2048)+2004;
#                 month=floor(mod(num,2048)/100);
#                 day=mod(mod(num,2048),100);
#   02 ~ 03 字节： 从0点开始至目前的分钟数，整型
#   04 ~ 07 字节：开盘价，float型
#   08 ~ 11 字节：最高价，float型
#   12 ~ 15 字节：最低价，float型
#   16 ~ 19 字节：收盘价，float型
#   20 ~ 23 字节：成交额，float型
#   24 ~ 27 字节：成交量（股），整型
#   28 ~ 31 字节：（保留）

print("----------------------------------")
f = open(r'.\data\sh601688.lc1', 'rb')  
while True:
    try:
        a = f.read(32)
        if a != b'':
            date, time, openPrice, MaxPrice, MinPrice, ClosePrice, Money, Total, other  = struct.unpack("hhfffffLL",a)
            print(int(date/2048)+2004, int((date%2048)/100), (date%2048)%100, int(time/60), time%60, 
                  '%.2f'%openPrice, '%.2f'%MaxPrice, '%.2f'%MinPrice, '%.2f'%ClosePrice, Money, Total, other)
        else:
            break
    except:
        break
f.close()
print("----------------------------------")
