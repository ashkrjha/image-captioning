
resnet = ResNet50(include_top=False,weights='imagenet',input_shape=(224,224,3),pooling='avg')