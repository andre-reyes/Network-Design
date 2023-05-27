# Reliable Data Transfer over as Perfectly Reliable Channel: rdt1.0
import os.path



save_path = os.getcwd() + '\\src'
filename = "tedastn.bmp"
print(save_path)

data = open(os.path.join(save_path, filename), 'w')
data.close()