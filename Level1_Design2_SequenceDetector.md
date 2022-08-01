# Sequence detector Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![image](https://user-images.githubusercontent.com/40283371/182210190-ebf07bff-eb6d-4150-ac55-758f478f5746.png)


## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (Multiplexer module here) which takes in *1 input* *1 reset* *1 Clock* and * 1 Output*

The values are assigned to the input port using 
```
dut.reset.value = 1
await FallingEdge(dut.clk)  
dut.reset.value = 0
await FallingEdge(dut.clk)

dut.inp_bit = 1
await FallingEdge(dut.clk)

```

The assert statement is used for comparing the SequenceDetector's outut to the expected value.

The following error is seen:
```
The sequence is not detetced by the FSM although a input sequence 1011 is provided 
Sequence detector result is incorrect for input
                     
```
## Test Scenario **(Important)**
- Test Inputs: 1011
- dut.seq_seen.value = 1 
- Observed Output in the DUT dut.seq_seen.value = 00 

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
SEQ_1:
      begin
        if(inp_bit == 1)
          next_state = IDLE;   ---> BUG
        else
          next_state = SEQ_10;
      end
      
SEQ_101:
      begin
        if(inp_bit == 1)
          next_state = SEQ_1011;
        else
          next_state = IDLE;  --> BUG
      end
  
```
For the Sequence detector design, the logic should be ``SEQ1 and SEQ10`` instead of ``IDLE and IDLE`` as in the design code.

## Design Fix
Updating the design and re-running the test makes the test pass.


![image](https://user-images.githubusercontent.com/40283371/182210977-01dac6bf-32da-44fd-9b6a-e82f509f9b84.png)



The updated design is checked in as seq_detect_1011_Fix.v

## Verification Strategy
For different values of input the corresponding output is evaluated and the bug has been detected.

