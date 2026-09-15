import os
import math
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
import imageio

def create_cinematic_loop():
    input_path = os.path.join("assets", "fayis_portrait.jpg")
    output_path = os.path.join("assets", "fayis_portrait.mp4")
    
    if not os.path.exists(input_path):
        input_path = os.path.join("assets", "fayis_portrait.jpeg")
    
    print(f"Loading portrait from: {input_path}")
    orig_img = Image.open(input_path).convert("RGB")
    orig_w, orig_h = orig_img.size
    print(f"Original resolution: {orig_w}x{orig_h}")
    
    # Target video resolution (3:4 ratio, e.g., 720x960)
    target_w, target_h = 720, 960
    
    fps = 30
    duration_sec = 6.0
    total_frames = int(fps * duration_sec)
    
    print(f"Generating {total_frames} frames ({duration_sec}s @ {fps}fps) -> {output_path}...")
    
    writer = imageio.get_writer(
        output_path,
        fps=fps,
        codec='libx264',
        quality=9,
        pixelformat='yuv420p',
        macro_block_size=16,
        ffmpeg_params=['-movflags', '+faststart', '-preset', 'medium', '-crf', '18']
    )
    
    # Center crop base image to 3:4 aspect ratio with slight padding for zoom
    # 3:4 crop
    target_ratio = target_w / target_h
    current_ratio = orig_w / orig_h
    
    if current_ratio > target_ratio:
        crop_h = orig_h
        crop_w = int(orig_h * target_ratio)
    else:
        crop_w = orig_w
        crop_h = int(orig_w / target_ratio)
        
    crop_x = (orig_w - crop_w) // 2
    # Adjust y crop slightly higher to keep head and chest centered
    crop_y = int((orig_h - crop_h) * 0.25)
    
    base_cropped = orig_img.crop((crop_x, crop_y, crop_x + crop_w, crop_y + crop_h))
    
    # Pre-render a slightly larger canvas so zoom crops don't hit edges
    margin = 32
    expanded_w = target_w + margin * 2
    expanded_h = target_h + margin * 2
    expanded_base = base_cropped.resize((expanded_w, expanded_h), Image.Resampling.LANCZOS)
    
    # Generate seamless sinusoidal loop
    for i in range(total_frames):
        t = i / total_frames  # 0.0 to 1.0
        
        # 1. Slow, steady cinematic camera push-in and return:
        # Smooth cosine curve: 0 at t=0, 1 at t=0.5, 0 at t=1.0
        cycle_weight = 0.5 * (1.0 - math.cos(2.0 * math.pi * t))
        
        # Micro push-in: 1.0 to 1.026
        scale = 1.0 + 0.026 * cycle_weight
        
        # 2. Natural breathing micro-motion (slight chest/body float)
        # Vertical displacement: -1.5px to +1.5px
        dy = 1.5 * math.sin(2.0 * math.pi * t)
        
        # Subtle horizontal micro-drift (0.5px)
        dx = 0.6 * math.sin(4.0 * math.pi * t)
        
        # 3. Soft ambient light breathing (subtle warmth/contrast oscillation)
        # Gives organic depth without morphing
        brightness_factor = 1.0 + 0.012 * cycle_weight
        contrast_factor = 1.0 + 0.010 * cycle_weight
        
        # Calculate crop coordinates on expanded canvas
        current_w = target_w / scale
        current_h = target_h / scale
        
        center_x = (expanded_w / 2.0) + dx
        center_y = (expanded_h / 2.0) + dy
        
        left = center_x - (current_w / 2.0)
        top = center_y - (current_h / 2.0)
        right = left + current_w
        bottom = top + current_h
        
        frame_img = expanded_base.crop((left, top, right, bottom))
        frame_img = frame_img.resize((target_w, target_h), Image.Resampling.BICUBIC)
        
        # Apply subtle organic lighting adjustment
        if brightness_factor != 1.0:
            enhancer = ImageEnhance.Brightness(frame_img)
            frame_img = enhancer.enhance(brightness_factor)
            
        if contrast_factor != 1.0:
            c_enhancer = ImageEnhance.Contrast(frame_img)
            frame_img = c_enhancer.enhance(contrast_factor)
            
        frame_np = np.array(frame_img)
        writer.append_data(frame_np)
        
        if (i + 1) % 30 == 0 or i == total_frames - 1:
            print(f"Processed frame {i + 1}/{total_frames} ({(i + 1)/total_frames*100:.1f}%)")
            
    writer.close()
    file_size = os.path.getsize(output_path)
    print(f"Successfully generated cinematic MP4: {output_path} ({file_size} bytes)")

if __name__ == "__main__":
    create_cinematic_loop()
