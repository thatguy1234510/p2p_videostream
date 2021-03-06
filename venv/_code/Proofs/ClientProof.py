from ..streambase import streamclient
import cv2

demoClient = streamclient.Client("192.168.0.36", port=5000, verbose=True)


def startStream(Cli):
    """Decodes files from stream and displays them"""
    Cli.initializeStream()  # decode initial frame
    cv2.namedWindow("feed", cv2.WINDOW_NORMAL)
    print("streaminitialized")
    while True:
        img = Cli.decodeFrame()  # decode frame

        cv2.imshow("feed", img)

        if cv2.waitKey(1) == 27:
            Cli.close(destroy=True)
            break  # esc to quit


startStream(demoClient)
