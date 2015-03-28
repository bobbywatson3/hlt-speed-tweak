#!/usr/bin/env python
import xml.etree.ElementTree as ET
import gzip
import argparse
import os.path

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', 
            help="Input LapTimer file location.", required = True)
parser.add_argument('-o', '--output', 
            help='Destination file name for corrected LapTimer file. Default is "corrected_obd_speed.hlptrz"')
parser.add_argument('-c', '--correction-factor', 
            help="Correction factor to be applied in format '0.95' or '1.1'", required = True)
args = parser.parse_args()


if args.input.endswith('.hlptrz'):
    lap_timer_file = gzip.open(args.input, 'rb')
    lap_timer_string = lap_timer_file.read()
    root = ET.fromstring(lap_timer_string)
    for speed in root.findall('.//obd/speed'):
        corrected_speed = float(speed.text) * float(args.correction_factor)
        speed.text = str(corrected_speed)
    tree = ET.ElementTree(root)
    if not args.output:
        args.output = 'corrected_obd_speed.hlptrz'
    corrected_gzip = gzip.open(args.output, 'wb')
    tree.write(corrected_gzip)
    corrected_gzip.close()
    lap_timer_file.close()
    print "Corrected OBD speed LapTimer file saved to:", os.path.realpath(corrected_gzip.name)
else: 
    parser = ET.XMLParser(encoding="windows-1252")
    tree = ET.parse(args.input, parser=parser)
    root = tree.getroot()
    for speed in root.findall('.//obd/speed'):
        corrected_speed = float(speed.text) * float(args.correction_factor)
        speed.text = str(corrected_speed)
    if not args.output:
        args.output = 'corrected_speed.hlptrl'
    tree.write(args.output)
    print "Corrected OBD speed LapTimer file saved to:", os.path.realpath(args.output)
