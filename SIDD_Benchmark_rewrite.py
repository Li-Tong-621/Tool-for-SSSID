from natsort import natsorted
from glob import glob
import cv2
import numpy as np
import scipy.io
import numpy as np
import pandas as pd
import base64

def array_to_base64string(x):
    array_bytes = x.tobytes()
    base64_bytes = base64.b64encode(array_bytes)
    base64_string = base64_bytes.decode('utf-8')
    return base64_string


def base64string_to_array(base64string, array_dtype, array_shape):
    decoded_bytes = base64.b64decode(base64string)
    decoded_array = np.frombuffer(decoded_bytes, dtype=array_dtype)
    decoded_array = decoded_array.reshape(array_shape)
    return decoded_array
denoised_paths = natsorted(glob('/data4/litong/Pycode/DN/ZS-N2N/results/sidd_bench/*'))
output_blocks_base64string = []
for i in denoised_paths:
    out_block = cv2.imread(i)
    out_block = cv2.cvtColor(out_block, cv2.COLOR_BGR2RGB)
    out_block_base64string = array_to_base64string(out_block)
    output_blocks_base64string.append(out_block_base64string)

# Save outputs to .csv file.
output_file = './results/SubmitSrgb.csv'
print(f'Saving outputs to {output_file}')
output_df = pd.DataFrame()
n_blocks = len(output_blocks_base64string)
print(f'Number of blocks = {n_blocks}')
output_df['ID'] = np.arange(n_blocks)
output_df['BLOCK'] = output_blocks_base64string

output_df.to_csv(output_file, index=False)
print('Done.')
