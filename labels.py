import json
import numpy as np
#"C:\\Users\\Korisnik\\Desktop\\testovi za drugi zadatak\\public\\set\\1\\bboxes.json"
#"C:\\Users\\Korisnik\\Desktop\\testovi za drugi zadatak\\public\\set\\1\\joints.json"
# json_data = (
#     input())
# bboxes_data = json.load(open(json_data))
# json_data = (
#     input())

json_data = (
    "C:\\Users\\Korisnik\\Desktop\\testovi za drugi zadatak\\public\\set\\14\\bboxes.json")
bboxes_data = json.load(open(json_data))
json_data = (
    "C:\\Users\\Korisnik\\Desktop\\testovi za drugi zadatak\\public\\set\\14\\joints.json")
joints_data = json.load(open(json_data))

identity_data_save1 = []  # bbox
identity_data_save2 = []  # joints
bounding_box_coordinates = []
joint_coordinates = []


def get_bbox_indentity():
    frames_list = bboxes_data['frames']
    for frames in frames_list:
        bounding_box_list = frames['bounding_boxes']
        for item in bounding_box_list:
            identity = item['identity']
            #coordinate = item['bounding_box']
            identity_data_save1.append(identity)
            # bounding_box_coordinates.append(coordinate)
    return list(set(identity_data_save1))


def get_joint_indentity():
    frames_list = joints_data['frames']
    for frames in frames_list:
        joint_list = frames['joints']
        for item in joint_list:
            identity = item['identity']
            identity_data_save2.append(identity)
            #coordinate = item['joint']
            # joint_coordinates.append(coordinate)
    return list(set(identity_data_save2))


def is_in_box(x, y, h, w, jx, jy):
    return (x < jx < x+w) and (y < jy < y+h)


def increase_connection_matrix(matrix, identity_box, identity_joint):
    matrix[list_bbox_identity.index(identity_box)][list_joint_identity.index(
        identity_joint)] = matrix[list_bbox_identity.index(identity_box)][list_joint_identity.index(identity_joint)] + 1
    return matrix


list_bbox_identity = get_bbox_indentity()
list_joint_identity = get_joint_indentity()
matrix = np.zeros(((len(list_bbox_identity), len(list_joint_identity))))
# print(matrix)


def check_joints(frame_index_box, identity_box, lista_koordinata_box):
    frames_list = joints_data['frames']
    frame_ = frames_list[frame_index_box]
    joint_list = frame_['joints']
    for item in joint_list:
        identity = item['identity']
        joints_dict = item['joint']
        koordinate = list(joints_dict.values())
        if(is_in_box(lista_koordinata_box[2], lista_koordinata_box[3], lista_koordinata_box[0], lista_koordinata_box[1], koordinate[0], koordinate[1])):
            increase_connection_matrix(matrix, identity_box, identity)

            # print(lista_koordinata_box[0], lista_koordinata_box[1], lista_koordinata_box[2],
            #       lista_koordinata_box[3], "box a u boxu je ", koordinate[0], koordinate[1])


frames_list = bboxes_data['frames']
num_frame = -1
for frames in frames_list:
    num_frame = num_frame+1
    bounding_box_list = frames['bounding_boxes']
    for item in bounding_box_list:
        identity = item['identity']
        bounding_box_dict = item['bounding_box']
        koordinate_box = list(bounding_box_dict.values())
        check_joints(num_frame, identity, koordinate_box)

max_i = 0
max_j = 0
no_of_rows = len(matrix)
no_of_column = len(matrix[0])
for i in range(no_of_rows):
    max1 = 0
    for j in range(no_of_column):
        if matrix[i][j] > max1:
            max1 = matrix[i][j]
            max_i = i
            max_j = j
    if(max1 != 0):
        ispis = list_joint_identity[max_j]+":"+list_bbox_identity[max_i]
    else:
        continue
    print(ispis)
