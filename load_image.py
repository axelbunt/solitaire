import os
import pygame as pg


def load_image(name: str, color_key=None) -> pg.Surface:
    filename = os.path.join('data', name)
    try:
        img = pg.image.load(filename).convert()
    except pg.error as message:
        print(f'File {filename} is absent')
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = img.get_at((0, 0))
        img.set_colorkey(color_key)
    else:
        img = img.convert_alpha()

    return img
