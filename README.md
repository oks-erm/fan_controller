# fan_controller
a Python script to read temperature data from a sensor and control a fan

# Hardware
- ESP32 microcontroller
- DHT22 temperature and humidity sensor
- 12V DC fan 
- Transistor (like the 2N2222) or relay module 
- 10kΩ resistor (for the DHT22 sensor)
- Breadboard
- Jumper wires
- Power supply

# Assembly Instructions

### Step 1: Setting Up the ESP32

Insert the ESP32 into the Breadboard.

### Step 2: Wiring the DHT22 Sensor

Connect the DHT22 to the ESP32:
VCC: Connect the VCC pin of the DHT22 to a 3.3V pin on the ESP32.
GND: Connect the GND pin of the DHT22 to a GND pin on the ESP32.
Data: Connect the data pin of the DHT22 to a digital GPIO pin on the ESP32 (e.g., GPIO14). Place a 10kΩ resistor between the VCC and Data lines. 

### Step 3: Wiring the Fan

Connect the Fan Using a Transistor or Relay (depending on the fan's power requirement):
For a Transistor:
Emitter to GND: Connect the emitter of the transistor to the GND.
Collector to Fan: Connect the collector to the negative terminal of the fan.
Base to GPIO: Connect the base to a digital GPIO pin on the ESP32 through a current-limiting resistor (about 1kΩ).
Fan's Positive Terminal: Connect the positive terminal of the fan to the appropriate voltage (5V or 12V, depending on the fan specification).
For a Relay Module:
Relay Input: Connect the input of the relay module to a digital GPIO pin on the ESP32.
Fan and Power Supply: Connect the fan and power supply to the relay's output terminals, following the module's wiring diagram.

### Step 4: Connect Power Supply 

Ensure the ESP32 is powered either via USB or an external power source compatible with its voltage requirements.
If using a 12V fan with a separate power supply, connect it accordingly.

### Step 5: Check All Connections

Double-check all connections for correctness.
Ensure there are no loose wires or short circuits on the breadboard.

### Step 6: Upload the Code

Connect the ESP32 to your computer via USB.
Upload the script.

# Requirements for MicroPython Temperature-Controlled Fan Project
- MicroPython Firmware (version compatible with [Your Microcontroller Model])
- DHT22 MicroPython Library (if not included in firmware)
- umqtt.simple or umqtt.robust Library (for MQTT communication)
