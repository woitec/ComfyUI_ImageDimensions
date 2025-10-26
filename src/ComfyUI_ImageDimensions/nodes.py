import torch

class ImageDimensionsExtractorInt:
    """
    ComfyUI Custom node that extracts dimensions from an image tensor and returns it.
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "extract_dimensions_int"
    CATEGORY = "ImageDimensions"

    def extract_dimensions_int(self, image: torch.Tensor):
        try:
            # Expected shape: [B, H, W, C]
            _, h, w, _ = image.shape
            return (int(w), int(h))
        except Exception as e:
            print(f"[ImageDimensionsExtractorInt] Warning: failed to extract dimensions ({e})")
            return (-1, -1)

class ImageDimensionsExtractorFloat:
    """
    ComfyUI Custom node that extracts dimensions from an image tensor and returns it.
    """
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
            },
        }

    RETURN_TYPES = ("FLOAT", "FLOAT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "extract_dimensions_float"
    CATEGORY = "ImageDimensions"

    def extract_dimensions_float(self, image: torch.Tensor):
        try:
            # Expected shape: [B, H, W, C]
            _, h, w, _ = image.shape
            return (float(w), float(h))
        except Exception as e:
            print(f"[ImageDimensionsExtractorInt] Warning: failed to extract dimensions ({e})")
            return (-1, -1)

NODE_CLASS_MAPPINGS = {
    "ImageDimensionsExtractorInt": ImageDimensionsExtractorInt,
    "ImageDimensionsExtractorFloat": ImageDimensionsExtractorFloat
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ImageDimensionsExtractorInt": "Extract Image Dimensions (Int)",
    "ImageDimensionsExtractorFloat": "Extract Image Dimensions (Float)"
}