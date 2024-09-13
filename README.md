# DomeRotator

Control over rotation of our Schneider MDrive stepper motor.

## Requires
* pyserial
* OpenCV
* pygame

## Background

We don't have an ASCOM driver for our dome, so we must rotate it manually.  This script allows remote operation of the dome, albeit not in TheSkyX.

## Future ideas:

* Use image processing to automatically rotate the dome.
* Query TheSkyX for the position of the telescope, and automatically position the dome.  This is complicated by the offset of the GEM, but it is calculable.
