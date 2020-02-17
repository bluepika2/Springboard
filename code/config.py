backbone = 'unet'
dataset = 'coco'
batch_size = 4
workers = 6
checkname = backbone
# checkname = 'deeplab-' + backbone
out_stride = 16
sync_bn = False
freeze_bn = False
lr = 0.1
momentum = 0.9
weight_decay = 5e-4
nesterov = False
useCUDA = True
gpu_ids = str(0)
loss_type = 'ce'
lr_scheduler = 'poly'
epochs = 10
base_size = 513
crop_size = 513
eval_interval = 2