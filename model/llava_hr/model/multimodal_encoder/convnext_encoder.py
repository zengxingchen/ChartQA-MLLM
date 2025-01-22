import torch
import torch.nn as nn
from timm import create_model
from transformers import CLIPImageProcessor
from .convnext import convnext_base_clip,convnext_large_mlp,convnext_xxlarge
from torch.utils.checkpoint import checkpoint



cfg={
    "crop_size": 256,
    "do_center_crop": True,
    "do_normalize": True,
    "do_resize": True,
    "feature_extractor_type": "CLIPFeatureExtractor",
    "image_mean": [
        0.48145466,
        0.4578275,
        0.40821073
    ],
    "image_std": [
        0.26862954,
        0.26130258,
        0.27577711
    ],
    "resample": 3,
    "size": 256
}

class ConvNextVisionTower(nn.Module):
    def __init__(self, vision_tower, args, delay_load=False):
        super().__init__()

        self.is_loaded = False
        self.freeze_vision=args.freeze_vision
        self.input_image_size=args.input_image_size
        self.vision_tower_name = vision_tower
        self.select_layer = args.mm_vision_select_layer
        self.select_feature = getattr(args, 'mm_vision_select_feature', 'patch')

        self.load_model()

    def load_model(self):
        self.image_processor = CLIPImageProcessor(**cfg)
        if 'xxlarge' in self.vision_tower_name:
            self.vision_tower = convnext_xxlarge(self.vision_tower_name)
            setattr(self.vision_tower, 'hidden_size', 3072)
        else:
            self.vision_tower = convnext_large_mlp(self.vision_tower_name)
            setattr(self.vision_tower, 'hidden_size', 1536)
        if self.freeze_vision:
            self.vision_tower.requires_grad_(False)

        # if self.vision_tower.grad_checkpointing:
        for s in self.vision_tower.stages:
            s.grad_checkpointing = True

        if self.input_image_size is not None:
            self.image_processor.size=self.input_image_size
            self.image_processor.crop_size={
                'height':self.input_image_size,
                'width': self.input_image_size
            }

        self.is_loaded = True

    def feature_select(self, image_forward_outs):

        if self.select_layer>100:
            image_features = image_forward_outs[-4:]
        else:
            image_features = image_forward_outs[-1]
        return image_features

    def forward_features(self, x):
        x = self.vision_tower.stem(x)
        image_forward_out=[]
        for blk in self.vision_tower.stages:
            x = blk(x)
            b,c,h,w=x.shape
            image_forward_out.append(x.view(b,c,-1).transpose(1,2))
        return image_forward_out

    def forward(self, images):
        if self.freeze_vision:
            with torch.no_grad():
                image_features = self._forward_images(images)
        else:
            image_features = self._forward_images(images)

        return image_features

    def _forward_images(self, images):
        if type(images) is list:
            image_features = []
            for image in images:
                image_forward_out = self.forward_features(image.to(device=self.device, dtype=self.dtype).unsqueeze(0))
                image_feature = self.feature_select(image_forward_out)
                image_features.append(image_feature)
        else:
            image_forward_outs = self.forward_features(images.to(device=self.device, dtype=self.dtype))
            image_features = self.feature_select(image_forward_outs)

        return image_features

    @property
    def dummy_feature(self):
        return torch.zeros(1, self.hidden_size, device=self.device, dtype=self.dtype)

    @property
    def dtype(self):
        return next(self.vision_tower.parameters()).dtype

    @property
    def device(self):
        return next(self.vision_tower.parameters()).device

    @property
    def config(self):
        assert  NotImplementedError
        pass

    @property
    def num_attention_heads(self):
        # as constant
        return 16
    @property
    def num_layers(self):
        # as constant
        return 4
    @property
    def hidden_size(self):
        return self.vision_tower.hidden_size

    @property
    def num_patches(self):
        return (cfg['image_size'] // self.patch_embed.patch_size[0]) ** 2
