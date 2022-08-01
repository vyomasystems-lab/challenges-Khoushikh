# Multiplexer Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![image](https://user-images.githubusercontent.com/40283371/182201013-04832885-3f28-41c4-a236-94aa076a264c.png)


## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (Multiplexer module here) which takes in *30 inputs* *1 select line*  and gives 2-bit output *out*

The values are assigned to the input port using 
```
dut.sel.value = i  
InputVal = random.randint(0,3)
str1 =  "inp" + str(i)
dut._id(str1,extended = False).value = InputVal

```

The assert statement is used for comparing the Mulitplexer's outut to the expected value.

The following error is seen:
```
Expected Value {dut._id(str1,extended = False).value}"
                     AssertionError: Mux result is incorrect: Sel Value 12 |  Input value = 10 | OuptValue = 00 |  Expected Value 10
                     
```
## Test Scenario **(Important)**
- Test Inputs: sel=12, inp12 = 10
- Expected Output: 10
- Observed Output in the DUT dut.out = 00 

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
  5'b01101: out = inp12; ---> BUG
  5'b01101: out = inp13; ---> BUG
  
```
For the Multiplexer design, the logic should be `` `` instead of ``a - b`` as in the design code.

## Design Fix
Updating the design and re-running the test makes the test pass.

![image](https://user-images.githubusercontent.com/40283371/182203050-88c22ed9-8ba7-4d66-8b10-1160badb3892.png)



The updated design is checked in as Mux_fix.v

## Verification Strategy
For different values of input the corresponding output is evaluated and the bug has been detected.
