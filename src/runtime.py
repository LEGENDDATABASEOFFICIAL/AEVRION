"""
=========================================================
 AEVRION Programming Language v0.4
 Runtime System
=========================================================
"""

class Runtime:
    """
    Runtime manager.
    The startup animation has been removed to match
    the classic AEVRION v0.2 interface.
    """

    def __init__(self):
        self.version = "0.4.0 Alpha"
        self.running = False

    def startup(self):
        """
        Start runtime silently.
        """
        self.running = True

    def shutdown(self):
        """
        Stop runtime silently.
        """
        self.running = False

    def is_running(self):
        return self.running
