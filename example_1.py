# Example shows how to interuct with the realsense camera.

import lib
import matplotlib.pyplot as plt

def example_1(): 

    realsense_presence = lib.check_if_realsense_is_present(print_logs= True)

    if realsense_presence:
        print("Realsense camera is present")
        realsense_config = lib.get_realsense_camera_config()
        print(realsense_config)

        #get color and depth image
        color_image, depth_image = lib.get_rgb_and_depth_image_from_realsense()

        fig = plt.figure(figsize=(14,7))

        fig.add_subplot(1,2,1)
        plt.imshow(color_image)
        fig.add_subplot(1,2,2)
        plt.imshow(depth_image)

        plt.show()

        #get depth point cloud
        lib.save_ply_file_from_realsense(filename="example_1")
        lib.view_cloude_point_from_ply("example_1.ply")   

    else:
        print("Realsense camera is not present")
        

        #get point cloud




if __name__ == "__main__":
    example_1()