from random import choice
from transformers import ViltProcessor, ViltForQuestionAnswering
from PIL import Image


class VisualQuestionAnswering:
    """
    Multimodal model for visual question answering (VQA) with ViLT
    """
    emojis = ["🤫", "🤩", "🧐", "🤠", "👀", "✅", "🧚", "🥳", "🥸"]

    def __init__(self) -> None:
        # Download the model if not present
        self.processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
        self.model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

    def pipeline(self, text: str, image: Image):
        encoding = self.processor(image, text, return_tensors="pt")

        outputs = self.model(**encoding)
        logits = outputs.logits
        idx = logits.argmax(-1).item()

        self.result = self.model.config.id2label[idx]

        return self.result

    @property
    def format_answer(self):
        return f"{self.result} {choice(self.emojis)}."
