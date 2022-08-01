
# Bit Manipulation Design Verification

The verification environment is setup using [Vyoma's UpTickPro](https://vyomasystems.com) provided for the hackathon.

![image](https://user-images.githubusercontent.com/40283371/182212702-8fd4a4da-5a9d-476c-a031-980bf1923653.png)



## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (Multiplexer module here) which takes in *3 inputs 32 bits* *1 InstructionSet  32 bits*  and * 1 Output 33 bits*

The values are assigned to the input port using 
```
    SRC1_Values = map(''.join, product('0123456789ABCDEF', repeat=8))
    SRC2_Values = map(''.join, product('0123456789ABCDEF', repeat=8))
    SRC3_Values = map(''.join, product('0123456789ABCDEF', repeat=8))
    Instruction = map(''.join, product('0123456789ABCDEF', repeat=2))

```

The assert statement is used for comparing the Valid bit of BitManipulation's output to the expected value.

The following error is seen:
```

                     
```
## Test Scenario **(Important)**
- SRC1_Values = map(''.join, product('0123456789ABCDEF', repeat=8))
  SRC2_Values = map(''.join, product('0123456789ABCDEF', repeat=8))
  SRC3_Values = map(''.join, product('0123456789ABCDEF', repeat=8))
  Instruction = map(''.join, product('0123456789ABCDEF', repeat=2))


Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```

  
```
For the Sequence detector design, the logic should be ``  `` instead `` `` in the design code.

## Design Fix
Updating the design and re-running the test makes the test pass.








## Verification Strategy


