# hlt-speed-tweak

To use this script, copy the LapTimer file to your computer, and determine your correction factor. You can find the correction factor by logging both GPS and OBD speeds at a steady speed. Then figure your correction factor by dividing GPS_SPEED/OBD_SPEED. Your GPS speed will typically be lower than your OBD speed.

Once you have the file and know your correction factor, run the script with the following options:

python hlt-speed-tweak -i [LapTimer file location] -c [Correction factor in format .95 or 1.1] -o [Optional output file location, default is "corrected_obd_speed.hlptrz"]
