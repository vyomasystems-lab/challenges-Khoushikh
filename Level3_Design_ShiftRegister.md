# Multiplexer Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![image](https://user-images.githubusercontent.com/40283371/182205898-139e069f-8b75-4a59-98a5-f40f525bedba.png)


## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (ShiftRegister module here) which takes in *7 inputs* and gives *4 outputs*

The values are assigned to the input port using 
```
data=list(map(''.join, product('01', repeat=4)))
dut.D0.value= int(D[0])
dut.D1.value= int(D[1])
dut.D2.value= int(D[2])
dut.D3.value= int(D[3])
dut.S0.value= 1
dut.S1.value= 1 

```

The assert statement is used for comparing the Mulitplexer's outut to the expected value.

The following error is seen:
```
Expected: {dut.D2.value}{dut.D1.value}{dut.D0.value}{dut.D3.value} Got: {dut.Q3.value}{dut.Q2.value}{dut.Q1.value}{dut.Q0.value}"
                     AssertionError: Expected: 0100 Got: 0110
                     
```

## Test Scenario **(Important)**
- Input - 0 0 1 0
- BeforeShift  0 0 1 0
- AfterShift   0 1 1 0
- Expected: 0100 Got: 0110

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
multiplexer_4_1 #(1) mux1(X1, Q1 --> BUG, Q2, Q1, D1, S1, S0);  
  
```
For the Multiplexer design, the logic should be ``multiplexer_4_1 #(1) mux1(X1, Q0, Q2, Q1, D1, S1, S0); `` instead of ``multiplexer_4_1 #(1) mux1(X1, Q1 --> BUG, Q2, Q1, D1, S1, S0); `` as in the design code.

## Design Fix
Updating the design and re-running the test makes the test pass.

![image](https://user-images.githubusercontent.com/40283371/182206954-b19ad4e3-6f04-4a63-94d9-a64d41eea56e.png)



The updated design is checked in as ShifRegister_fix.v

## Verification Strategy
For different values of input the corresponding output is evaluated and the bug has been detected.
