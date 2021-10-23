class ConvertToDataType:
  def convertToDataType(self, num, mode = 0):
    help = '''Modes:
    0 - denary to binary
    1 - binary to denary
    2 - denary to hexidecimel'''    
    
    if mode == -1:
      return help
    elif mode == 0:
      return str(bin(num))[2:]
    elif mode == 1:
      return int(str(num), 2)
    elif mode == 2:
      return str(hex(num))[2:]