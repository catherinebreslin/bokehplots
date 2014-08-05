import sys
import wave
import numpy as np
from bokeh.plotting import *

def plot_wave_segment(time, data, start, end, framerate):
    st = int(start*framerate)
    et = int(end*framerate)
    if et >= len(data):
        et = len(data)

    secs = time[len(data)-1]

    if start >= 0 and end <= secs:
        figure()
        line(time[st:et],data[st:et],color="black",plot_height=300, plot_width=1000,title=None)
        # Change some of the axis properties
        ygrid().grid_line_color=None
        xgrid().grid_line_color=None
        xaxis().location = "top"
        axis().major_label_text_font_size = "14pt"
        axis().axis_line_width=2
        axis().major_tick_line_width=2 
        axis().major_tick_in = 0
        axis().major_tick_out = 10

def main(argv):

    if len(argv)<1:
        print "Expected: plot_wave.py <wavfile>"
        exit(1)

    wavefn=argv[0]

    # Read in data from wave file
    wavfile=wave.open(wavefn)
    (nchannels, sampwidth, framerate, nframes, comptype, compname)=wavfile.getparams()
    print nframes

    dstr = wavfile.readframes(nframes)
    data = np.fromstring(dstr, np.int16)

    time=np.asarray([float(i)/float(framerate) for i in range(len(data))])

    # Create the output page
    output_file("wave.html")

    # Plot the whole wave
    plot_wave_segment(time, data, 0, time[len(data)-1], framerate)

    # Plot a segment of the waveform
    plot_wave_segment(time, data, 0.82, 0.92, framerate)

    # Show the HTML page
    show()

if __name__ == "__main__":
   main(sys.argv[1:])

