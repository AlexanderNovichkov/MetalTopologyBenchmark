import itertools

from gudhi.simplex_tree import SimplexTree


def make_boundary_matrix(simplex_tree: SimplexTree) -> list[list]:
    simplex_to_id = {}
    boundary_matrix = []
    for simlex, filtration in simplex_tree.get_filtration():
        simplex_to_id[tuple(simlex)] = len(simplex_to_id)
        boundary = []
        for boundary_simplex in itertools.combinations(simlex, len(simlex) - 1):
            if len(boundary_simplex) > 0:
                boundary.append(simplex_to_id[boundary_simplex])
        boundary.sort()
        boundary_matrix.append(boundary)
    return boundary_matrix


def write_boundary_matrix_with_metal_format(path: str, boundary_matrix: list[list]):
    non_zeros = 0
    for col in boundary_matrix:
        non_zeros += len(col)

    with open(path, 'w') as f:
        lines = [f'{len(boundary_matrix)} {non_zeros}']
        for col in boundary_matrix:
            lines.append("{} {}".format(len(col), " ".join(map(str, col))))
        result = "\n".join(lines)
        f.writelines(result)


def write_boundary_matrix_with_phat_format(path: str, boundary_matrix: list[list]):
    with open(path, 'w') as f:
        lines = []
        for col in boundary_matrix:
            lines.append("{} {}".format(max(0, len(col) - 1), " ".join(map(str, col))))
        result = "\n".join(lines)
        f.writelines(result)
