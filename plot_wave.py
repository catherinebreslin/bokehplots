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
        p = figure(plot_height=300, plot_width=1000)

        p.line(time[st:et],data[st:et],color="black")
        # Change some of the axis properties
        p.ygrid.grid_line_color=None
        p.xgrid.grid_line_color=None
        #p.xaxis.fixed_location = "top"
        p.axis.major_label_text_font_size = "14pt"
        p.axis.axis_line_width=2
        p.axis.major_tick_line_width=2 
        p.axis.major_tick_in = 0
        p.axis.major_tick_out = 10

        
    return p


def main(argv):

    if len(argv)<1:
        print ("Expected: plot_wave.py <wavfile>")
        exit(1)

    wavefn=argv[0]

    # Read in data from wave file
    wavfile=wave.open(wavefn)
    (nchannels, sampwidth, framerate, nframes, comptype, compname)=wavfile.getparams()
    print (nframes)

    dstr = wavfile.readframes(nframes)
    data = np.fromstring(dstr, np.int16)

    time=np.asarray([float(i)/float(framerate) for i in range(len(data))])

    # Create the output page
    output_file("wave.html")

    # Plot the whole wave
    p = plot_wave_segment(time, data, 0, time[len(data)-1], framerate)

    # Plot a segment of the waveform
    p = plot_wave_segment(time, data, 0.4, 1.2, framerate)

    # Show the HTML page
    show(p)

if __name__ == "__main__":
   main(sys.argv[1:])
