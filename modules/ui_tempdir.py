import os
import tempfile
from collections import namedtuple
from pathlib import Path
import gradio as gr
from PIL import PngImagePlugin
from modules import shared


Savedfile = namedtuple("Savedfile", ["name"])


def register_tmp_file(gradio, filename):
    if hasattr(gradio, 'temp_file_sets'):  # gradio 3.15
        gradio.temp_file_sets[0] = gradio.temp_file_sets[0] | {os.path.abspath(filename)}
    if hasattr(gradio, 'temp_dirs'):  # gradio 3.9
        gradio.temp_dirs = gradio.temp_dirs | {os.path.abspath(os.path.dirname(filename))}


def check_tmp_file(gradio, filename):
    if hasattr(gradio, 'temp_file_sets'):
        return any([filename in fileset for fileset in gradio.temp_file_sets])
    if hasattr(gradio, 'temp_dirs'):
        return any(Path(temp_dir).resolve() in Path(filename).resolve().parents for temp_dir in gradio.temp_dirs)
    return False


def save_pil_to_file(pil_image, dir=None): # pylint: disable=redefined-builtin
    already_saved_as = getattr(pil_image, 'already_saved_as', None)
    if already_saved_as and os.path.isfile(already_saved_as):
        register_tmp_file(shared.demo, already_saved_as)
        file_obj = Savedfile(already_saved_as)
        return file_obj
    if shared.opts.temp_dir != "":
        dir = shared.opts.temp_dir
    use_metadata = False
    metadata = PngImagePlugin.PngInfo()
    for key, value in pil_image.info.items():
        if isinstance(key, str) and isinstance(value, str):
            metadata.add_text(key, value)
            use_metadata = True
    file_obj = tempfile.NamedTemporaryFile(delete=False, suffix=".png", dir=dir)
    pil_image.save(file_obj, pnginfo=(metadata if use_metadata else None))
    return file_obj


# override save to file function so that it also writes PNG info
gr.processing_utils.save_pil_to_file = save_pil_to_file


def on_tmpdir_changed():
    if shared.opts.temp_dir == "":
        return
    register_tmp_file(shared.demo, os.path.join(shared.opts.temp_dir, "x"))


def cleanup_tmpdr():
    temp_dir = shared.opts.temp_dir
    if temp_dir == "" or not os.path.isdir(temp_dir):
        return
    for root, _dirs, files in os.walk(temp_dir, topdown=False):
        for name in files:
            _, extension = os.path.splitext(name)
            if extension != ".png" and extension != ".jpg" and extension != ".webp":
                continue
            filename = os.path.join(root, name)
            os.remove(filename)