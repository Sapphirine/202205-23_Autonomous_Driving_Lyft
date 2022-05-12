import zarr
import numpy as np

z = zarr.open("C:\Users\11063\Desktop\lyft_level5\sample\sample.zarr\agents", mode="w", shape=(500,), dtype=np.float32, chunks=(100,))

    # We can write to it by assigning to it. This gets persisted on disk.
z[0:150] = np.arange(150)

print(z.info)