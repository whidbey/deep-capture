import time
import matplotlib.pyplot as plt

import sys; sys.path.append('../../lib/python')
import deep_capture

import yolo_tf

import numpy as np
import cv2
import pygame
from pygame.locals import *

def main(argvs):
    SCREEN_SIZE = 448,448
    SCREEN_FLAG = DOUBLEBUF|HWSURFACE|RESIZABLE

    frame = cv2.imread('person.jpg')
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    yolo = yolo_tf.YOLO_TF()
    dc = deep_capture.create_display_capture()
    dc.init()
    dc.start()

    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, SCREEN_FLAG)
    pygame.display.set_caption("YOLO Screen")
    font = pygame.font.SysFont("Courier New",15)
    clock = pygame.time.Clock()

    detect = True
    running = True
    while running:
        clock.tick()
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == VIDEORESIZE:
                SCREEN_SIZE = event.dict['size']
                screen = pygame.display.set_mode(SCREEN_SIZE, SCREEN_FLAG)
            elif event.type == KEYDOWN:
                if event.unicode == "D":
                    detect = not detect

        buf = dc.get_buffer()
        frame = deep_capture.to_numpy(buf.buffer, buf.size)
        frame = frame.reshape((buf.height, buf.width, 4))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGB)
        frame = frame[150:448, 50:448]

        if detect:
            results = yolo.detect_from_cvmat(frame)
            img = yolo.show_results(frame, results)
        else:
            img = frame

        frame_sf = pygame.image.frombuffer(img.tostring(), img.shape[1::-1], "RGB")
        frame_sf = pygame.transform.smoothscale(frame_sf, SCREEN_SIZE)

        screen.fill((0,0,0))
        screen.blit(frame_sf, (0, 0))

        fps_sf = font.render("FPS: %.2f"%clock.get_fps(), True, (255, 0, 0))
        screen.blit(fps_sf, (0,0))

        pygame.display.flip()

    dc.stop()
    pygame.quit()

if __name__=='__main__':
    main(sys.argv)
