import json
import os
import sys
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, ListView, ListItem
from textual.containers import Horizontal
from textual.reactive import reactive
from PIL import Image


class ReviewApp(App):
    CSS = """
    Screen {
        layout: vertical;
    }
    #main {
        layout: horizontal;
    }
    #text {
        width: 40%;
        border: solid white;
        padding: 1;
    }
    #images {
        width: 30%;
        border: solid white;
    }
    #preview {
        width: 30%;
        border: solid white;
    }
    """

    slide_index = reactive(0)
    image_index = reactive(0)

    def __init__(self, path):
        super().__init__()
        self.path = path
        with open(os.path.join(path, "slides.json")) as f:
            self.slides = json.load(f)

    def compose(self) -> ComposeResult:
        yield Header()

        with Horizontal(id="main"):
            self.text_box = Static(id="text")
            self.image_list = ListView(id="images")
            self.preview = Static(id="preview")

            yield self.text_box
            yield self.image_list
            yield self.preview

        yield Footer()

    def on_mount(self):
        self.load_slide()

    def load_slide(self):
        slide = self.slides[self.slide_index]

        self.text_box.update(slide["text"][:1000])

        self.image_list.clear()
        for img in slide["images"]:
            self.image_list.append(ListItem(Static(f"[x] {img}")))

        self.image_index = 0
        self.update_preview()

    def update_preview(self):
        slide = self.slides[self.slide_index]
        if not slide["images"]:
            self.preview.update("No image")
            return

        img_path = slide["images"][self.image_index]

        try:
            img = Image.open(img_path)
            img.thumbnail((400, 400))
            self.preview.update(f"[Preview]\n{img_path}")
        except:
            self.preview.update("Error loading image")

    def action_next_slide(self):
        if self.slide_index < len(self.slides) - 1:
            self.slide_index += 1
            self.load_slide()

    def action_prev_slide(self):
        if self.slide_index > 0:
            self.slide_index -= 1
            self.load_slide()

    def action_next_image(self):
        slide = self.slides[self.slide_index]
        if self.image_index < len(slide["images"]) - 1:
            self.image_index += 1
            self.update_preview()

    def action_prev_image(self):
        if self.image_index > 0:
            self.image_index -= 1
            self.update_preview()

    def action_toggle(self):
        slide = self.slides[self.slide_index]
        if not slide["images"]:
            return

        img = slide["images"][self.image_index]

        if "removed" not in slide:
            slide["removed"] = []

        if img in slide["removed"]:
            slide["removed"].remove(img)
        else:
            slide["removed"].append(img)

        self.load_slide()

    def action_select_all(self):
        slide = self.slides[self.slide_index]
        slide["removed"] = []

        self.load_slide()

    def action_deselect_all(self):
        slide = self.slides[self.slide_index]
        slide["removed"] = slide["images"][:]

        self.load_slide()

    def action_save(self):
        # apply removals
        for slide in self.slides:
            if "removed" in slide:
                slide["images"] = [
                    img for img in slide["images"] if img not in slide["removed"]
                ]

        with open(os.path.join(self.path, "slides.json"), "w") as f:
            json.dump(self.slides, f, indent=2)

        self.exit("Saved!")

    BINDINGS = [
        ("j", "next_image"),
        ("k", "prev_image"),
        ("down", "next_image"),
        ("up", "prev_image"),
        ("l", "next_slide"),
        ("h", "prev_slide"),
        ("right", "next_slide"),
        ("left", "prev_slide"),
        ("enter", "toggle"),
        ("space", "toggle"),
        ("a", "select_all"),
        ("d", "deselect_all"),
        ("s", "save"),
        ("q", "quit"),
    ]


if __name__ == "__main__":
    path = sys.argv[1]
    app = ReviewApp(path)
    app.run()
