import os, imghdr, uuid
import numpy as np
from PIL import Image
# from pathlib import Path

class ImagePixelator:
    def __init__(self, fp, n_px: int) -> None:

        if(not imghdr.what(fp)):
            raise IOError(2, "No such file or directory")
        
        self.file_ext = os.path.splitext(fp)[1]
        if(self.file_ext != ".jpg" and self.file_ext != ".png"):
            raise TypeError(2, "File type not supported")
        else:
            image = Image.open(fp)

        transformed_image = image.resize((n_px, n_px), resample=Image.Resampling.BILINEAR)
        self.pixel_array = np.asarray(transformed_image)
        image.close()
        transformed_image.close()

    def get_pixels(self):
        return self.pixel_array
    
    def get_extension(self):
        return self.file_ext

class ImageBuilder:
    def __init__(self, pixel_data: np.ndarray, name_id: any = None, sample: bool = False) -> None:

        image = Image.fromarray(pixel_data.astype(np.uint8))
        self.image_id = uuid.uuid4()
        if(name_id == None):
            self.filename = "image-%s.jpg"%(str(self.image_id)[0:4])
            fp = (r"../images/results/image-" 
             + str(self.image_id)[0:4] 
             + r".jpg")
        
            image.save(fp, 'JPEG')
        else:
            id = str(name_id)
            self.filename = "image-%s.jpg"%(id[0:6])
            fp = (r"../images/results/image-" 
                + id[0:6] 
                + r".jpg")
            image.save(fp, 'JPEG')

        image.close()
