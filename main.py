# This is a sample Python script.
import igl
import meshplot as mp
import numpy as  np
# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



import open3d as o3d

def read_mesh_from_off(database_path):
    mesh_file = database_path + "/1.off"  # Replace "example.off" with the actual filename of the .OFF file in your database

    mesh = o3d.io.read_triangle_mesh(mesh_file)

    return mesh



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
 """""
 database_path ="C:/Users/pc/Desktop/FaceNet/SHREC2021/dataset/training_set/OFFs";
 mesh = read_mesh_from_off(database_path)
 print(mesh)
 vertices = mesh.vertices  # Access the vertices of the mesh
 faces = mesh.triangles  # Access the faces of the mesh
 vertices_np = np.asarray(vertices)
 faces_np = np.asarray(faces)

 print("Vertices:")
 print(vertices_np)

 print("Faces:")
 print(faces_np)
"""
 v, f = igl.read_triangle_mesh('C:/Users/pc/Desktop/FaceNet/SHREC2021/dataset/training_set/OFFs/1.off')
 mp.plot(v, f)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
