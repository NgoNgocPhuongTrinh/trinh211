# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 10:09:46 2024

@author: Student
"""

import math

# Viết chương trình nhập giá trị cho hai số thực a, b

a = float(input("Nhập vào số thực a: "))
b = float(input("Nhập vào số thực b: "))

# Tính giá trị biểu thức và in kết quả

B = ( ( math.sqrt(a)-math.sqrt(b) )/( pow(a,1/4)-pow(b,1/4) ) )-( ( math.sqrt(a)+pow(a*b,1/4) )/( pow(a,1/4)+pow(b,1/4) ) )
print("Kết quả: ", B)