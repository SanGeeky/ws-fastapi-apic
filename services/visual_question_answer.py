from transformers import ViltProcessor, ViltForQuestionAnswering
from PIL import Image


class VisualQuestionAnswering:
    """
    Multimodal model for visual question answering (VQA) with ViLT
    """
    def __init__(self) -> None:
        # Download the model if not present
        self.processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
        self.model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

    def pipeline(self, text: str, image: Image):
        encoding = self.processor(image, text, return_tensors="pt")

        outputs = self.model(**encoding)
        logits = outputs.logits
        idx = logits.argmax(-1).item()

        return self.model.config.id2label[idx]
