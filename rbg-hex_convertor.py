def rgb_hex():
  invalid_msg = 'This values are disabled!'
  red = int(raw_input('Enter value for red: '))
  print(hex(red)[2:])
  if red < 0 or red > 255:
    print(invalid_msg)
    return
  green = int(raw_input('Enter value for green: '))
  print(hex(green)[2:])
  if green < 0 or green > 255:
    print(invalid_msg)
    return
  blue = int(raw_input('Enter value for blue: '))
  print(hex(blue)[2:])
  if blue < 0 or blue > 255:
    print(invalid_msg)
    return
  val = (red << 16) + (green << 8) + blue
  print('%s' %(hex(val)[2:]).upper())

def hex_rgb():
  hex_val = raw_input('Enter hex value')
  if len(hex_val) != 6:
    print('Hex numbers should have 6 digits')
    return
  else:
    hex_val = int(hex_val, 16)
  
  two_hex_digits = 2 ** 8
  blue = hex_val % two_hex_digits
  print(blue)
  hex_val = hex_val >> 8
  green = hex_val % two_hex_digits
  print(green)
  hex_val = hex_val >> 8
  red = hex_val % two_hex_digits
  print(red)
  print('Res: %s Green: %s Blue: %s' %(red, green, blue))

def convert():
  while True:
    option = raw_input('Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit:')
    
    if option == '1':
      print('RGB to Hex...')
      rgb_hex()
    elif option == '2':
      print('Hex to RGB...')
      hex_rgb()
    elif option == 'X':
      option = option.upper()
      break
    else:
      print('Error.')
convert()