import ImgClassify_pb2 as simple_pb2

received_imgs = simple_pb2.imgs()
received_imgs.num_img = 1
single_image = received_imgs.all_img.add()
single_image.single_img.extend([1,2,3,4])
single_image = received_imgs.all_img.add()
single_image.single_img.extend([4,3,2,1])

simple_message = simple_pb2.classified()
simple_message.num_img = 3
sample_list = simple_message.classes
sample_list.append("l")
sample_list.append("s")
sample_list.append("j")

print(simple_message)

with open("simple.bin", "wb") as f:
    print("write as binary")
    bytesAsString = simple_message.SerializeToString()
    f.write(bytesAsString)

with open("simple.bin", "rb") as f:
    print("read values")
    simple_message_read = simple_pb2.classified().FromString(f.read())

print(simple_message_read)

print(received_imgs)
