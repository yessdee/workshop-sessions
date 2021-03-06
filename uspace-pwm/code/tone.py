#!/usr/bin/python
import time
from pwm import *

BUZZER = 2
pwm_export_channel(BUZZER)

melody = [379218, 379218, 100000, 379218,
          100000, 477782, 379218, 100000,
          318878, 100000, 100000, 100000,
          637754, 100000, 100000, 100000,
          477782, 100000, 100000, 637754,
          100000, 100000, 75814,  100000,
          100000, 568182, 100000, 506072,
          100000, 536192, 568182, 100000,
          637754, 379218, 379218,
          284092, 100000, 35792, 318878,
          100000, 379218, 100000, 477782,
          100000, 379218, 100000, 477782,
          425712, 506072, 100000, 100000,
          379218, 379218, 100000, 379218,
          100000, 477782, 379218, 100000,
          318878, 100000, 100000, 100000,
          637754, 100000, 100000, 100000,
          284092, 100000, 35792, 318878,
          100000, 379218, 100000, 477782,
          100000, 379218, 100000, 477782,
          425712, 506072, 100000, 100000,
          ]

note = [0.083, 0.083, 0.083, 0.083,
        0.083, 0.083, 0.083, 0.083,
        0.083, 0.083, 0.083, 0.083,
        0.083, 0.083, 0.083, 0.083,
        0.083, 0.083, 0.083, 0.083,
        0.083, 0.083, 0.083, 0.083,
        0.083, 0.083, 0.083, 0.083,
        0.083, 0.083, 0.083, 0.083,
        0.111, 0.111, 0.111,
        0.083, 0.083, 0.083, 0.083,
        0.083, 0.083, 0.083, 0.083,
        0.083, 0.083, 0.083, 0.083,
        0.083, 0.083, 0.083, 0.083,
        0.083, 0.083, 0.083, 0.083,
        0.083, 0.083, 0.083, 0.083,
        0.083, 0.083, 0.083, 0.083,
        0.111, 0.111, 0.111, 0.111,
        0.083, 0.083, 0.083, 0.083,
        0.083, 0.083, 0.083, 0.083,
        0.083, 0.083, 0.083, 0.083,
        0.083, 0.083, 0.083, 0.083]

count = 0
while count < 83:
    pwm_set_period(BUZZER, melody[count])
    duty = melody[count]//2
    pwm_set_dutycycle(BUZZER, duty)
    pwm_enable(BUZZER)
    time.sleep(note[count])
    pwm_set_dutycycle(BUZZER, 0)
    time.sleep(note[count])
    count += 1

pwm_unexport_channel(BUZZER)
