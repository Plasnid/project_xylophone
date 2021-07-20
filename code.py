print("Hello World!")
import time
import board
import busio
import adafruit_aw9523
from digitalio import DigitalInOut, Direction

i2c = busio.I2C(board.SCL1, board.SDA1)
aw = adafruit_aw9523.AW9523(i2c)

# led_pin = aw.get_pin(0)

solenoid_count = 2 # total number of solenoids used
start_pin = 2 # starting at pin A2 for this version

solenoid = []

# solenoid_1 = DigitalInOut(getattr(board, "A2"))
# solenoid_1.direction = Direction.OUTPUT
# solenoid_2 = DigitalInOut(getattr(board, "A3"))
# solenoid_2.direction = Direction.OUTPUT
solenoid_1 = aw.get_pin(1)
solenoid_1.direction = Direction.OUTPUT
solenoid_2 = aw.get_pin(2)
solenoid_2.direction = Direction.OUTPUT
solenoid_3 = aw.get_pin(3)
solenoid_3.direction = Direction.OUTPUT
solenoid_4 = aw.get_pin(4)
solenoid_4.direction = Direction.OUTPUT
solenoid_5 = aw.get_pin(5)
solenoid_5.direction = Direction.OUTPUT
solenoid_6 = aw.get_pin(6)
solenoid_6.direction = Direction.OUTPUT
solenoid_7 = aw.get_pin(7)
solenoid_7.direction = Direction.OUTPUT
solenoid_8 = aw.get_pin(8)
solenoid_8.direction = Direction.OUTPUT
solenoid.append(solenoid_1)
solenoid.append(solenoid_2)
solenoid.append(solenoid_3)
solenoid.append(solenoid_4)
solenoid.append(solenoid_5)
solenoid.append(solenoid_6)
solenoid.append(solenoid_7)
solenoid.append(solenoid_8)

STRIKE_TIME = 0.01 # Time between initiating a strike and turning it off
TIME_BETWEEN = 0.5 # Timee between actions in seconds

song = [0,1,2,3,4,5,6,7]

def play(key, time_to_strike):
    print(key)
    solenoid[key].value = True
    print(solenoid[key].value)
    time.sleep(time_to_strike)
    solenoid[key].value = False

def rest(time_to_wait):
    time.sleep(time_to_wait)

while True:
    # Play each of the bars
    # for bar in range(solenoid_count):
    #    play(bar, STRIKE_TIME)
    #    rest(TIME_BETWEEN)

    # time.sleep(1.0)  # Wait a bit before playing the song

    # Play the notes defined in song
    # simple example does not vary time between notes
    for bar in range(len(song)):
        play(song[bar], STRIKE_TIME)
        rest(TIME_BETWEEN)

    # time.sleep(1.0)
