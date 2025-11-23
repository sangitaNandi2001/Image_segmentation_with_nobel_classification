import matplotlib.pyplot as plt
import cv2  # Add OpenCV import

def sobel_operator(image):
    # Sobel kernels for horizontal and vertical edges
    sobel_kernel_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    sobel_kernel_y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]

    # Get image dimensions
    height, width, channels = image.shape

    # If the image has four channels (RGBA), convert it to RGB
    if channels == 4:
        image = image[:, :, :3]

    # Convert the image to grayscale using OpenCV
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Initialize arrays for horizontal and vertical edges
    edges_x = [[0] * width for _ in range(height)]
    edges_y = [[0] * width for _ in range(height)]

    # Convolve the image with the Sobel kernels
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            edges_x[i][j] = (
                sobel_kernel_x[0][0] * gray_image[i - 1, j - 1] +
                sobel_kernel_x[0][1] * gray_image[i - 1, j] +
                sobel_kernel_x[0][2] * gray_image[i - 1, j + 1] +
                sobel_kernel_x[1][0] * gray_image[i, j - 1] +
                sobel_kernel_x[1][1] * gray_image[i, j] +
                sobel_kernel_x[1][2] * gray_image[i, j + 1] +
                sobel_kernel_x[2][0] * gray_image[i + 1, j - 1] +
                sobel_kernel_x[2][1] * gray_image[i + 1, j] +
                sobel_kernel_x[2][2] * gray_image[i + 1, j + 1]
            )

            edges_y[i][j] = (
                sobel_kernel_y[0][0] * gray_image[i - 1, j - 1] +
                sobel_kernel_y[0][1] * gray_image[i - 1, j] +
                sobel_kernel_y[0][2] * gray_image[i - 1, j + 1] +
                sobel_kernel_y[1][0] * gray_image[i, j - 1] +
                sobel_kernel_y[1][1] * gray_image[i, j] +
                sobel_kernel_y[1][2] * gray_image[i, j + 1] +
                sobel_kernel_y[2][0] * gray_image[i + 1, j - 1] +
                sobel_kernel_y[2][1] * gray_image[i + 1, j] +
                sobel_kernel_y[2][2] * gray_image[i + 1, j + 1]
            )

    edges = []

    # Iterate over each row in the image
    for i in range(height):
        row_edges = []
        for j in range(width):
            horizontal_edge = edges_x[i][j]
            vertical_edge = edges_y[i][j]
            edge_magnitude = (horizontal_edge**2 + vertical_edge**2)**0.5
            row_edges.append(edge_magnitude)
        edges.append(row_edges)

    return edges

# Load an example image (replace with your image path)
image = plt.imread(r"D:\\PROJECT-2\\image\\Lena-gray.png")  # Change the file extension based on your image format

# Apply the Sobel operator for edge detection
sobel_edges = sobel_operator(image)

# Plot the original image
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')

# Plot the edges detected by the Sobel operator
plt.subplot(1, 2, 2)
plt.imshow(sobel_edges, cmap='gray')
plt.title('Edges (Sobel Operator)')

# Show the plots
plt.show()
