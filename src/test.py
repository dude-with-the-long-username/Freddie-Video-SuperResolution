from ipywidgets import interact
from matplotlib import pyplot as plt
from PIL import Image
import numpy as np
import av


def get_np_frame_diff(frame1, frame2):
    """Get difference of the frames
    :frame1: object of class av.VideoFrame
    :frame2: object of class av.VideoFrame
    :returns: difference of 2 frames as av.VideoFrame
    """
    np_frame1 = frame1.to_ndarray(format='rgb24')
    np_frame2 = frame2.to_ndarray(format='rgb24')
    diff = np.subtract(np_frame1, np_frame2)
    return diff


def display_frame(frame):
    """Display frame of type av.VideoFrame with matplotlib 
    :frame: object of class av.VideoFrame
    :returns: nothing
    """
    np_frame = frame.to_ndarray(format='rgb24')
    display_np_frame(np_frame)


def display_np_frame(np_frame):
    """Display numpy array with matplotlib
    :np_frame: numpy array
    :returns: nothing
    """
    plt.imshow(np_frame, interpolation='nearest', cmap='binary')
    plt.show()

def show_frames_as_diffs(filename):
    """Display frames as diffs with previous frame till next keyframe
    :filename: TODO
    :returns: TODO
    """
    container = av.open(filename)
    for frame in container.decode(video=0):
        if frame.key_frame:
            # next are p/b frames
            display_frame(frame)
            prev_frame = frame
            continue

if __name__ == "__main__":
    # extract_frames('v/mha_s4_ep2.mp4')
    pass
