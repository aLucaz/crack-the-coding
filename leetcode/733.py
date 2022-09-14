"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color.
You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting
pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on.
 Replace the color of all the aforementioned pixels with color.

Return the modified image after performing the flood fill.

O(nxm)

"""

from typing import List


class Solution:

    def reviewFourSides(self, image, sr, sc, color, curr_value, nr, nc):
        image[sr][sc] = color
        for dir in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
            sr_aux = sr + dir[0]
            sc_aux = sc + dir[1]
            if (0 <= sr_aux <= nr) and (0 <= sc_aux <= nc):
                print(image[sr_aux][sc_aux])
                if image[sr_aux][sc_aux] == curr_value:
                    self.reviewFourSides(image, sr_aux, sc_aux, color, curr_value, nr, nc)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        curr_value = image[sr][sc]
        if curr_value == color:
            return image
        nr = len(image) - 1
        nc = len(image[0]) - 1
        self.reviewFourSides(image, sr, sc, color, curr_value, nr, nc)
        return image


if __name__ == '__main__':
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    sr = 1
    sc = 1
    color = 2
    s = Solution().floodFill(image, sr, sc, color)
    print(s)

