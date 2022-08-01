import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

from itertools import product


@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """
    S=[[0,0],[1,0]]
    clock = Clock(dut.CLK, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    data=list(map(''.join, product('01', repeat=4)))
    # print(data)

    for i in S:
        for D in data:
            #load the data
            dut.D0.value= int(D[0])
            dut.D1.value= int(D[1])
            dut.D2.value= int(D[2])
            dut.D3.value= int(D[3])
            dut.S0.value= 1
            dut.S1.value= 1 
            
            await FallingEdge(dut.CLK) 
            await FallingEdge(dut.CLK)

            dut.S0.value= i[0]
            dut.S1.value= i[1] 
            print("BeforeShift ",i[0],i[1],dut.Q3.value,dut.Q2.value,dut.Q1.value,dut.Q0.value)
            await FallingEdge(dut.CLK)
            print("AfterShift  ",i[0],i[1],dut.Q3.value,dut.Q2.value,dut.Q1.value,dut.Q0.value)

            if (i==[0,0]):
                assert (dut.Q0.value == dut.D3.value  and dut.Q1.value == dut.D0.value and dut.Q2.value == dut.D1.value and dut.Q3.value == dut.D2.value), f"Expected: {dut.D2.value}{dut.D1.value}{dut.D0.value}{dut.D3.value} Got: {dut.Q3.value}{dut.Q2.value}{dut.Q1.value}{dut.Q0.value}" 
            elif (i==[1,0]):
                assert (dut.Q0.value == dut.D1.value and dut.Q1.value == dut.D2.value and dut.Q2.value == dut.D3.value and dut.Q3.value == dut.D0.value), f"Expected: {dut.D0.value}{dut.D3.value}{dut.D2.value}{dut.D1.value} Got: {dut.Q3.value}{dut.Q2.value}{dut.Q1.value}{dut.Q0.value}" 
