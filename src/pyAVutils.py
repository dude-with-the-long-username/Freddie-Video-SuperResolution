from matplotlib import pyplot as plt
import numpy as np
import av

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
    plt.imshow(np_frame)
    plt.show()

def np_frame_diff(frame1, frame2):
    """Get difference of the frames
    
    :frame1: object of class av.VideoFrame
    :frame2: object of class av.VideoFrame
    :returns: difference of 2 frames as av.VideoFrame

    """
    np_frame1 = frame1.to_ndarray(format='rgb24')
    np_frame2 = frame2.to_ndarray(format='rgb24')
    diff = np.subtract(np_frame1, np_frame2)
    return diff


def start_of_scene(frame):
    """Check if a frame is the start of scene with keyframe heuristic

    :frame: Object of class av.VideoFrame
    :returns: True if frame is keyframe

    """
    if frame.key_frame:
        return True
    else:
        return False

def make_generator(filename):
    """make a generator to retreive frames from video

    :filename: path to video file as string
    :returns: generator object that generates av.VideoFrame objects

    """
    container = av.open('v/mha_s4_ep2.mp4')
    return container.decode(video = 0)

if __name__ == "__main__":
    pass
    
