import logging
import subprocess
import threading

import psutil

from context import Context
from freddielib.utils.freddie_utils import get_operating_system
from freddielib.utils.thread_utils import CancellationToken


class FreddieCppWrapper(threading.Thread):
    """
    A wrapper for the freddie_cpp module. It simply calls the module using information used from the context.
    """

    def __init__(self, context: Context):
        # load stuff from context
        self.workspace = context.workspace
        self.freddie_cpp_dir = context.freddie_cpp_dir
        self.frame_count = context.frame_count
        self.block_size = context.block_size
        self.step_size = context.step_size
        self.extension_type = context.extension_type
        self.residual_images_dir = context.residual_images_dir
        self.log_dir = context.console_output_dir
        self.freddie_cpp_subprocess = None

        self.exec_command = [self.freddie_cpp_dir,
                             self.workspace,
                             str(self.frame_count),
                             str(self.block_size),
                             str(self.step_size),
                             "n",
                             str(1),
                             self.extension_type]

        # Threading Specific

        self.alive = True
        self.cancel_token = CancellationToken()
        self._stopevent = threading.Event()
        threading.Thread.__init__(self, name="FreddieCpp")

    def join(self, timeout=None):
        print("freddiecpp killed")
        threading.Thread.join(self, timeout)

    def kill(self):
        self.alive = False
        self.cancel_token.cancel()
        self._stopevent.set()

        d2xcpp_psutil = psutil.Process(self.freddie_cpp_subprocess.pid)
        d2xcpp_psutil.kill()

    def set_start_frame(self, start_frame):
        self.exec_command = [self.freddie_cpp_dir,
                             self.workspace,
                             str(self.frame_count),
                             str(self.block_size),
                             str(self.step_size),
                             "r",
                             str(start_frame),
                             self.extension_type]

    def run(self):
        logger = logging.getLogger(__name__)

        logger.info(self.exec_command)

        # On linux, we can't use subprocess.create_new_console, so we just write
        # The freddie_cpp output to a text file.
        if get_operating_system() == 'win32':
            self.freddie_cpp_subprocess = subprocess.Popen(self.exec_command,
                                                             creationflags=subprocess.CREATE_NEW_CONSOLE)

        elif get_operating_system() == 'linux':
            console_output = open(self.log_dir + "freddie_cpp.txt", "w")
            console_output.write(str(self.exec_command))
            self.freddie_cpp_subprocess = subprocess.Popen(self.exec_command, shell=False, stderr=console_output,
                                                             stdout=console_output)

        if self.freddie_cpp_subprocess.returncode == 0:
            logger.info("d2xcpp finished correctly")
        else:
            logger.info("d2xcpp ended unexpectedly")
