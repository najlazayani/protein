# This is a sample Python script.
import igl


import numpy as np


# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



import open3d as o3d

def read_mesh_from_off(database_path):
    mesh_file = database_path + "/1.off"  # Replace "example.off" with the actual filename of the .OFF file in your database

    mesh = o3d.io.read_triangle_mesh(mesh_file)

    return mesh

def read_txt_file():
    file_path = "C:/Users/pc/Desktop/FaceNet/SHREC2021/dataset/training_set/properties/1.txt"  # Replace with the actual path to your file

    # Read the file and store its contents in a list
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Process the data as needed
    data = []
    vector = []

    for line in lines:
        values = line.strip().split()  # Split the line by whitespace
        values = [float(val) for val in values]  # Convert values to float
        data.append(values)

    # Print the data

        print(data)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


 database_path ="./SHREC2021/dataset/training_set/OFFs";
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

file_path = "./SHREC2021/dataset/training_set/properties/1.txt"
read_txt_file()


