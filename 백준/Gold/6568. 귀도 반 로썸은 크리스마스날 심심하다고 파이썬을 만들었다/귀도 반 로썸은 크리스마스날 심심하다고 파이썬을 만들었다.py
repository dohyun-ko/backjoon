def computer(memory):
  pc = 0
  adder = 0
  while True:
    command = memory[pc][0:3]
    operand = int(memory[pc][3:8], 2)

    pc += 1
    if pc > 31:
      pc = 0

    if command == "000":
      memory[operand] = bin(adder)[2:].zfill(8)

    elif command == "001":
      adder = int(memory[operand], 2)
      
    elif command == "010":
      if adder == 0:
        pc = operand
      
    elif command == "011":
      pass

    elif command == "100":
      adder -= 1
      if adder < 0:
        adder = 255

    elif command == "101":
      adder += 1
      if adder > 255:
        adder = 0

    elif command == "110":
      pc = operand
      
    elif command == "111":
      break

  print(bin(adder)[2:].zfill(8))
counter = 0
memory = [0] * 32
while True:
  try:
    command = input()
    if not command:
      break
  except EOFError:
    break
  memory[counter] = command
  counter += 1

  if counter == 32:
    computer(memory)
    counter = 0