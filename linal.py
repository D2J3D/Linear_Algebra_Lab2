from manim import *
from math import *


class Transformations(LinearTransformationScene):
    def __init__(self):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            show_basis_vectors=True
        )

    def transform(self, matrix):
        self.apply_matrix(matrix)

    def object_setup(self):
        unit_square = self.get_unit_square()
        vect1 = self.get_vector([1, 2], color=PURPLE_B)
        vect2 = self.get_vector([1, 5], color=GREEN_B)
        VGroup(vect1, vect2, unit_square)
        self.add(vect1, vect2, unit_square)
        self.add_transformable_mobject(vect1, vect2, unit_square)

    def make_subtitles(self):
        matrix_tex = MathTex(
            "A = \\begin{bmatrix} \\frac{5}{3} & \\frac{-1}{3}\\\\\\frac{-2}{3} &\\frac{1}{3}\\end{bmatrix}").to_edge(
            DL)  # .add_background_rectangle()
        self.add_background_mobject(matrix_tex)


    def construct(self):
        matrix = [[5/3, -1/3], [-2/3, 1/3]]
        self.object_setup()
        self.make_subtitles()
        self.transform(matrix)
