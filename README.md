# HID Attack POC with Raspberry Pi Pico

This project demonstrates a Proof of Concept (POC) for a HID (Human Interface Device) attack using a Raspberry Pi Pico and the `adafruit_hid` library. This README will guide you through the setup and usage of the project.

---

## Disclaimer
This project is intended solely for educational and ethical purposes. It is designed to raise awareness about the potential risks of HID attacks and to promote better security practices. 

**Do not use this project for illegal or malicious purposes.** The author assumes no responsibility for any misuse of this project.

---

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
  - [Flash CircuitPython](#flash-circuitpython)
  - [Install the adafruit_hid Library](#install-the-adafruit_hid-library)
  - [Upload the Project Code](#upload-the-project-code)
- [Usage](#usage)
- [Credits](#credits)
- [License](#license)

---

## Introduction

This project aims to demonstrate how the Raspberry Pi Pico can be used to simulate HID attacks. HID attacks involve using a device, such as a keyboard or mouse, to send malicious inputs to a target system. This Proof of Concept illustrates the risks and emphasizes the need for secure device handling.

---

## Features
- Simulates keyboard inputs.
- Utilizes the `adafruit_hid` library for ease of development.
- Simple setup with step-by-step instructions.

---

## Requirements
- Raspberry Pi Pico
- Micro USB cable
- Computer with a USB port
- CircuitPython installed on the Raspberry Pi Pico
- `adafruit_hid` library

---

## Installation

### Flash CircuitPython
1. **Download CircuitPython**: 
   - Visit the [CircuitPython Downloads](https://circuitpython.org/) page.
   - Download the latest UF2 file for the Raspberry Pi Pico.
2. **Enter Bootloader Mode**:
   - Hold down the **BOOTSEL** button on your Raspberry Pi Pico.
   - While holding the button, connect the Pico to your computer using a USB cable.
3. **Flash CircuitPython**:
   - A new drive should appear on your computer.
   - Drag and drop the downloaded UF2 file onto this drive.

### Install the adafruit_hid Library
1. **Download the Library**:
   - Visit the [CircuitPython Bundle](https://github.com/adafruit/Adafruit_CircuitPython_Bundle) page.
   - Download the latest ZIP file.
2. **Extract and Copy**:
   - Extract the ZIP file.
   - Locate the `adafruit_hid` folder within the `lib` directory.
   - Copy this folder to the `lib` directory on your Raspberry Pi Pico.

### Upload the Project Code
1. **Clone the Repository**:
   - Clone this repository or download the project files as a ZIP.
2. **Transfer Files**:
   - Use your preferred IDE (e.g., [Thonny](https://thonny.org/)) to copy the project code to the Raspberry Pi Pico.

---

## Usage
1. Connect your Raspberry Pi Pico to a target computer using a USB cable.
2. The device will simulate keyboard inputs based on the script you have uploaded.


---


