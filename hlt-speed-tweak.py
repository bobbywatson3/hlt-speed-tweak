#!/usr/bin/env python
import xml.etree.ElementTree as ET
file_name = "LapTimer-0131-20150326-096540.hlptrz"
correction_factor = 0.96

parser = ET.XMLParser(encoding="windows-1252")
tree = ET.parse(file_name, parser=parser)
root = tree.getroot()

for speed in root.findall('.//obd/speed'):
    corrected_speed = float(speed.text) * correction_factor
    speed.text = str(corrected_speed)
tree.write('corrected_speed.xml')
