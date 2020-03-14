import av
from pyAVutils import *
from playback import send_to_playback_buffer
import sys

def np_frame_upscale(np_frame):
    """Upscale given np_frame with neural nets

    :np_frame: numpy array
    :returns: TODO

    """
    # TODO: return actual upscaled method here <15-03-20, Balamurali M> #
    return np_frame


def super_res(filename):
    """Upscale the video in real-time

    :filename: TODO
    :returns: TODO

    """
    videogen = make_generator(filename)
    prev_np_frame = np.zeros(3)
    for frame in videogen:
        print ("LR frame number", frame.index)
        np_frame = frame.to_ndarray(format='rgb24')
        if start_of_scene(frame):
            prev_np_frame = np_frame
            upscaled_frame = np_frame_upscale(np_frame)
            send_to_playback_buffer(np_frame)
        else:
            diff = np.subtract(prev_np_frame, np_frame)
            upscaled_diff = np_frame_upscale(diff)
            # TODO:  <14-03-20, Balamurali M> #
            # show size of diff
            frame_merge(upscaled_frame, upscaled_diff)
            send_to_playback_buffer(upscaled_frame)


def frame_merge(latest_frame, upscaled_diff):
    """Replace pixels in latest_frame with corresponding non zero
    pixels in upscaled_diff

    :latest_frame: Latest upscaled frame as numpy array
    :upscaled_diff: Upscaled diff of new frame as numpy array
    :returns: Writes merge of latest_frame and upscaled_diff to latest_frame

    """
    latest_frame[np.nonzero(upscaled_diff)
                 ] = upscaled_diff[np.nonzero(upscaled_diff)]

if __name__ == "__main__":
    # filename = sys.argv[1]
    # super_res('v/mha_s4_ep2.mp4')

    x = np.random.random_sample((768, 1366, 3))
    y = np.zeros((768, 1366, 3))
    z = x.copy()
    display_np_frame (x)
    display_np_frame (y)
    frame_merge(x, y)
    display_np_frame(np.subtract(x, z))


