#!/usr/bin/env python
import xml.etree.ElementTree as ET
import gzip

lap_timer_file = "LapTimer-0131-20150326-093740.hlptrz"
correction_factor = 0.96

if lap_timer_file.endswith('.hlptrz'):
    print "Unzipping file"
    lap_timer_file = gzip.open(lap_timer_file, 'rb')
    lap_timer_string = lap_timer_file.read()
    root = ET.fromstring(lap_timer_string)
    for speed in root.findall('.//obd/speed'):
        corrected_speed = float(speed.text) * correction_factor
        speed.text = str(corrected_speed)
    tree = ET.ElementTree(root)
    corrected_gzip = gzip.open('corrected_obd_speed.hlptrz', 'wb')
    tree.write(corrected_gzip)
    corrected_gzip.close()
    lap_timer_file.close()
else: 
    parser = ET.XMLParser(encoding="windows-1252")
    tree = ET.parse(lap_timer_file, parser=parser)
    root = tree.getroot()

    for speed in root.findall('.//obd/speed'):
        corrected_speed = float(speed.text) * correction_factor
        speed.text = str(corrected_speed)
    tree.write('corrected_speed.hlptrz')

