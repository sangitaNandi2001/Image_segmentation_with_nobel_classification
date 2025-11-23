# Iterate ov
import matplotlib.pyplot as plt
import cv2  # Add OpenCV import

def prewitt_operator(image):
    # Prewitt kernels for horizontal and vertical edges
    prewitt_kernel_x = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
    prewitt_kernel_y = [[-1, -1, -1], [0, 0, 0], [1, 1, 1]]

    height, width, channels = image.shape

    # If the image has four channels (RGBA), convert it to RGB
    
    if channels == 4:
        image = image[:, :, :3]

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Initialize arrays for horizontal and vertical edges
    edges_x = [[0] * width for _ in range(height)]
    edges_y = [[0] * width for _ in range(height)]

    # Convolve the image with the Prewitt kernels
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            edges_x[i][j] = (
                prewitt_kernel_x[0][0] * gray_image[i - 1, j - 1] +
                prewitt_kernel_x[0][1] * gray_image[i - 1, j] +
                prewitt_kernel_x[0][2] * gray_image[i - 1, j + 1] +
                prewitt_kernel_x[1][0] * gray_image[i, j - 1] +
                prewitt_kernel_x[1][1] * gray_image[i, j] +
                prewitt_kernel_x[1][2] * gray_image[i, j + 1] +
                prewitt_kernel_x[2][0] * gray_image[i + 1, j - 1] +
                prewitt_kernel_x[2][1] * gray_image[i + 1, j] +
                prewitt_kernel_x[2][2] * gray_image[i + 1, j + 1]
            )

            edges_y[i][j] = (
                prewitt_kernel_y[0][0] * gray_image[i - 1, j - 1] +
                prewitt_kernel_y[0][1] * gray_image[i - 1, j] +
                prewitt_kernel_y[0][2] * gray_image[i - 1, j + 1] +
                prewitt_kernel_y[1][0] * gray_image[i, j - 1] +
                prewitt_kernel_y[1][1] * gray_image[i, j] +
                prewitt_kernel_y[1][2] * gray_image[i, j + 1] +
                prewitt_kernel_y[2][0] * gray_image[i + 1, j - 1] +
                prewitt_kernel_y[2][1] * gray_image[i + 1, j] +
                prewitt_kernel_y[2][2] * gray_image[i + 1, j + 1]
            )

    # edges = [[(edges_x[i][j]*2 + edges_y[i][j]2)*0.5 for j in range(width)] for i in range(height)]
    edges = [[((edges_x[i][j]**2 + edges_y[i][j]**2)**0.5) for j in range(width)] for i in range(height)]


    return edges
image_path = ("image\\Lena-gray.png")
image = plt.imread(image_path)
prewitt_edges = prewitt_operator(image)

# Plot the original image
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

# Plot the edges detected by the Prewitt operator
plt.subplot(1, 2, 2)
plt.imshow(prewitt_edges, cmap='gray')
plt.title('Edges (Prewitt Operator)')

# Show the plots
plt.show()       

