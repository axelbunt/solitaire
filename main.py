import ctypes

# noinspection PyUnresolvedReferences
import hide_pg_prompt  # need to be the first import

from start_game import start


if __name__ == '__main__':
    my_app_id = u'solitaire'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app_id)

    start()
