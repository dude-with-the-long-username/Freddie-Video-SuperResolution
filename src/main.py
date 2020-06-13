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
        # print("LR frame number", frame.index)
        np_frame = frame.to_ndarray(format='rgb24')
        if start_of_scene(frame):
            prev_np_frame = np_frame
            upscaled_frame = np_frame_upscale(np_frame)
            send_to_playback_buffer(np_frame)
        else:
            diff = np.subtract(np_frame, prev_np_frame)
            #write diff to /train
            np.save("train/lr/%s" % str(frame.index), np.asarray(diff))
            upscaled_diff = np_frame_upscale(diff)
            print("size of diff", len(upscaled_diff.nonzero()[0]))
            frame_merge(upscaled_frame, upscaled_diff)
            send_to_playback_buffer(upscaled_frame)

def frame_merge(latest_frame, upscaled_diff):
    """Replace pixels in latest_frame with corresponding non zero
    pixels in upscaled_diff

    :latest_frame: Latest upscaled frame as numpy array
    :upscaled_diff: Upscaled diff of new frame as numpy array
    :returns: Writes merge of latest_frame and upscaled_diff to latest_frame

    """
    latest_frame[upscaled_diff.nonzero(
    )] += upscaled_diff[upscaled_diff.nonzero()]


if __name__ == "__main__":
    # filename = sys.argv[1]
    super_res('v/mha_s4_ep2.mp4')
