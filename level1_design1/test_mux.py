# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random



@cocotb.test()
async def test_mux(dut):

    for i in range (0,31):
        dut.sel.value = i  
        InputVal = random.randint(0,3)
        str1 =  "inp" + str(i)
        if i != 30:
            dut._id(str1,extended = False).value = InputVal
            await Timer(2, units='ns')
            # print(dut.sel.value, InputVal, dut.out.value,dut._id(str1,extended = False).value)
            assert dut.out.value == InputVal , f"Mux result is incorrect: Sel Value {i} |  Input value = {dut._id(str1,extended = False).value} | OuptValue = {dut.out.value} |  Expected Value {dut._id(str1,extended = False).value}"
        else:
            dut._id(str1,extended = False).value =0 
            await Timer(2, units='ns')
            # print(dut.sel.value, InputVal, dut.out.value,dut._id(str1,extended = False).value)
            assert dut.out.value == 0 , f"Mux result is incorrect: Sel Value {i} | Input value = {dut._id(str1,extended = False).value} | OuptValue = {dut.out.value} |  Expected Value {dut._id(str1,extended = False).value}"


    